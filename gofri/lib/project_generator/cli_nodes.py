from clinodes.nodes import ArgNode
from gofri.lib.project_generator.shortcuts import generate_controller

from gofri.lib.project_generator.module_generator import generate_module2

data = {}

class ModuleGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = True
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        inner_path = args_remained[1]
        generate_module2(
            root_package_path=data["root"],
            module_package=inner_path,
            name=name
        )

class ControllerGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = False
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        inner_path = "{}.back.controller".format(data["root_base"])
        generate_module2(
            root_package_path=data["root"],
            module_package=inner_path,
            name=name
        )


class ModelGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = False
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        inner_path = "{}.back.model".format(data["root_base"])
        generate_module2(
            root_package_path=data["root"],
            module_package=inner_path,
            name=name
        )


class ServiceGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = False
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        inner_path = "{}.back.service".format(data["root_base"])
        generate_module2(
            root_package_path=data["root"],
            module_package=inner_path,
            name=name
        )


class GenerateNode(ArgNode):
    def setup(self):
        self.commands = {
            "module" : ModuleGeneratorNode,
            "controller": ControllerGeneratorNode,
            "model": ModelGeneratorNode,
            "service": ServiceGeneratorNode
        }
        self.expects_more = True

class RootNode(ArgNode):
    def setup(self):
        self.commands = {
            "generate": GenerateNode,
        }
        self.expects_more = True