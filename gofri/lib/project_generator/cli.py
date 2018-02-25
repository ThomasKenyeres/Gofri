from gofri.lib.project_generator.module_generator import generate_module


def execute_command(project_root_package, argv):
    command_words = argv[1::]
    print("COMMANDS: {} from {}".format(command_words, project_root_package))

    #TODO: beautify cli argparse

    try:
        root_path = project_root_package + "/"
        command = command_words[0]
        if command == "generate":
            option = command_words[1]
            if option == "project":
                print("GEN project")
            elif option == "module":
                name = command_words[2]
                path = ""
                if len(command_words) == 4:
                    path = command_words[3]
                    generate_module(
                        root_package_path=root_path,
                        inner_path=path,
                        name=name
                    )
                    print("Generated module {} at {}".format(name, path))
            elif option == "controller":
                name = command_words[2]
                generate_module(
                    root_package_path=root_path,
                    inner_path="back/controller",
                    name=name
                )
                print("Generated controller {}".format(name))
            else:
                raise IndexError()
    except IndexError:
        print("Invalid input!")
