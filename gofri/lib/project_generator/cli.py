import os

from gofri.lib.project_generator.cli_nodes import data, RootNode


def execute_command(project_root_package, argv):
    command_words = argv[1::]
    print("COMMANDS: {} from {}".format(command_words, project_root_package))

    root_path = project_root_package + "/"
    data["root"] = root_path
    data["root_base"] = os.path.basename(project_root_package)

    RootNode()
