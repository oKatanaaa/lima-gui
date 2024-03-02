from lima_gui.logging import all_methods_logger
from lima_gui.view.function_desc_window import ToolDescriptionWindow
from lima_gui.model.function import Tool


@all_methods_logger
class ToolDescController:
    def __init__(
        self, tool_desc_window: ToolDescriptionWindow, tool: Tool
    ):
        self.tool_desc_window = tool_desc_window
        self.tool = tool
        self.last_tool_hash = hash(tool)
        
        self.tool_desc_window.set_name(tool.name)
        self.tool_desc_window.set_description(tool.description)
        for param in self.tool.lima_compatible_params:
            self.tool_desc_window.add_param(param)
        
        self.tool_desc_window.set_name_changed_callback(self.on_name_changed)
        self.tool_desc_window.set_description_changed_callback(self.on_description_changed)
        self.tool_desc_window.set_save_function_callback(self.on_save_function_clicked)
        self.tool_desc_window.set_close_window_callback(self.on_save_function_clicked)
        self.tool_desc_window.set_add_param_clicked_callback(self.on_add_param_clicked)
        self.tool_desc_window.set_delete_param_clicked_callback(self.on_delete_param_clicked)
        self.tool_desc_window.set_param_updated_callback(self.on_param_updated)
        
        self.save_tool_callback = None
    
    def on_name_changed(self, name):
        self.tool.name = name
        
    def on_description_changed(self, description):
        self.tool.description = description
    
    def on_save_function_clicked(self):
        if self.save_tool_callback:
            self.save_tool_callback(self.tool)
            
    def on_param_updated(self, ind, data):
        self.tool.edit_param(ind, data)
            
    def on_add_param_clicked(self):
        self.tool_desc_window.add_param(Tool.create_empty_param())
        self.tool.add_param(Tool.create_empty_param())
    
    def on_delete_param_clicked(self, ind, data):
        param_name = data[Tool.name]
        self.tool.remove_param(param_name)

