from .util import init_secrets as init_secrets_handle
from .util import edit_secrets as edit_secrets_handle
import fire


def init_secrets():
    init_secrets_handle()


def edit_secrets():
    edit_secrets_handle()


if __name__ == '__main__':
    fire.Fire()
