import os

def in_development():
    try:
        return os.environ['SERVER_SOFTWARE'].startswith('Development')
    except KeyError:
        return False
