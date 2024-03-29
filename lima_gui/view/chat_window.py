from PySide6.QtWidgets import QWidget, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt
from typing import List
from loguru import logger

from lima_gui.logging import all_methods_logger
from .ui_chat_widget import Ui_ChatWidget
from .chat_item import ChatItem
from ..model.function import Tool


@all_methods_logger
class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ChatWidget()
        self.ui.setupUi(self)
        
        self.close_callback = None
        self.msg_changed_callback = None
        self.delete_msg_callback = None
        self.name_changed_callback = None
        self.language_changed_callback = None
        self.tag_added_callback = None
        self.tag_deleted_callback = None
        self.generate_callback = None
        
        self.is_generate_allowed = False

        self.roles = []
        self.generator_role = 'assistant'
        self.functions = []
        
        self.ui.delete_msg_btn.clicked.connect(self.on_delete_msg_clicked)
        self.ui.name.textChanged.connect(self.on_name_changed)
        self.ui.language.currentIndexChanged.connect(self.on_language_changed)
        self.ui.addTagBtn.clicked.connect(self.on_tag_added)
        self.ui.deleteTagBtn.clicked.connect(self.on_tag_deleted)
        self.ui.deleteFnBtn.clicked.connect(self.on_delete_fn_clicked)
        self.ui.fnListWidget.doubleClicked.connect(self.on_fn_double_clicked)
        
        
        self.ui.listWidget.verticalScrollBar().setSingleStep(10)
        self.ui.listWidget.itemSelectionChanged.connect(self.on_item_selection_changed)
        
        self.ui.generate_btn.clicked.connect(self.on_generate_clicked)
        
    def set_token_count(self, n_tokens: int):
        self.ui.n_tokens.setText(str(n_tokens))
        
    def set_msg_count(self, msg_count: int):
        self.ui.msg_count.setText(str(msg_count))

    def set_role_options(self, roles, generator_role):
        self.roles = roles
        self.generator_role = generator_role

    def set_language_options(self, languages):
        self.ui.language.clear()
        for language in languages:
            self.ui.language.addItem(language)

    def set_tag_options(self, tags):
        self.ui.tagComboBox.clear()
        self.ui.tagComboBox.addItems(tags)

    def set_tags(self, tags):
        self.ui.tagList.clear()
        self.ui.tagList.addItems(tags)

    def set_language(self, language):
        self.ui.language.setCurrentText(language)
    
    def set_name(self, name):
        self.ui.name.setText(name)

    def add_msg(self, role, content, fn_call_data=None):
        item = QListWidgetItem(self.ui.listWidget)
        chat_item = ChatItem(item)
        chat_item.set_role_options(self.roles)
        chat_item.set_functions(self.functions)
        chat_item.set_data(role, content, fn_call_data)
        chat_item.set_content_changed_callback(self.on_item_changed)
        
        item.setSizeHint(chat_item.sizeHint())
        
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, chat_item)
        
        self.ui.listWidget.scrollToBottom()
        
    def set_functions(self, functions: List[Tool]):
        self.ui.fnListWidget.clear()
        for fn in functions:
            self.ui.fnListWidget.addItem(fn.name)
        
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            chat_item: ChatItem = self.ui.listWidget.itemWidget(item)
            chat_item.set_functions(functions)
        
        self.functions = functions

    def set_close_callback(self, callback):
        self.close_callback = callback

    def closeEvent(self, event):
        event.accept()
        self.close_callback()

    def set_add_msg_clicked_callback(self, callback):
        self.ui.add_msg_btn.clicked.connect(callback)

    def set_delete_msg_clicked_callback(self, callback):
        self.delete_msg_callback = callback
        
    def set_msg_changed_callback(self, callback):
        self.msg_changed_callback = callback
        
    def set_name_changed_callback(self, callback):
        self.name_changed_callback = callback
    
    def set_language_changed_callback(self, callback):
        self.language_changed_callback = callback
        
    def set_tag_added_callback(self, callback):
        self.tag_added_callback = callback
        
    def set_tag_deleted_callback(self, callback):
        self.tag_deleted_callback = callback
    
    def set_generate_callback(self, callback):
        self.generate_callback = callback
        
    def set_add_function_callback(self, callback):
        self.ui.addFnBtn.clicked.connect(callback)
        
    def set_delete_function_callback(self, callback):
        self.delete_function_callback = callback
    
    def set_function_double_clicked_callback(self, callback):
        self.function_double_clicked_callback = callback
        
    def on_delete_msg_clicked(self):
        row_id = self.ui.listWidget.currentRow()
        
        if self.delete_msg_callback:
            self.delete_msg_callback(row_id)
        # Remove item from view
        self.ui.listWidget.takeItem(row_id)

    def on_item_changed(self, item):
        row_id = self.ui.listWidget.row(item)
        row_item = self.ui.listWidget.item(row_id)
        
        chat_item: ChatItem = self.ui.listWidget.itemWidget(item)
        role, content, fn_call_data = chat_item.get_data()
        
        row_item.setSizeHint(chat_item.sizeHint())
        
        self.msg_changed_callback(row_id, role, content, fn_call_data)
        self.on_item_selection_changed()
        
    def on_name_changed(self, new_name):
        if self.name_changed_callback:
            self.name_changed_callback(self.ui.name.text())
        
    def on_language_changed(self, new_lang):
        if self.language_changed_callback:
            self.language_changed_callback(self.ui.language.currentText())
            
    def on_tag_added(self):
        tag = self.ui.tagComboBox.currentText()
        
        # Don't add existing tags
        is_in_list = self.ui.tagList.findItems(tag, Qt.MatchExactly)
        if is_in_list:
            return
        
        self.ui.tagList.addItem(tag)
        
        if self.tag_added_callback:
            self.tag_added_callback(tag)
    
    def on_tag_deleted(self):
        row_id = self.ui.tagList.currentRow()
        
        tag = self.ui.tagList.takeItem(row_id).text()
        
        if self.tag_deleted_callback:
            self.tag_deleted_callback(tag)
            
    def on_item_selection_changed(self):
        row_id = self.ui.listWidget.currentRow()
        
        if row_id == -1:
            return
        
        item = self.ui.listWidget.item(row_id)
        chat_item: ChatItem = self.ui.listWidget.itemWidget(item)
        role, content, fn_call_data = chat_item.get_data()
        self.ui.generate_btn.setEnabled(role == self.generator_role and self.is_generate_allowed)

    def on_generate_clicked(self):
        row_id = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(row_id)
        chat_item: ChatItem = self.ui.listWidget.itemWidget(item)
        if self.generate_callback is not None:
            self.generate_callback(row_id, chat_item)

    def on_delete_fn_clicked(self):
        ind = self.ui.fnListWidget.currentRow()
        self.ui.fnListWidget.takeItem(ind)
        
        if self.delete_function_callback:
            self.delete_function_callback(ind)

    def on_fn_double_clicked(self, item):
        ind = item.row()
        
        if self.function_double_clicked_callback:
            self.function_double_clicked_callback(ind)
