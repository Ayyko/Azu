from .factory import anime_factory, manga_factory, person_factory


class Character:

    def __init__(self, **options):
        self.id = options.pop("id")  # str
        self.name = options.pop("name")  # str
        self.japanese_name = options.pop("jap_name")  # str
        self.bio = options.pop("bio")  # str
        self._anime = options.pop("anime")  # list of Generics to be turned into objects
        self._manga = options.pop("manga")  # list of Generics to be turned into objects
        self.favorites = options.pop("favorites")  # int
        self._voice_actors = options.pop("voice_actors")  # list of Generics to be turned into objects

    def __str__(self):
        return self.name

    @property
    def get_anime(self):
        if not self._anime:
            return None

        for anime in self._anime:
            yield anime_factory(anime)

    @property
    def get_manga(self):
        if not self._manga:
            return None

        for manga in self._manga:
            yield manga_factory(manga)

    @property
    def get_voice_actors(self):
        if not self._voice_actors:
            return None

        for va in self._voice_actors:
            yield person_factory(va)
