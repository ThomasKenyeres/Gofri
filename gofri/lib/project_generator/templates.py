def build_xml(root_package, name):
    xml = """
    <configuration>
        <project>
            <name>{}</name>
            <app-path>{}</app-path>
        </project>
        <hosting>
            <host></host>
            <port>8080</port>
        </hosting>

        <dependencies>
        </dependencies>

    </configuration>

    """.format(name, root_package)
    return xml


start_file_content = """
import os

from gofri.lib.main import main
from app import modules

if __name__ == '__main__':
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    main(ROOT_PATH, modules)
"""

generator_file_content = """
import os

import sys
from gofri.lib.project_generator.cli import execute_command

def generate():
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    execute_command(ROOT_PATH, sys.argv)

if __name__ == '__main__':
    generate()
"""