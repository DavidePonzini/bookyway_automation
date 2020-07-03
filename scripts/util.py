from scripts.bookyway_exception import BookywayException


def log(message):
    print('[*] {}'.format(message))


def warn(message):
    print('[!] {}'.format(message))


def error_quit(message):
    raise BookywayException(message)
