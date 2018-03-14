# GOFRI

Python3 web framework with builtin SQL-support, ORM, URL-mappings and easily configurable module management and inner builtin packages.

Uses Flask and SqlAlchemy.

Documented at: <gofri.readthedocs.io>

### Install

To install latest version run ```pip3 install Gofri```.

### Create project

To create a project run ```python3 -m gofri.generate_project <ProjectName>``` and the project will be created in the current directory.

### Start your application

To start the newly created app run ```start.py``` in its generated root package with ```python3```.




Project structure:
```
My-First-Project
    my_first_project
        __init__.py
        start.py
        conf.xml
        modules.py
        generate.py
        back
            __init__.py
            controller
                __init__.py
                ...
            dao
                __init__.py
                ...
            ...
        web
            <web content if needed>
```

### Gofri CLI

You can add new modules easily:
```
<Project>/<root_package>/generate.py generate module <name> <packages>
```

```
MyFirstProject/my_first_project/generate.py generate module my_module my_first_project.back.dao
```

Or add a controller more easily:
```
<Project>/<root_package>/generate.py generate controller <name>
```

```
MyFirstProject/my_first_project/generate.py generate controller my_controller
```