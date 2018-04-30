import os

from gofri.lib.project_generator.cli_nodes import data, RootNode


def execute_command(project_root_package, argv, from_file=True):
    if from_file:
        root_path = project_root_package + "/"
        data["root"] = root_path
        data["root_base"] = os.path.basename(project_root_package)
    else:
        root_path = os.getcwd()
        data["root"] = root_path
        data["root_base"] = os.path.basename(os.getcwd())

    RootNode()
