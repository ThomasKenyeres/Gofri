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


start_file = """
import os
from gofri.lib.main import main

if __name__ == '__main__':
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    main(ROOT_PATH)
"""