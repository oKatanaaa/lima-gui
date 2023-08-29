from PySide6.QtWidgets import QWidget
from .ui_chat_item import Ui_ChatItem


class ChatItem(QWidget):
    def __init__(self, parent_item, parent=None):
        super().__init__(parent)
        self.parent_item = parent_item
        self.ui = Ui_ChatItem()
        self.ui.setupUi(self)
        
        self.ui.textEdit.document().contentsChanged.connect(self.on_content_changed)
        self.content_changed_callback = None
    
    def set_content_changed_callback(self, callback):
        self.content_changed_callback = callback
    
    def set_role_options(self, roles):
        self.ui.comboBox.clear()
        for role in roles:
            self.ui.comboBox.addItem(role)
    
    def set_data(self, role, content):
        self.ui.comboBox.setCurrentText(role)
        self.ui.textEdit.setText(content)
    
    def get_data(self):
        # Role, content
        return self.ui.comboBox.currentText(), self.ui.textEdit.toPlainText()
    
    def on_content_changed(self):
        print('content changed')
        if self.content_changed_callback:
            self.content_changed_callback(self.parent_item)

