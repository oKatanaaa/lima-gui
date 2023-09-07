from PySide6.QtWidgets import QWidget, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt
from .ui_chat_widget import Ui_ChatWidget
from .chat_item import ChatItem


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
        self.roles = []
        
        self.ui.delete_msg_btn.clicked.connect(self.on_delete_msg_clicked)
        self.ui.name.textChanged.connect(self.on_name_changed)
        self.ui.language.currentIndexChanged.connect(self.on_language_changed)
        self.ui.addTagBtn.clicked.connect(self.on_tag_added)
        self.ui.deleteTagBtn.clicked.connect(self.on_tag_deleted)
        
        self.ui.listWidget.verticalScrollBar().setSingleStep(10)
    
    def set_token_count(self, n_tokens: int):
        self.ui.n_tokens.setText(str(n_tokens))
        
    def set_msg_count(self, msg_count: int):
        self.ui.msg_count.setText(str(msg_count))

    def set_role_options(self, roles):
        self.roles = roles

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

    def add_msg(self, role, content):
        item = QListWidgetItem(self.ui.listWidget)
        print('added message', role, content)
        chat_item = ChatItem(item)
        chat_item.set_role_options(self.roles)
        chat_item.set_data(role, content)
        chat_item.set_content_changed_callback(self.on_item_changed)
        
        item.setSizeHint(chat_item.sizeHint())
        
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, chat_item)
        
        self.ui.listWidget.scrollToBottom()

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
        role, content = chat_item.get_data()
        
        row_item.setSizeHint(chat_item.sizeHint())
        
        self.msg_changed_callback(row_id, role, content)
        
    def on_name_changed(self):
        if self.name_changed_callback:
            self.name_changed_callback(self.ui.name.text())
        
    def on_language_changed(self):
        if self.language_changed_callback:
            self.language_changed_callback(self.ui.language.currentText())
            
    def on_tag_added(self):
        print('window. on tag added')
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
