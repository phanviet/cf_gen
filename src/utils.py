import os

from config import BUILD_PATH


# All CloudFormation templates will be here after generating
if not os.path.exists(BUILD_PATH):
    os.mkdir(BUILD_PATH)


def get_file_build_path(file_name):
    return '{}/{}'.format(BUILD_PATH, file_name)
