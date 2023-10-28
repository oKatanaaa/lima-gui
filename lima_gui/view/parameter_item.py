from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from .ui_param_item import Ui_ParamItem


class ParameterItem(QWidget):
    def __init__(self, name, type_, required, value=None, enum=None, parent=None):
        super(ParameterItem, self).__init__(parent)
        self.ui = Ui_ParamItem()
        self.ui.setupUi(self)

        # Initialize UI components
        self.ui.paramNameLabel.setText(name)
        self.ui.paramTypeLabel.setText(type_)
        self.ui.requiredCheckBox.setChecked(required)
        if value is not None:
            self.ui.valueTextEdit.setText(value)
        
        # Save enum in a field
        self.enum = enum

        # Connect textEdit value changed signal to a validation slot
        self.ui.valueTextEdit.textChanged.connect(self.validate)

    def get_data(self):
        return self.ui.valueTextEdit.toPlainText()

    def validate(self):
        text = self.get_data()
        reddish = '#FFCCCC'  # The reddish color for the textEdit background

        # Check if required but empty
        if self.ui.requiredCheckBox.isChecked() and not text:
            self.ui.valueTextEdit.setStyleSheet(f'background-color: {reddish}')
            return

        # Check if enum and value not in enum
        if self.enum and text not in self.enum:
            self.ui.valueTextEdit.setStyleSheet(f'background-color: {reddish}')
            return

        # Check if type is int or float but format is bad
        type_ = self.ui.paramTypeLabel.text()
        if type_ == 'int':
            try:
                int(text)
            except ValueError:
                self.ui.valueTextEdit.setStyleSheet(f'background-color: {reddish}')
                return
        elif type_ == 'float':
            try:
                float(text)
            except ValueError:
                self.ui.valueTextEdit.setStyleSheet(f'background-color: {reddish}')
                return

        # If everything is okay, reset background
        self.ui.valueTextEdit.setStyleSheet('background-color: none')
