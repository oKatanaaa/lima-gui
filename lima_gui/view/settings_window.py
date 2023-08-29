from PySide6.QtWidgets import QWidget, QFileDialog
from .ui_settings import Ui_Settings


class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        
        self.set_tokenizer_callback = None
        self.ui.setTokBtn.clicked.connect(self.on_set_tokenizer_clicked)
        
        self.load_config_callback = None
        self.ui.loadButton.clicked.connect(self.on_load_config_clicked)
        
        self.close_callback = None
        
    def set_tokenizer_name(self, name):
        self.ui.tokenizerName.setText(name)
    
    def set_tags(self, tags):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(tags)
        
    def set_set_tokenizer_callback(self, callback):
        self.set_tokenizer_callback = callback
    
    def set_load_config_callback(self, callback):
        self.load_config_callback = callback
        
    def on_load_config_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '', 'JSON (*.json)')
        if filename[0]:
            self.load_config_callback(filename[0])
        
    def on_set_tokenizer_clicked(self):
        if self.set_tokenizer_callback:
            self.set_tokenizer_callback(self.ui.tokenizerName.text())
    
    def set_close_callback(self, callback):
        self.close_callback = callback

    def closeEvent(self, event):
        event.accept()
        self.close_callback()