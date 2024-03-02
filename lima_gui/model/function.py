from typing import Dict, List
from copy import deepcopy
from loguru import logger

from lima_gui.logging import all_methods_logger

"""
Why do dynamic data update within OAI structure?
TODO: Remove this shit and do conversion to OAI only when adding the tool to a chat.
"""
@all_methods_logger
class Tool:
    """
    See https://platform.openai.com/docs/guides/gpt/function-calling for more details.
    
    Schema:
    {
        "type": "function",
        "function": {
            "name": "my_function",
            "description": "My function",
            "parameters": {
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "First parameter"
                    },
                    "param2": {
                        "type": "string",
                        "enum": ["value1", "value2"]
                    }
                },
                "required": ["param1"]
            }
        }
    }
    
    This class encapsulates tool data stored with OpenAI schema. 
    But all the interactions with the data are done via a separate data schema
    more suitable for the context of this software.
    """
    
    # Parameter fields
    PARAM_NAME = "name"
    PARAM_DESCRIPTION = "description"
    PARAM_TYPE = "type"
    PARAM_REQUIRED = "required"
    PARAM_ENUM = "enum"
    
    
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
        return Tool({
            "type": "function",
            "function": {
                "name": name,
                "description": "",
                "parameters": {
                    "type": "object",
                    "properties": dict(),
                    "required": []
                }
            }
        })
        
    @staticmethod
    def create_empty_param():
        return {
            Tool.PARAM_NAME: '',
            Tool.PARAM_TYPE: 'string',
            Tool.PARAM_DESCRIPTION: '',
            Tool.PARAM_REQUIRED: False,
            Tool.PARAM_ENUM: []
        }

    @staticmethod
    def assert_param_schema(param_dict: Dict[str, str]):
        assert Tool.PARAM_NAME in param_dict
        assert Tool.PARAM_DESCRIPTION in param_dict
        assert Tool.PARAM_TYPE in param_dict
        assert Tool.PARAM_REQUIRED in param_dict
        assert Tool.PARAM_ENUM in param_dict
        assert isinstance(param_dict[Tool.PARAM_REQUIRED], bool)
        
    def __init__(self, fn_dict: dict):
        assert isinstance(fn_dict, dict)
        self._main_dict = fn_dict
        self._fn_dict = fn_dict['function']
        self._param_names = list(self._fn_dict["parameters"]["properties"].keys())
    
    @property
    def name(self):
        return self._fn_dict["name"]
    
    @name.setter
    def name(self, name):
        self._fn_dict["name"] = name
        
    @property
    def description(self):
        return self._fn_dict["description"]
    
    @description.setter
    def description(self, description):
        self._fn_dict["description"] = description
        
    @property
    def lima_compatible_params(self) -> List[Dict[str, any]]:
        params = []
        for name, data in self._fn_dict["parameters"]["properties"].items():
            param = {
                Tool.PARAM_NAME: name,
                Tool.PARAM_TYPE: data["type"],
                Tool.PARAM_DESCRIPTION: data["description"],
                Tool.PARAM_REQUIRED: name in self._fn_dict["parameters"]["required"],
                Tool.PARAM_ENUM: data["enum"]
            }
            params.append(param)
        return params
    
    @property
    def _parameters(self) -> Dict[str, any]:
        return self._fn_dict["parameters"]["properties"]
    
    def add_param(self, param_dict: Dict[str, str]):
        Tool.assert_param_schema(param_dict)
        param_name = param_dict[Tool.PARAM_NAME]
        assert param_name not in self._parameters.keys(), \
            f'Parameter {param_name} is already exists for tool={self.name}.'
            
        oai_param_dict = {
            param_dict[Tool.PARAM_NAME]: {
                Tool.PARAM_TYPE: param_dict[Tool.PARAM_TYPE],
                Tool.PARAM_DESCRIPTION: param_dict[Tool.PARAM_DESCRIPTION],
                Tool.PARAM_ENUM: param_dict[Tool.PARAM_ENUM]
            }
        }
        
        self._parameters.update(oai_param_dict)
        self._param_names.append(param_name)
        if param_dict[Tool.PARAM_REQUIRED]:
            self._add_required_parameter(param_name)
    
    def edit_param(self, ind: int, param_dict: Dict[str, str]):
        Tool.assert_param_schema(param_dict)
        assert ind < len(self._param_names), \
            f'Tried to edit unknown parameter {param_dict} for tool={self.name}.'
        param_name = self._param_names[ind]
        oai_param_dict = {
            param_dict[Tool.PARAM_NAME]: {
                Tool.PARAM_TYPE: param_dict[Tool.PARAM_TYPE],
                Tool.PARAM_DESCRIPTION: param_dict[Tool.PARAM_DESCRIPTION],
                Tool.PARAM_ENUM: param_dict[Tool.PARAM_ENUM]
            }
        }
        
        # Remove param data for old name
        self._parameters.pop(param_name)
        # Add param data with new name
        self._parameters.update(oai_param_dict)
        # Update param name list with the new name
        self._param_names[ind] = param_dict[Tool.PARAM_NAME]
        if param_dict[Tool.PARAM_REQUIRED]:
            self._remove_required_parameter(param_name)
            self._add_required_parameter(param_dict[Tool.PARAM_NAME])
        else:
            self._remove_required_parameter(param_name)
        
    def _add_required_parameter(self, param_name: str):
        if param_name in self._fn_dict["parameters"]["required"]:
            logger.warning(
                f'Parameter {param_name} is already in the required parameters list. This call will do nothing.' \
                f'Tool name = {self.name}'
            )
            return
        
        self._fn_dict["parameters"]["required"].append(param_name)
    
    def _remove_required_parameter(self, param_name: str):
        if param_name not in self._fn_dict["parameters"]["required"]:
            logger.warning(
                f'Tried to remove parameter {param_name} which is not in the required parameters list. This call will do nothing.' \
                f'Tool name = {self.name}'
            )
            return

        self._fn_dict["parameters"]["required"].remove(param_name)
        
    def remove_param(self, param_name):
        assert param_name in self._fn_dict["parameters"].keys(), \
            f'Tried to remove unknown parameter {param_name} from the parameters list.' \
            f'Tool name = {self.name}, current parameters list = {self._fn_dict["parameters"].keys()}'
            
        self._parameters.pop(param_name)
        self._param_names.remove(param_name)
        
        if param_name in self._fn_dict["parameters"]["required"]:
            self._remove_required_parameter(param_name)
    
    def to_openai_dict(self):
        return deepcopy(self._main_dict)
    
    def __str__(self) -> str:
        return str(self.to_openai_dict())

    def __repr__(self) -> str:
        return str(self.to_openai_dict())
    
    def __hash__(self):
        return hash(str(self))
