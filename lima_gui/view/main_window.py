from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QMainWindow, QTableWidgetItem, QFileDialog
from loguru import logger

from .ui_main_window import Ui_MainWindow
from .openai_window import OpenaiWindow
from lima_gui.logging import all_methods_logger


@all_methods_logger
class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.openai_window = OpenaiWindow()
        
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.ui.actionDelete_chat.triggered.connect(
            self.on_delete_chat_triggered)
        self.ui.actionCopy_chat.triggered.connect(
            self.on_copy_chat_triggered)
        self.ui.tableWidget.itemDoubleClicked.connect(
            self.on_item_double_clicked)
        self.ui.actionSaveCurrent.triggered.connect(
            self.on_save_current_triggered)
        self.ui.actionSave_to.triggered.connect(
            self.on_save_to_triggered)
        self.ui.actionOpen.triggered.connect(
            self.on_open_triggered)
        self.ui.actionOpenAI_API.triggered.connect(
            self.on_openai_api_triggered)
        self.ui.actionExport_as_OpenAI_dataset.triggered.connect(
            self.on_export_as_openai_dataset_triggered)
        self.delete_chat_callback = None
        self.chat_double_click_callback = None
        self.copy_chat_callback = None
        
        self.save_to_callback = None
        self.save_current_callback = None
        self.export_as_openai_dataset_callback = None
        self.post_open_callback = None
        self.pre_open_callback = None
        self.close_callback = None
        
    def set_column_names(self, names: list):
        self.ui.tableWidget.setColumnCount(len(names))
        self.ui.tableWidget.setHorizontalHeaderLabels(names)
        header = self.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def set_add_chat_callback(self, callback):
        self.ui.actionAdd_chat.triggered.connect(callback)
    
    def set_delete_chat_callback(self, callback):
        self.delete_chat_callback = callback
    
    def set_copy_chat_callback(self, callback):
        self.copy_chat_callback = callback
        
    def set_chat_double_clicked_callback(self, callback):
        self.chat_double_click_callback = callback
    
    def set_save_current_callback(self, callback):
        self.save_current_callback = callback
    
    def set_save_to_callback(self, callback):
        self.save_to_callback = callback
        
    def set_pre_open_callback(self, callback):
        self.pre_open_callback = callback
        
    def set_post_open_callback(self, callback):
        self.post_open_callback = callback
        
    def set_settings_callback(self, callback):
        self.ui.actionSettings.triggered.connect(callback)
    
    def set_close_even_happened_callback(self, callback):
        self.close_callback = callback
    
    def set_export_as_openai_dataset_callback(self, callback):
        self.export_as_openai_dataset_callback = callback
        
    def on_save_current_triggered(self):
        self.save_current_callback()
        
    def on_save_to_triggered(self):
        filename = QFileDialog.getSaveFileName(self, 'Save file', '', 'All Files (*)')
        if filename[0]:
            self.save_to_callback(filename[0])
            
    def on_export_as_openai_dataset_triggered(self):
        filename = QFileDialog.getSaveFileName(self, 'Save file', '', 'All Files (*)')
        if filename[0]:
            self.export_as_openai_dataset_callback(filename[0])
    
    def on_open_triggered(self):
        # Check if opening another file is allowed (e.g. current file is not saved yet)
        if not self.pre_open_callback():
            return
        
        filename = QFileDialog.getOpenFileName(self, 'Open file', '', 'All Files (*)')
        if filename[0]:
            self.post_open_callback(filename[0])
        
    def on_delete_chat_triggered(self):
        row_id = self.ui.tableWidget.currentRow()
        
        if self.delete_chat_callback:
            self.delete_chat_callback(row_id)
        # Remove item from view
        self.ui.tableWidget.removeRow(row_id)
        
    def on_copy_chat_triggered(self):
        row_id = self.ui.tableWidget.currentRow()
        
        if self.copy_chat_callback:
            self.copy_chat_callback(row_id)
        
    def on_item_double_clicked(self, item):
        row_id = self.ui.tableWidget.row(item)
        
        if self.chat_double_click_callback:
            self.chat_double_click_callback(row_id)
    
    def closeEvent(self, event):
        logger.debug('Close event.')
        if self.close_callback:
            do_close = self.close_callback()
            if not do_close:
                event.ignore()
                return
            
    def on_openai_api_triggered(self):
        self.openai_window.show()
    
    def add_chat_item(self, data: list):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        for i in range(len(data)):
            self.ui.tableWidget.setItem(
                self.ui.tableWidget.rowCount() - 1, i, QTableWidgetItem(str(data[i])))
            
    def clear(self):
        n = self.ui.tableWidget.rowCount()
        for i in range(n):
            self.ui.tableWidget.removeRow(0)


