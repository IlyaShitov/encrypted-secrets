import os
import tempfile
import subprocess
import src.conf as secrets_conf
from src import secrets
from src.aes import AESCipher


def detect_mode(**kwargs):
    pass


def write_secrets(message, key=secrets_conf.ENCRYPTED_SECRETS_KEY, encrypted_secrets_path=secrets_conf.ENCRYPTED_SECRETS_PATH):
    with open(encrypted_secrets_path, 'w') as encrypted_secrets_file:
        cipher = AESCipher(message, key)
        encrypted = cipher.encrypt()
        encrypted_secrets_file.write(encrypted)


def read_secrets(encrypted_secrets_file_path=secrets_conf.ENCRYPTED_SECRETS_PATH, key=secrets_conf.ENCRYPTED_SECRETS_KEY):
    key_file_exists = os.path.isfile(encrypted_secrets_file_path)

    if not key_file_exists:
        return False

    with open(encrypted_secrets_file_path, 'r') as encrypted_secrets_file:
        message = encrypted_secrets_file.read()
        cipher = AESCipher(message, key)
        decrypted = cipher.decrypt()

    return decrypted


def check_editor():
    if not os.environ.get('EDITOR'):
        raise Exception('Unable to open editor; please set your EDITOR '
                        'environment variable to point to your preferred '
                        'editor, e.g. "/usr/bin/vim" or simply "vim"')
    return os.environ['EDITOR']


def edit_secrets():
    editor = check_editor()
    decrypted_content = read_secrets()
    fd, filename = tempfile.mkstemp(text=True)
    f = open(filename, 'w')
    f.write(decrypted_content)
    f.close()
    cmd = '%s %s' % (editor, filename)
    write_status = subprocess.call(cmd, shell=True)

    if write_status != 0:
        os.remove(filename)
        raise Exception("The editor returned a non-zero status "
                        "(that means it failed.)")
    f = open(filename)
    unencrypted_contents = f.read()
    write_secrets(unencrypted_contents)
    f.close()
    os.remove(filename)


def new_yaml_file_template():
  message = "# Write the credentials that you want to encrypt in YAML format below.\n" \
            "# for example:\n" \
            "#\n" \
            "# aws:\n" \
            "#   access_key_id: 123\n" \
            "#   secret_access_key: 345"
  return message


def write_default_encrypted_secrets_file(encrypted_secrets_path, key):

    write_secrets(new_yaml_file_template(), key, encrypted_secrets_path)


def init_secrets():
    key = secrets.token_urlsafe(256)
    path = secrets_conf.ENCRYPTED_SECRETS_KEY_PATH
    file = open(path, 'w')
    file.write(key)
    file.close()

    encrypted_secrets_path = secrets_conf.DEFAULT_YAML_PATH

    encrypted_file_exists = os.path.isfile(encrypted_secrets_path)

    if not encrypted_file_exists:
        write_default_encrypted_secrets_file(encrypted_secrets_path, key)
