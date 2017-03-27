from .factory import producer_factory, person_factory, character_factory, manga_factory, anime_factory
from .generic import Generic


class Anime:

    def __init__(self, **options):
        """
        API: id, title, english, synonyms, episodes, score, type, status, start_date, end_date, synopsis, image
        NON-API: japanese, producers, licensors, studio, source, genres, duration, rating, ranked, popularity, members, favorites, external_links(official_site, animedb, etc), background, related(adaptation, sequel, etc), characters, voice_actors, staff, opening_theme(s), ending_theme(s), reviews, recommendations, recent_news, recent_forum, recent_articles, fansubbing_groups
        """
        # TODO: check if any of these can be omitted by the anime page
        # some of these should be defined differently later probably
        self.id = options.pop("id")  # str
        self.title = options.pop("title")  # str
        self.english = options.pop("english")  # str
        self.synonyms = options.pop("synonyms")  # list of str
        self.episodes = options.pop("episodes")  # int
        self.score = options.pop("score")  # str(?)
        self.type = options.pop("type")  # str
        self.status = options.pop("status")  # str
        self.start_date = options.pop("start_date")  # str(datetime/unix time?)
        self.end_date = options.pop("end_date")  # str(datetime/unix time?)
        self.synopsis = options.pop("synopsis")  # str
        self.image = options.pop("image")  # str
        self.japanese = options.pop("japanese")  # str
        self._producers = options.pop("producers")  # list of Generics to be turned into real objects
        self._licensors = options.pop("licensors")  # list of Generics to be turned into real objects
        self._studios = options.pop("studios")  # list of Generics to be turned into real objects
        self.source = options.pop("source")  # str
        self.genres = options.pop("genres")  # list of str
        self.duration = options.pop("duration")  # str
        self.rating = options.pop("rating")  # str
        self.ranked = options.pop("ranked")  # int or None (str?)
        self.popularity = options.pop("popularity")  # int
        self.members = options.pop("members")  # int
        self.favorites = options.pop("favorites")  # int
        self.external_links = options.pop("external_links")  # list of Generics (link title, link url)
        self.background = options.pop("background")  # str
        self._related = options.pop("related")  # list of Generics (title, Generic(object skeleton to be turned into real object), type, relation)
        self._characters = options.pop("characters")  # list of Generics to be turned into real objects
        self._voice_actors = options.pop("voice_actors")  # list of Generics to be turned into real objects
        self._staff = options.pop("staff")  # list of Generics to be turned into real objects
        self.opening_themes = options.pop("opening_theme(s)")  # list of Generics (title, artist, episodes
        self.ending_themes = options.pop("ending_theme(s)")  # list of Generics (title, artist, episodes

        # TODO: everything below
        # self._reviews = options.pop("reviews")
        # self._recommendations = options.pop("recommendations")
        # self._recent_news = options.pop("recent_news")
        # self._recent_forum = options.pop("recent_forum")
        # self._recent_articles = options.pop("recent_articles")
        # self._fansubbing_groups = options.pop("fansubbing_groups")

    def __str__(self):
        return self.title

    @property
    def url(self) -> str:
        return "https://myanimelist.net/anime/{}".format(self.id)

    @property
    def get_producers(self):
        """Returns a generator with every Producer listed on the Anime's page"""
        # generators, ofc how could I forget!
        if not  self._producers:
            return None

        for producer in self._producers:
            yield producer_factory(producer)

    @property
    def get_licensors(self):
        """Returns a generator with every Licensor listed on the Anime's page"""
        if not self._licensors:
            return None

        for licensor in self._licensors:
            yield producer_factory(licensor)

    @property
    def get_studios(self):
        """Returns a generator with every Studio listed on the Anime's page"""
        if not self._studios:
            return None

        for studio in self._studios:
            yield producer_factory(studio)

    @property
    def get_related(self):
        """Returns a generator with a Generic object for each related work. """
        if not self._related:
            return None

        for related in self._related:
            ret = Generic(url=related.url, name=related.name, type=related.type, kind=related.kind)
            if related.type == "anime":
                ret._anime = anime_factory(related.anime)
            if related.type == "manga":
                ret.manga = manga_factory(related.manga)
            yield ret

    @property
    def get_characters(self):
        if not self._characters:
            return None

        for character in self._characters:
            yield character_factory(character)

    @property
    def get_voice_actors(self):
        if not self._voice_actors:
            return None

        for va in self._voice_actors:
            yield person_factory(va)

    @property
    def get_staff(self):
        if not self._staff:
            return None

        for staff in self._staff:
            yield person_factory(staff)
