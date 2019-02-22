import shutil


def generate_start_banner(version):
    return """

 ██████╗  ██████╗ ███████╗██████╗ ██╗
██╔════╝ ██╔═══██╗██╔════╝██╔══██╗██║
██║  ███╗██║   ██║█████╗  ██████╔╝██║
██║   ██║██║   ██║██╔══╝  ██╔══██╗██║
╚██████╔╝╚██████╔╝██║     ██║  ██║██║
 ╚═════╝  ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝    
version {}
{}
        """.format(version, "_" * shutil.get_terminal_size().columns)