from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QScrollArea, QDialog, QPushButton
from PySide6.QtCore import Qt
from .parameter_item import ParameterItem
from ..model.function import Tool


class FunctionCallWindow(QDialog):
    def __init__(self, parameter_metadata, parent=None):
        super(FunctionCallWindow, self).__init__(parent)

        # Optionally set the window title
        self.setWindowTitle("Enter Function Parameters")

        # Create a layout
        layout = QVBoxLayout()

        # Create a scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)

        # Create a scroll widget
        scroll_widget = QWidget()
        scroll.setWidget(scroll_widget)

        # Create a layout for scroll_widget
        scroll_layout = QVBoxLayout()

        # Dictionary to hold ParameterItem instances by name
        self.parameter_items = {}

        # Create and populate ParameterItem instances
        for param in parameter_metadata:
            name = param['name']
            description = param.get('description', '')  # Optional
            type_ = param['type']
            required = param['required']
            enum = param.get('enum', None)  # Optional

            parameter_item = ParameterItem(name, type_, required, enum=enum, parent=self)
            parameter_item.setToolTip(description)
            scroll_layout.addWidget(parameter_item)

            # Store ParameterItem instance
            self.parameter_items[name] = parameter_item

        # Set the layout for scroll_widget
        scroll_widget.setLayout(scroll_layout)
        
        # Add an "OK" button and connect its clicked signal to the accept slot
        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        # Set the layout for the dialog
        self.setLayout(layout)

    def set_data(self, values):
        if values is None:
            return
        
        for name, value in values.items():
            if name in self.parameter_items:
                self.parameter_items[name].ui.valueTextEdit.setText(value)

    def get_data(self):
        values = {}
        for name, parameter_item in self.parameter_items.items():
            value = parameter_item.get_data()
            values[name] = value if value != '' else None
        return values
