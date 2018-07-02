
import os

from clinodes.nodes import ArgNode, Switch

from gofri.lib.project_generator.generator import generate_project
from gofri.lib.project_generator.module_generator import generate_module
from gofri.lib.project_generator.templates import build_entity_file, build_filter_file

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
        generate_module(
            root_package_path=data["root"],
            module_package=inner_path,
            name=name
        )


class DtoGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = False
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        inner_path = "{}.back.dto".format(data["root_base"])
        generate_module(
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
        generate_module(
            root_package_path=data["root"],
            module_package=inner_path,
            name=name
        )


class EntityGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = False
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        cols = args_remained[1::]
        print(cols)
        inner_path = "{}.back.entity".format(data["root_base"])
        generate_module(
            root_package_path=data["root"],
            module_package=inner_path,
            name=name,
            template=build_entity_file(data["root"], name, cols)
        )


class FilterGeneratorNode(ArgNode):
    def setup(self):
        self.expects_more = False
        self.enable_any = True

    def run(self, *args_remained):
        name = args_remained[0]
        print(name)
        inner_path = "{}.back.filter".format(data["root_base"])
        generate_module(
            root_package_path=data["root"],
            module_package=inner_path,
            name=name,
            template=build_filter_file(data["root"], name)
        )


class GenerateNode(ArgNode):
    def setup(self):
        self.commands = {
            "module" : ModuleGeneratorNode,
            "controller": ControllerGeneratorNode,
            "dto": DtoGeneratorNode,
            "service": ServiceGeneratorNode,
            "entity": EntityGeneratorNode,
            "filter": FilterGeneratorNode
        }
        self.expects_more = True


class EncryptNode(ArgNode):
    def setup(self):
        self.expects_more = False
        pass

    def run(self, *args_remained):
        if len(args_remained) > 0:
            encryptable = args_remained[0]
            if encryptable == "local-config":
                print("Encrypting lc")
                print("Unimplemented")
            else:
                print("Invalid option: '{}'".format(encryptable))
        else:
            print("Please specify what to encrypt")


class VenvSwitch(Switch):
    pass


class NewProjectNode(ArgNode):
    def setup(self):
        self.expects_more = False

    def run(self, *args_remained):
        name = args_remained[0]
        if len(args_remained) == 1:
            print("Generating project...")
            generate_project(os.getcwd(), name)
        elif len(args_remained) == 2:
            generate_project(os.getcwd(), name, use_venv=True)
        else:
            print("Invalid option!")

USE_RELOADER = False

class ReloaderSwitch(Switch):
    def run(self, *args):
        global USE_RELOADER
        USE_RELOADER = True


class StartNode(ArgNode):
    def setup(self):
        self.expects_more = False
        self.switches = {
            "--reload": ReloaderSwitch,
            "--use-reloader": ReloaderSwitch
        }

    def run(self, *args_remained):
        __name__ = "__main__"
        fullpath = "{}/start.py".format(os.getcwd())
        if USE_RELOADER:
            os.system("python3 {} --use-reloader".format(fullpath))
        else:
            os.system("python3 {}".format(fullpath))


class RootNode(ArgNode):
    def setup(self):
        self.commands = {
            "generate": GenerateNode,
            "encrypt": EncryptNode,
            "new": NewProjectNode,
            "start": StartNode
        }
        self.expects_more = True