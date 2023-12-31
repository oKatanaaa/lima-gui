from PySide6.QtWidgets import QWidget
from .ui_openai import Ui_openai


class OpenaiWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_openai()
        self.ui.setupUi(self)
        
        self.ui.apiBase_lineEdit.textChanged.connect(self.on_settings_changed)
        self.ui.apiKey_lineEdit.textChanged.connect(self.on_settings_changed)
        self.ui.modelName_lineEdit.textChanged.connect(self.on_settings_changed)
        self.ui.temperature_lineEdit.textChanged.connect(self.on_settings_changed)
        self.ui.comboBox.currentIndexChanged.connect(self.on_settings_changed)
        self.ui.completionTokens_lineEdit.textChanged.connect(self.on_settings_changed)
        
        self.ui.checkBox.stateChanged.connect(self.on_api_enabled)
        
        self.api_enabled_callback = None
        self.settings_changed_callback = None
    
    def set_api_key(self, key):
        self.ui.apiKey_lineEdit.setText(key)
    
    def set_api_types(self, types, default_type):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(types)
        self.ui.comboBox.setCurrentText(default_type)

    def set_api_enabled_callback(self, callback):
        self.api_enabled_callback = callback
        
    def set_settings_changed_callback(self, callback):
        self.settings_changed_callback = callback
    
    def set_copy_key_callback(self, callback):
        self.ui.copyKey_pushButton.clicked.connect(callback)
        
    def on_api_enabled(self, state):
        if self.api_enabled_callback:
            self.api_enabled_callback(state)
            
    def on_settings_changed(self):
        api_base = self.ui.apiBase_lineEdit.text()
        api_key = self.ui.apiKey_lineEdit.text()
        model_name = self.ui.modelName_lineEdit.text()
        temperature = float(self.ui.temperature_lineEdit.text())
        api_type = self.ui.comboBox.currentText()
        n_completion_tokens = int(self.ui.completionTokens_lineEdit.text())
        
        if self.settings_changed_callback:
            self.settings_changed_callback(
                api_base,
                api_key,
                model_name,
                temperature,
                api_type,
                n_completion_tokens
            )


        
        
        