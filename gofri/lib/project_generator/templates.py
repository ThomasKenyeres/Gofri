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


def build_start_file_content(root_package_name):
    start_file_content = """import os
import sys
from gofri.lib.main import main

sys.path.append(sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from {} import modules
    
if __name__ == '__main__':
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    main(ROOT_PATH, modules)
""".format(root_package_name)
    return start_file_content

generator_file_content = """import os
import sys
from gofri.lib.project_generator.cli import execute_command

def generate():
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    execute_command(ROOT_PATH, sys.argv)

if __name__ == '__main__':
    generate()
"""