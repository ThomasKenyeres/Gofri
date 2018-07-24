import importlib
import os
import shlex
import sys


def check_pname(name):
    #TODO: check if package is available
    if " " in name or name is "":
        return False
    return True

class PIPHandler():
    def __init__(self):
        self.packages = []

    def get_uninstalled_packages(self):
        result = []
        if self.packages is not None:
            for package in self.packages:
                pname = package["name"]
                spec = importlib.util.find_spec(pname)
                if spec is None:
                    result.append(package)
        return result


    def install(self):
        for package in self.get_uninstalled_packages():
            INSTALL_STR = "{} -m pip install".format(sys.executable)
            package_name = package["name"]
            install_scope = package["install"]
            version = package["version"]
            if version == "latest":
                version = None
            if check_pname(package_name):
                print("Installing missing dependency: \"{}\" ...".format(package_name))
                if install_scope == "user":
                    if version is not None:
                        os.system("{} {}=={} --user".format(
                            INSTALL_STR,
                            shlex.quote(package_name),
                            shlex.quote(version)))
                    else:
                        os.system("{} {} --user".format(
                            INSTALL_STR,
                            shlex.quote(package_name)
                        ))
                if install_scope == "system":
                    if version is not None:
                        os.system("sudo -S {} {}=={}".format(
                            INSTALL_STR,
                            shlex.quote(package_name),
                            shlex.quote(version)))
                    else:
                        os.system("sudo -S {} {}".format(
                            INSTALL_STR,
                            shlex.quote(package_name)
                        ))