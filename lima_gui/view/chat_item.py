from PySide6.QtGui import QKeyEvent, QTextCursor
from PySide6.QtWidgets import QTextEdit, QWidget, QDialog
from PySide6.QtCore import Qt
from typing import List
from loguru import logger

from .ui_chat_item import Ui_ChatItem
from .function_call_window import FunctionCallWindow
from ..model.function import Function
from lima_gui.logging import all_methods_logger


@all_methods_logger
class ChatItem(QWidget):
    def __init__(self, parent_item, parent=None):
        super().__init__(parent)
        self.parent_item = parent_item
        self.ui = Ui_ChatItem()
        self.ui.setupUi(self)
        
        # Add an attribute to keep track of auto-indentation
        self.auto_indent_next_line = True
        self.ui.textEdit.keyPressEvent = self.handleKeyPressEvent
        
        self.function_call_data = {"name": None, "arguments": None}
        self.functions = dict()
        
        # Initialize fn combo box to default value
        self.ui.fnNameComboBox.addItem('none')
        self.ui.fnNameComboBox.setCurrentIndex(0)
        
        # TODO: move somewhere outside
        self.role2color = {
            'system': '#f4ebff',
            'user': '#ebf2ff',
            'assistant': '#ebfff6',
            'function': '#ffe9eb'
        }
        
        self.ui.textEdit.document().contentsChanged.connect(self.on_content_changed)
        self.ui.textEdit.setAcceptRichText(False)
        self.content_changed_callback = None
        
        self.ui.textEdit.document().documentLayout().documentSizeChanged.connect(self.update_height)
        # Ignore wheel event
        self.ui.comboBox.wheelEvent = lambda x: ()
        self.ui.comboBox.currentIndexChanged.connect(self.on_content_changed)
        self.ui.fnNameComboBox.wheelEvent = lambda x: ()
        self.ui.fnNameComboBox.currentIndexChanged.connect(self.on_content_changed)
        self.ui.fnCallParamsPushButton.clicked.connect(self.on_fn_call_clicked)
        
    # TextEdit modified keyPressEvent
    # Keeps tabulation on the same level as the previous line
    def handleKeyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Tab:
            # Insert four spaces
            self.ui.textEdit.insertPlainText('    ')
            return  # Consume the event to prevent default behavior
    
        if event.key() == Qt.Key_Return:
            # Fetch the current line's indentation
            cursor = self.ui.textEdit.textCursor()
            cursor.movePosition(QTextCursor.StartOfBlock, QTextCursor.KeepAnchor)  # Adjusted for PySide6
            leading_spaces = len(cursor.selectedText()) - len(cursor.selectedText().lstrip())
            
            # Enter and apply auto-indentation only if required
            QTextEdit.keyPressEvent(self.ui.textEdit, event)
            if self.auto_indent_next_line:
                self.ui.textEdit.insertPlainText(' ' * leading_spaces)
            else:
                # Reset flag for next time
                self.auto_indent_next_line = True
            return

        # Detect backspaces at the start of a line (to disable auto-indentation on the next line)
        if event.key() == Qt.Key.Key_Backspace:
            cursor = self.ui.textEdit.textCursor()
            cursor.movePosition(QTextCursor.StartOfBlock, QTextCursor.KeepAnchor)  # Adjusted for PySide6
            if not cursor.selectedText().strip():
                self.auto_indent_next_line = False

        # Default handler
        QTextEdit.keyPressEvent(self.ui.textEdit, event)

    def get_cursor_context(self):
        cursor = self.ui.textEdit.textCursor()

        # Get the current position of the cursor
        cursor_position = cursor.position()

        # Get the text of the entire QTextEdit
        full_text = self.ui.textEdit.toPlainText()
        text_before_cursor = full_text[:cursor_position]
        text_after_cursor = full_text[cursor_position:]

        return text_before_cursor, text_after_cursor
    
    def set_content_changed_callback(self, callback):
        self.content_changed_callback = callback
    
    def set_role_options(self, roles):
        self.ui.comboBox.clear()
        for role in roles:
            self.ui.comboBox.addItem(role)
        self.ui.comboBox.setCurrentIndex(0)
            
    def set_functions(self, functions: List[Function], no_callback=True):
        if no_callback:
            self.ui.fnNameComboBox.currentIndexChanged.disconnect()
        
        current_fn = self.ui.fnNameComboBox.currentText()
        self.ui.fnNameComboBox.clear()
        self.ui.fnNameComboBox.addItem('none')
        for fn in functions:
            self.ui.fnNameComboBox.addItem(fn.name)
        
        self.functions = dict([(fn.name, fn) for fn in functions])
        if current_fn in self.functions:
            self.ui.fnNameComboBox.setCurrentText(current_fn)
        else:
            self.ui.fnNameComboBox.setCurrentIndex(0)
        
        self.update_fn_ui_elements()
        
        self.ui.fnNameComboBox.currentIndexChanged.connect(self.on_content_changed)
    
    def set_data(self, role, content, function_call_data=None, no_callback=True):
        self.ui.comboBox.currentIndexChanged.disconnect()
        self.ui.textEdit.document().contentsChanged.disconnect()
        self.ui.textEdit.document().documentLayout().documentSizeChanged.disconnect()
        self.ui.fnNameComboBox.currentIndexChanged.disconnect()
            
        self.ui.comboBox.setCurrentText(role)
        self.ui.textEdit.setPlainText(content)
        
        self.set_function_call_data(function_call_data)
        
        if no_callback:
            self.update_height()
            
        if not no_callback:
            self.on_content_changed()
        
        # Enable callbacks
        self.ui.comboBox.currentIndexChanged.connect(self.on_content_changed)
        self.ui.textEdit.document().contentsChanged.connect(self.on_content_changed)
        self.ui.textEdit.document().documentLayout().documentSizeChanged.connect(self.on_content_changed)
        self.ui.fnNameComboBox.currentIndexChanged.connect(self.on_content_changed)
    
    def set_function_call_data(self, function_call_data):
        if function_call_data is None:
            function_call_data = {"name": None, "arguments": None}
            
        if function_call_data['name'] is not None:
            self.ui.fnNameComboBox.setCurrentText(function_call_data['name'])
        else:
            self.ui.fnNameComboBox.setCurrentIndex(0)
        self.function_call_data = function_call_data
    
    def get_data(self):
        # Role, content
        return self.ui.comboBox.currentText(), self.ui.textEdit.toPlainText(), self.function_call_data
    
    def on_content_changed(self, *args):
        current_fn = self.ui.fnNameComboBox.currentText()
        self.function_call_data["name"] = current_fn if current_fn != 'none' else None
        self.update_height()
        self.update_background_color_by_role()
        self.update_fn_ui_elements()
        if self.content_changed_callback:
            # Parent item that's contained in QListWidget is passed
            # as the callback is a ChatWindow's method and it must know which list item got changed
            self.content_changed_callback(self.parent_item)
            
    def on_fn_call_clicked(self):
        fn_name = self.ui.fnNameComboBox.currentText()
        fn = self.functions[fn_name]
        
        fn_call_window = FunctionCallWindow(fn.params)
        if self.function_call_data is not None:
            fn_call_window.set_data(self.function_call_data["arguments"])
        result = fn_call_window.exec()
        
        if result == QDialog.Accepted:
            params = fn_call_window.get_data()
            self.function_call_data["arguments"] = params if len(params) > 0 else None
            self.on_content_changed()

    def update_height(self):
        size = self.ui.textEdit.document().size().toSize()
        self.ui.textEdit.setFixedHeight(size.height() + 5)
        self.setFixedHeight(size.height() + 20 + 50)
        logger.debug(f"ChatItem updated height: {size.height()}")

    def sizeHint(self):
        print(super().sizeHint())
        return super().sizeHint()

    def update_background_color_by_role(self):
        role = self.ui.comboBox.currentText()
        if role not in self.role2color:
            return
        self.ui.widget.setStyleSheet(f'background-color: {self.role2color[role]};')
        
    def update_fn_ui_elements(self):
        def config_ui(enable_combo, enable_fn_btn):
            self.ui.fnNameComboBox.setEnabled(enable_combo)
            self.ui.fnCallParamsPushButton.setEnabled(enable_fn_btn)
        role = self.ui.comboBox.currentText()
        
        if role == 'function':
            config_ui(True, False)
        elif role == 'system':
            config_ui(False, False)
        elif role == 'assistant':
            config_ui(True, self.ui.fnNameComboBox.currentText() != 'none')
        elif role == 'user':
            config_ui(False, False)
        else:
            logger.error(f"Unknown role {role} is set. It may cause errors when using OpenAI API.")
