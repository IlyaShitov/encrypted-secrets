# encrypted_secrets

* Либа, основанная на батарейки для джанги `django-encrypted-secrets`. Позволяет шифровать переменные. Работает как на 2, так и на 3 Питоне.

# Шифрование переменных: 
* Зашифрованные переменные хранятся в файле `secrets.yml.enc`, для расшифровки используется файл `master.key`, либо переменная окружения ОС `MASTER_KEY`.
### Инициализация зашифрованного файла `secrets.yml.enc`:
* `python {Название переменного окружения}/lib/{Версия Питона}/site-packages/encrypted_secrets/secrets_manage.py init_secrets`
* Пример: `python .env/lib/python2.7/site-packages/encrypted_secrets/secrets_manage.py init_secrets`
* В папке с проектом появятся 2 файла `secrets.yml.enc` и `master.key`
### Редактирование зашифрованного файла `secrets.yml.enc`:
* Положить рядом с файлом `secrets.yml.enc` файл `master.key`, либо установить переменную `ОС DJANGO_MASTER_KEY` (`export DJANGO_MASTER_KEY=ключ`)
* `python {Название переменного окружения}/lib/{Версия Питона}/site-packages/encrypted_secrets/secrets_manage.py edit_secrets`
* Пример: `python .env/lib/python2.7/site-packages/encrypted_secrets/secrets_manage.py edit_secrets`
* Если появляется ошибка `Unable to open editor; please set your EDITOR environment variable to point to your preferred editor`, то делаем `export EDITOR=nano или vim`
* меняем открывшийся файл, комитим только `secrets.yml.enc` (Ключ нигде не должен светиться)

### Пример находится в файле `example.py`

# Установка:
* `pip install git+ssh://git@new-gitlab.oits.su:2222/its-dev/encrypted_secrets.git`