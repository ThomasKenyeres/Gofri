from clinodes.nodes import ArgNode
from gofri.lib.project_generator.module_generator import generate_module

data = {}

class ModuleGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = True
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        inner_path = args_remained[1]
        generate_module(
            root_package_path=data["root"],
            inner_path=inner_path,
            name=name
        )

class ControllerGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = False
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        inner_path = "back/controller"
        generate_module(
            root_package_path=data["root"],
            inner_path=inner_path,
            name=name
        )

class GenerateNode(ArgNode):
    def setup(self):
        self.commands = {
            "module" : ModuleGeneratorNode,
            "controller": ControllerGeneratorNode
        }
        self.expects_more = True

class RootNode(ArgNode):
    def setup(self):
        self.commands = {
            "generate": GenerateNode
        }
        self.expects_more = True


if __name__ == '__main__':
    RootNode()