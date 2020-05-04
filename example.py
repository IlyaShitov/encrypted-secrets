from src import get_secret, load_secrets

if __name__ == '__main__':
    load_secrets()
    print('YOUR SECRET: %s' % get_secret('SECRET_KEY'))
