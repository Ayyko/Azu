from bs4 import BeautifulSoup as BS
from .anime import Anime
from .manga import Manga
from .person import Person
from .producer import Producer
from .generic import Generic

def anime_factory(generic: Generic):
    """returns an Anime object by scraping the url defined in a Generic object."""
    # return the object if it's already in cache, save it to cache and return if not
    # all non Generic lib objects should be passed to the dataclass as a Generic, as every lib Object will call a factory for other lib objects
    return NotImplemented


def manga_factory(generic: Generic):
    return NotImplemented


def person_factory(generic: Generic):
    return NotImplemented


def producer_factory(generic: Generic):
    return NotImplemented


def character_factory(generic: Generic):
    return NotImplemented
