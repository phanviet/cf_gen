# This file contains all command lines to generate CloudFormation templates.
# This file uses an extra package called `fire` (author: Google) to generate
# CLI Tools
#
# Current it supports:
# 1. Generating CloudFormation templates snippet as basic as possible. Mainly,
# we will focus only Parameters, Resources and Outputs. The CloudFormation
# template should not be magic and complex.
# 2. The CloudFormation templates written as YAML format.

# ==============================================================================
# BEGIN
# ==============================================================================
import fire

from src.role import exec as role_exec


def role(file_name='role.yml'):
    """
    Generating Cloudformation templates include resources:

    AWS::IAM::Role
    AWS::IAM::Policy
    """
    role_exec(file_name)


if __name__ == '__main__':
    fire.Fire()
