from lima_gui.view.function_desc_window import FunctionDescriptionWindow
from lima_gui.model.function import Function


class FunctionDescController:
    def __init__(
        self, function_desc_window: FunctionDescriptionWindow, function: Function
    ):
        self.function_desc_window = function_desc_window
        self.function = function
        
        self.function_desc_window.set_name(function.name)
        self.function_desc_window.set_description(function.description)
        for param in self.function.params:
            self.function_desc_window.add_param(param)
        
        self.function_desc_window.set_name_changed_callback(self.on_name_changed)
        self.function_desc_window.set_description_changed_callback(self.on_description_changed)
        self.function_desc_window.set_save_function_callback(self.on_save_function_clicked)
        #self.function_desc_window.set_close_callback(self.on_save_function_clicked)
        self.function_desc_window.set_add_param_clicked_callback(self.on_add_param_clicked)
        self.function_desc_window.set_delete_param_clicked_callback(self.on_delete_param_clicked)
        self.function_desc_window.set_param_updated_callback(self.on_param_updated)
        
        self.save_function_callback = None
    
    def on_name_changed(self, name):
        self.function.name = name
        
    def on_description_changed(self, description):
        self.function.description = description
    
    def on_save_function_clicked(self):
        if self.save_function_callback:
            self.save_function_callback(self.function)
            
    def on_param_updated(self, ind, data):
        print('param updated', ind, data)
        self.function.edit_param(ind, data)
            
    def on_add_param_clicked(self):
        print('add param clicked')
        self.function_desc_window.add_param(Function.create_empty_param())
        self.function.add_param(Function.create_empty_param())
    
    def on_delete_param_clicked(self, ind):
        self.function.remove_param(ind)
