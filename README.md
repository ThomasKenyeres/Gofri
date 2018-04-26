# GOFRI

Python3 web framework with builtin SQL-support, ORM, URL-mappings and easily configurable module management and inner builtin packages.
Uses Werkzeug/Jinja and SqlAlchemy.

Documented at: http://gofri.readthedocs.io

**LATEST: 1.0.3**

---
**NEXT VERSION: 2.0.0**

1. Extension handling &#10004;
1. JWT extension
1. New config possibilities
1. CORS support &#10004;
1. Local config encryption
1. Template projects for getting started
1. Virtualenv support
---
*&#10004; : available in developer version(this repo).

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