import os

def create_import_statement(project_path, name):
    package = str(project_path).replace("/", ".")
    return "from app.{} import {}".format(package, name)

def generate_module(root_package_path, inner_path, name, template=""):
    #TODO: __init__.py generation in each directory from root package!!!
    fullpath = "{}/{}".format(root_package_path, inner_path)
    file_path = "{}/{}.py".format(fullpath, name)

    os.makedirs(fullpath, exist_ok=True)

    with open("{}{}/{}.py".format(root_package_path, inner_path, name), "w+") as module_file:
        module_file.write(template)

    modules_py_path = "{}/modules.py".format(root_package_path)

    old = ""
    with open(modules_py_path, "r") as modules_py:
        old = modules_py.read()

    with open(modules_py_path, "w+") as modules_py:
        print(old)
        new = old + "\n{}".format(create_import_statement(inner_path, name))
        modules_py.write(new)


if __name__ == '__main__':
    generate_module(
        root_package_path="/home/thomas/MyThings/PROG/PYTHON/MyProjects/try/serpent/SerpentExample1/app/",
        inner_path="back/controller",
        name="van_controller"
    )
    """generate_module(
        "/home/thomas/MyThings/PROG/PYTHON/MyProjects/try/serpent/SerpentExample1/app/",
        "back/service",
        "person_service"
    )"""
