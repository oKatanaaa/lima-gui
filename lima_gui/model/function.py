from typing import Dict, List
from copy import deepcopy


class Function:
    """
    See https://platform.openai.com/docs/guides/gpt/function-calling for more details.
    """
    @staticmethod
    def create_empty(name):
        """
        Parameters
        ----------
        name : str
            Name of the function. Must be unique.

        Returns
        -------
        function : Function
            An emplty function with the given name.
        """
        return Function({
            "name": name,
            "description": "Describe your function here",
            "params": []
        })
        
    def __init__(self, fn_dict):
        self.fn_dict = fn_dict
    
    @property
    def name(self):
        return self.fn_dict["name"]
    
    @name.setter
    def name(self, name):
        self.fn_dict["name"] = name
        
    @property
    def description(self):
        return self.fn_dict["description"]
    
    @description.setter
    def description(self, description):
        self.fn_dict["description"] = description
        
    @property
    def params(self) -> List[Dict[str, str]]:
        return deepcopy(self.fn_dict["params"])
    
    def add_param(self, param_dict: Dict[str, str]):
        self.fn_dict["params"].append(param_dict)
    
    def edit_param(self, ind: int, param_dict: Dict[str, str]):
        self.fn_dict["params"][ind] = param_dict
        
    def remove_param(self, ind: int):
        self.fn_dict["params"].pop(ind)
    
    def to_openai_dict(self):
        out_dict = {
            "name": self.name,
            "description": self.description,
            "parameters": { "type": "object" }
        }
        parameters = dict()
        required_params = []
        for param in self.params:
            param_dict = dict()
            param_dict["type"] = param["type"]
            
            if "description" in param:
                param_dict["description"] = param["description"]
                
            if "enum" in param:
                param_dict["enum"] = param["enum"]
                
            parameters[param["name"]] = param_dict
            
            if param["required"]:
                required_params.append(param["name"])
        
        out_dict["parameters"]["properties"] = parameters
        out_dict["required"] = required_params
        return out_dict
    
    def __str__(self) -> str:
        return str(self.to_openai_dict())

    def __repr__(self) -> str:
        return str(self.to_openai_dict())
