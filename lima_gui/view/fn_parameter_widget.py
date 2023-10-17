from PySide6.QtWidgets import QTextEdit, QWidget
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

from lima_gui.model.function import Function
from .ui_fn_parameter_widget import Ui_fnParameter


class EnumPopup(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Enum name")
        self.setGeometry(100, 100, 300, 100)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter enum name")

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.on_ok_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)
        
        self.enum_name = None

    def on_ok_button_clicked(self):
        input_text = self.line_edit.text()
        self.enum_name = input_text
        
        print(f"Entered text: {input_text}")
        self.accept()  # This closes the QDialog with an accepted result


class FnParameterWidget(QWidget):
    def __init__(self, parent_item, parent=None):
        super().__init__(parent)
        self.parent_item = parent_item
        self.ui = Ui_fnParameter()
        self.ui.setupUi(self)
        self.ui.paramNameLineEdit.textChanged.connect(self.on_parameter_updated)
        self.ui.paramTypeLineEdit.textChanged.connect(self.on_parameter_updated)
        self.ui.paramDescLineEdit.textChanged.connect(self.on_parameter_updated)
        self.ui.enumAddBtn.clicked.connect(self.on_enum_add_clicked)
        self.ui.enumDeleteBtn.clicked.connect(self.on_enum_delete_clicked)
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
            
    def on_enum_add_clicked(self):
        popup = EnumPopup()
        result = popup.exec()
        
        if result == QDialog.Accepted:
            if len(popup.enum_name) > 0:
                print(f"Enum name: {popup.enum_name}")
                self.ui.paramEnumListWidget.addItem(popup.enum_name)
                self.on_parameter_updated()
    
    def on_enum_delete_clicked(self):
        row_id = self.ui.paramEnumListWidget.currentRow()
        self.ui.paramEnumListWidget.takeItem(row_id)
        self.on_parameter_updated()

