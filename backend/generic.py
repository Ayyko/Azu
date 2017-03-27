from .factory import *


class Generic:

    def __init__(self, **options):
        self.url = options.pop("url", None)
        self.name = options.pop("name")
        self.type = options.pop("type", None)  # "generic" maybe?
        self.__dict__.update(options)

    def __str__(self):
        return self.name
