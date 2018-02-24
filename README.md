# GOFRI

Python3 web framework with builtin SQL-support, ORM, URL-mappings and easily configurable module management and inner builtin packages.

Based on Flask and SqlAlchemy.


To use the framework you can install an early version with running
```setup.py install``` in the 'Gofri' directory.


CLI tool not developed yet, you can generate new project with: 
```python
gofri.lib.project_generator.generate_project(<path>, <name>)

```

and start the newly created app by running ```start.py``` in its generated root package with ```python3```.


Project structure:
```
My-First-Project
    my_first_project
        __init__.py
        start.py
        conf.xml
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