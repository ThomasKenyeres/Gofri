from distutils.core import setup

setup(
    name='Gofri',
    version='0.1.0',
    packages=['gofri', 'gofri.lib', 'gofri.lib.pip', 'gofri.lib.xml',
              'gofri.lib.conf', 'gofri.lib.decorate',
              'gofri.lib.project_generator', 'gofri.lib.util'],
    install_requires=[
        'flask',
        'flask_restful',
        'sqlalchemy',
        'importlib',
        'xmltodict',
        'clinodes'
    ],
    url='',
    license='',
    author='thomas',
    author_email='',
    description=''
)
