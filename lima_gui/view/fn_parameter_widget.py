from PySide6.QtWidgets import QTextEdit, QWidget

from lima_gui.model.function import Function
from .ui_fn_parameter_widget import Ui_fnParameter



class FnParameterWidget(QWidget):
    def __init__(self, parent_item, parent=None):
        super().__init__(parent)
        self.parent_item = parent_item
        self.ui = Ui_fnParameter()
        self.ui.setupUi(self)
        self.ui.paramNameLineEdit.textChanged.connect(self.on_parameter_updated)
        self.ui.paramTypeLineEdit.textChanged.connect(self.on_parameter_updated)
        self.ui.paramDescLineEdit.textChanged.connect(self.on_parameter_updated)
        self.ui.enumAddBtn.clicked.connect(self.on_parameter_updated)
        self.ui.enumDeleteBtn.clicked.connect(self.on_parameter_updated)
        self.ui.paramRequiredCheckBox.clicked.connect(self.on_parameter_updated)
        
        self.param_updated_callback = None

    def set_data(self, data):
        self.ui.paramNameLineEdit.setText(data[Function.PARAM_NAME])
        self.ui.paramTypeLineEdit.setText(data[Function.PARAM_TYPE])
        self.ui.paramDescLineEdit.setText(data[Function.PARAM_DESCRIPTION])
        self.ui.paramRequiredCheckBox.setChecked(data[Function.PARAM_REQUIRED])
        self.ui.paramEnumListWidget.clear()
        self.ui.paramEnumListWidget.addItems(data[Function.PARAM_ENUM])
    
    def get_data(self):
        name = self.ui.paramNameLineEdit.text()
        type = self.ui.paramTypeLineEdit.text()
        desc = self.ui.paramDescLineEdit.toPlainText()
        required = self.ui.paramRequiredCheckBox.isChecked()
        enums = [self.ui.paramEnumListWidget.item(i).text() for i in range(self.ui.paramEnumListWidget.count())]
        return {
            Function.PARAM_NAME: name,
            Function.PARAM_TYPE: type,
            Function.PARAM_DESCRIPTION: desc,
            Function.PARAM_REQUIRED: required,
            Function.PARAM_ENUM: enums
        }
    
    def set_param_updated_callback(self, callback):
        self.param_updated_callback = callback
    
    def on_parameter_updated(self):
        if self.param_updated_callback:
            self.param_updated_callback(self.parent_item)
    