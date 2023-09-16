import json
import pathlib
from typing import List

from ..schema import Example
from .developer import Developer

# 使用不同的配置路径来区分不同的角色。
config_path = pathlib.Path(__file__).parent / ".autom" / "api_documentation_architect.json"

with open(config_path, "r") as f:
    config_data: dict = json.load(f)


class APIDocumentationArchitect(Developer):
    @property
    def model(self) -> str:
        return config_data["model"]

    @property
    def role(self) -> str:
        return config_data["title"]

    @property
    def job_description(self) -> str:
        return config_data["job-description"]

    @property
    def format_requirements(self) -> List[str]:
        requirements = config_data.get("extra-format-requirements", None)
        if requirements is None:
            requirements = []
        parent_format_requirements = super().format_requirements
        return parent_format_requirements + requirements

    @property
    def guidance_requirements(self) -> List[str]:
        requirements = config_data.get("extra-guidance-requirements", None)
        if requirements is None:
            requirements = []
        parent_guidance_requirements = super().guidance_requirements
        return parent_guidance_requirements + requirements

    @property
    def examples(self) -> List[Example]:
        example_dict_list = config_data.get("examples", None)
        if example_dict_list is None:
            return []
        return [Example(example_data["query"], example_data["response"]) for example_data in config_data["examples"]]


__all__ = ['APIDocumentationArchitect']
