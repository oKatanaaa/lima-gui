from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtCore import Qt
from .ui_function_description import Ui_FunctionDescription
from .fn_parameter_widget import FnParameterWidget


class FunctionDescriptionWindow(QWidget):
    def __init__(self, parent=None):
        super(FunctionDescriptionWindow, self).__init__(parent)
        self.ui = Ui_FunctionDescription()
        self.ui.setupUi(self)
        
        self.ui.fnNameTextEdit.textChanged.connect(self.on_name_changed)
        self.ui.fnDescriptionTextEdit.textChanged.connect(self.on_description_changed)
        
        self.name_changed_callback = None
        self.description_changed_callback = None
        self.param_updated_callback = None
        
    def set_name(self, name):
        self.ui.fnNameTextEdit.setText(name)
        
    def set_description(self, description):
        self.ui.fnDescriptionTextEdit.setText(description)
        
    def add_param(self, param_data):
        item = QListWidgetItem(self.ui.parametersListWidget)
        
        param_item = FnParameterWidget(item)
        param_item.set_data(param_data)
        param_item.set_param_updated_callback(self.on_param_updated)
        
        item.setSizeHint(param_item.sizeHint())
        
        self.ui.parametersListWidget.addItem(item)
        self.ui.parametersListWidget.setItemWidget(item, param_item)
        
        self.ui.parametersListWidget.scrollToBottom()
    
    def set_save_function_callback(self, callback):
        self.ui.fnSaveBtn.clicked.connect(callback)
        
    def set_name_changed_callback(self, callback):
        self.name_changed_callback = callback
    
    def set_description_changed_callback(self, callback):
        self.description_changed_callback = callback
    
    def set_add_param_clicked_callback(self, callback):
        self.ui.addParamBtn.clicked.connect(callback)
    
    def set_delete_param_clicked_callback(self, callback):
        self.ui.deleteParamBtn.clicked.connect(callback)
        
    def set_param_updated_callback(self, callback):
        self.param_updated_callback = callback
        
    def on_name_changed(self):
        if self.name_changed_callback:
            self.name_changed_callback(self.ui.fnNameTextEdit.text())

    def on_description_changed(self):
        if self.description_changed_callback:
            self.description_changed_callback(self.ui.fnDescriptionTextEdit.toPlainText())
    
    def on_param_updated(self, item):
        row_id = self.ui.parametersListWidget.row(item)
        row_item = self.ui.parametersListWidget.item(row_id)
        
        param_item: FnParameterWidget = self.ui.parametersListWidget.itemWidget(item)
        param_data = param_item.get_data()
        
        row_item.setSizeHint(param_item.sizeHint())
        
        self.param_updated_callback(row_id, param_data)
