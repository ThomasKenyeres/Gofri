import os


def init_custom_conf_file(root_path):
    print("FILE EXISTS: ", os.path.exists(root_path + "/local.ini"))
    if not os.path.exists(root_path + "/local.ini"):
        print("CFILE creation")
        with open(root_path + "/local.ini", "w") as cfile:
            cfile.close()