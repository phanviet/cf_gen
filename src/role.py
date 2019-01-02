import yaml

from src.utils import get_file_build_path


def exec(file_name='role.yml'):
    """
    Generating Cloudformation templates include resources:

    AWS::IAM::Role
    AWS::IAM::Policy
    """
    file_path = get_file_build_path(file_name)
    body = {
        'test': 'Hello world'
    }
    with open(file_path, 'w') as outfile:
        yaml.dump(body, outfile, default_flow_style=False)
