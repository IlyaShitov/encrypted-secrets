# -*- coding: future_fstrings -*-
import os

SECRETS_ROOT = os.environ.get('SECRETS_ROOT',  os.getcwd())

DEFAULT_YAML_PATH = f'{SECRETS_ROOT}/secrets.yml.enc'

ENCRYPTED_SECRETS_KEY_PATH = f'{SECRETS_ROOT}/master.key'

key_file_exists = os.path.isfile(ENCRYPTED_SECRETS_KEY_PATH)

if key_file_exists:
    ENCRYPTED_SECRETS_KEY = open(f'{SECRETS_ROOT}/master.key').read()
else:
    ENCRYPTED_SECRETS_KEY = None

ENCRYPTED_SECRETS_KEY = os.environ.get('MASTER_KEY', ENCRYPTED_SECRETS_KEY)

ENCRYPTED_SECRETS_PATH = f'{SECRETS_ROOT}/secrets.yml.enc'

encrypted_file_exists = os.path.isfile(ENCRYPTED_SECRETS_PATH)
