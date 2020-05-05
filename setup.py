import setuptools
import os


def get_log_description():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description


def get_install_requires():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    requirement_path = base_dir + '/requirements.txt'
    install_requires = []  # Examples: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
    if os.path.isfile(requirement_path):
        with open(requirement_path) as f:
            install_requires = f.read().splitlines()
    return install_requires


setuptools.setup(
    name="encrypted_secrets_its",
    version="0.0.1",
    author="Shitov Ilya",
    author_email="nagibator228@example.com",
    description="Либа, основанная на батарейки для джанги django-encrypted-secrets. Позволяет шифровать переменные.",
    long_description=get_log_description(),
    long_description_content_type="text/markdown",
    install_requires=get_install_requires(),
    url="https://new-gitlab.oits.su/its-dev/encrypted_secrets",
    packages=setuptools.find_packages(),
    python_requires='>=2.7',
    entry_points = {
        'console_scripts': [
            'init_secrets=encrypted_secrets.secrets_manage:init_secrets',
            'edit_secrets=encrypted_secrets.secrets_manage:edit_secrets'
        ],
    }
)
