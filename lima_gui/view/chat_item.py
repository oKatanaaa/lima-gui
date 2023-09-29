from PySide6.QtGui import QKeyEvent, QTextCursor
from PySide6.QtWidgets import QTextEdit, QWidget
from PySide6.QtCore import Qt
from .ui_chat_item import Ui_ChatItem

class ChatItem(QWidget):
    def __init__(self, parent_item, parent=None):
        super().__init__(parent)
        self.parent_item = parent_item
        self.ui = Ui_ChatItem()
        self.ui.setupUi(self)
        
        self.ui.textEdit.document().contentsChanged.connect(self.on_content_changed)
        self.ui.textEdit.setAcceptRichText(False)
        self.content_changed_callback = None
        
        self.ui.textEdit.document().documentLayout().documentSizeChanged.connect(self.on_content_changed)
        # Ignore wheel event
        self.ui.comboBox.wheelEvent = lambda x: ()
        self.ui.comboBox.currentIndexChanged.connect(self.on_content_changed)
        
        # TODO: move somewhere outside
        self.role2color = {
            'system': '#f4ebff',
            'user': '#ebf2ff',
            'assistant': '#ebfff6',
        }
        # Add an attribute to keep track of auto-indentation
        self.auto_indent_next_line = True
        self.ui.textEdit.keyPressEvent = self.handleKeyPressEvent

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

    
    def set_content_changed_callback(self, callback):
        self.content_changed_callback = callback
    
    def set_role_options(self, roles):
        self.ui.comboBox.clear()
        for role in roles:
            self.ui.comboBox.addItem(role)
    
    def set_data(self, role, content):
        self.ui.comboBox.setCurrentText(role)
        self.ui.textEdit.setPlainText(content)
        self.update_height()
    
    def get_data(self):
        # Role, content
        return self.ui.comboBox.currentText(), self.ui.textEdit.toPlainText()
    
    def on_content_changed(self):
        print('content changed')
        self.update_height()
        self.update_background_color_by_role()
        if self.content_changed_callback:
            self.content_changed_callback(self.parent_item)

    def update_height(self):
        size = self.ui.textEdit.document().size().toSize()
        self.ui.textEdit.setFixedHeight(size.height() + 5)
        self.setFixedHeight(size.height() + 20 + 50)
        print('New height', size.height() + 20 + 50)

    def sizeHint(self):
        print(super().sizeHint())
        return super().sizeHint()

    def update_background_color_by_role(self):
        role = self.ui.comboBox.currentText()
        self.ui.widget.setStyleSheet(f'background-color: {self.role2color[role]};')
