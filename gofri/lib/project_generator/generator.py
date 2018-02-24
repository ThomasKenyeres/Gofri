import os

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



def generate_xml(root_package, name):
    with open("{}/{}".format(root_package, "conf.xml"), "w") as xml_file:
        xml_file.write(build_xml(root_package, name))

def generate_web_dir(root_package):
    os.makedirs("{}/{}".format(root_package, "web"), exist_ok=True)
    open("{}/{}/{}".format(root_package, "web", "__init__.py"), "w")

def generate_back_dir(root_package):
    os.makedirs("{}/{}/{}".format(root_package, "back", "controller"), exist_ok=True)
    open("{}/{}/{}".format(root_package, "back", "__init__.py"), "w")

def get_project_name(name):
    root_package = ""
    for char in str(name):
        if char.isalnum():
            root_package += char
        else:
            root_package += "_"
    return root_package.lower()


def generate_project(path, name, web=True, back=True, db=True, orm=True, custom_xml=False):
    root_package_name = get_project_name(name)
    root_package = "{}/{}/{}".format(path, name, root_package_name)

    os.makedirs(root_package, exist_ok=True)
    open("{}/{}".format(root_package, "__init__.py"), "w")
    generate_xml(root_package, name)
    if web:
        generate_web_dir(root_package)
    if back:
        generate_back_dir(root_package)