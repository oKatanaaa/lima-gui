import pandas as pd
from functools import partial
from copy import deepcopy
from PySide6.QtWidgets import QMessageBox, QFileDialog

from lima_gui.logging import all_methods_logger
from lima_gui.view.main_window import MainWindow
from lima_gui.view.chat_window import ChatWindow
from lima_gui.view.settings_window import SettingsWindow
from lima_gui.model.chat_dataset import ChatDataset
from lima_gui.model.chat import Chat
from .chat_controller import ChatController
from .settings_controller import SettingsController
from .openai_controller import OpenAIController


@all_methods_logger
class Controller:
    def __init__(self, main_window: MainWindow):
        self.main_window = main_window
        self.openai_controller = OpenAIController(self.main_window.openai_window)
        self.main_window.set_column_names(['Chat name', 'Language', 'Msg count'])
        
        self.main_window.set_add_chat_callback(self.on_add_chat_clicked)
        self.main_window.set_delete_chat_callback(self.on_delete_chat_clicked)
        self.main_window.set_chat_double_clicked_callback(self.on_chat_double_clicked)
        self.main_window.set_save_to_callback(self.on_save_triggered)
        self.main_window.set_save_current_callback(self.on_save_current_triggered)
        self.main_window.set_export_as_openai_dataset_callback(self.on_export_as_openai_dataset_triggered)
        self.main_window.set_post_open_callback(self.on_post_open_triggered)
        self.main_window.set_pre_open_callback(self.on_pre_open_triggered)
        self.main_window.set_settings_callback(self.on_settings_clicked)
        self.main_window.set_copy_chat_callback(self.on_copy_chat_clicked)
        self.main_window.set_close_even_happened_callback(self.close_application)
        self.main_window.show()
        
        self.dataset = ChatDataset([])
        self.last_dataset_hash = hash(self.dataset)
        self.dataset_path = None
        
        self.chat_controllers = set()
    
    def on_save_triggered(self, filename):
        # TODO: improve it
        if filename.endswith('.csv'):
            self.dataset.save_csv(filename)
        else:
            self.dataset.save_jsonl(filename)
        self.last_dataset_hash = hash(self.dataset)
        self.dataset_path = filename
    
    def on_save_current_triggered(self):
        # TODO: improve it
        if self.dataset_path is None:
            filename = QFileDialog.getSaveFileName(None, 'Save file', '', 'All Files (*)')
            if filename[0]:
                self.dataset_path = filename[0]
            else:
                return
        if self.dataset_path.endswith('.csv'):
            self.dataset.save_csv(self.dataset_path)
        else:
            self.dataset.save_jsonl(self.dataset_path)
        self.last_dataset_hash = hash(self.dataset)
        
    def on_export_as_openai_dataset_triggered(self, filename):
        self.dataset.save_openai_jsonl(filename)
    
    def on_pre_open_triggered(self):
        if self.last_dataset_hash != hash(self.dataset):
            reply = QMessageBox.question(self.main_window, "Message",
                                          "You have unsaved changes. Opening a new file will discard them.",
                                          QMessageBox.Discard | QMessageBox.Cancel)
            return reply == QMessageBox.Discard
        return True
        
    def on_post_open_triggered(self, filename):
        # TODO: improve it
        if filename.endswith('.csv'):
            self.dataset = ChatDataset.from_csv(filename)
        else:
            self.dataset = ChatDataset.from_jsonl(filename)
        self.last_dataset_hash = hash(self.dataset)
        self.dataset_path = filename
        self.update_table()
        
    def on_add_chat_clicked(self):
        chat = Chat.create_empty()
        self.dataset.add_chat(chat)
        self.main_window.add_chat_item([
            chat.name, chat.language, len(chat)])
        
    def on_delete_chat_clicked(self, row_id):
        self.dataset.remove_chat(row_id)
    
    def on_copy_chat_clicked(self, row_id):
        if row_id == -1:
            return
        
        chat = self.dataset.get_chat(row_id)
        chat = deepcopy(chat)
        chat.name += ' (copy)'
        self.dataset.add_chat(chat)
        self.main_window.add_chat_item([
            chat.name, chat.language, len(chat)])
        
    def on_chat_double_clicked(self, row_id):
        chat_window = ChatWindow()
        chat_controller = ChatController(
            chat_window, self.dataset.get_chat(row_id))
        self.chat_controllers.add(chat_controller)
        
        chat_window.set_close_callback(
            partial(self.on_chat_window_close, chat_controller=chat_controller))
        chat_window.show()
    
    def on_chat_window_close(self, chat_controller):
        self.chat_controllers.remove(chat_controller)
        self.update_table()
        
    def on_settings_clicked(self):
        settings_window = SettingsWindow()
        self.settings_controller = SettingsController(settings_window)
        
        settings_window.set_close_callback(self.on_settings_window_close)
        settings_window.show()
        
    def on_settings_window_close(self):
        self.settings_controller = None
        self.update_table()
        
    def update_table(self):
        self.main_window.clear()
        for i in range(len(self.dataset)):
            chat = self.dataset.get_chat(i)
            self.main_window.add_chat_item([
                chat.name, chat.language, len(chat)])

    def close_application(self):
        if self.last_dataset_hash != hash(self.dataset):
            reply = QMessageBox.question(self.main_window, "Message",
                                          "You have unsaved changes. Closing the app will discard them.",
                                          QMessageBox.Discard | QMessageBox.Cancel)
            return reply == QMessageBox.Discard
        return True