class Manga:

    def __init__(self, **options):
        """
        API: id, title, english, synonyms, chapters, volumes, score, type, status, start_date, end_date, synopsis, image
        NON-API: japanese, genres, authors, serialization, ranked, popularity, members, favorites, external_links(official_site, animedb, etc), background, related(adaptation, sequel, etc), characters, reviews, recommendations, recent_news, recent_forum, recent_articles
        """
        self.id = options.pop("id")
        self.title = options.pop("title")
        self.english = options.pop("english")
        self.synonyms = options.pop("synonyms")
        self.chapters = options.pop("chapters")
        self.volumes = options.pop("volumes")
        self.score = options.pop("score")
        self.type = options.pop("type")
        self.status = options.pop("status")
        self.start_date = options.pop("start_date")
        self.end_date = options.pop("end_date")
        self.synopsis = options.pop("synopsis")
        self.image = options.pop("image")
        self.japanese = options.pop("japanese")
        self.genres = options.pop("genres")
        self.authors = options.pop("authors")
        self.serialization = options.pop("serialization")
        self.ranked = options.pop("ranked")
        self.popularity = options.pop("popularity")
        self.members = options.pop("members")
        self.favorites = options.pop("favorites")
        self.external_links = options.pop("external_links")
        self.background = options.pop("background")
        self.related = options.pop("related")
        self.characters = options.pop("characters")
        self.reviews = options.pop("reviews")
        self.recommendations = options.pop("recommendations")
        self.recent_news = options.pop("recent_news")
        self.recent_forum = options.pop("recent_forum")
        self.recent_articles = options.pop("recent_articles")

    def __str__(self):
        return self.title

    @property
    def url(self) -> str:
        return "https://myanimelist.net/manga/{}/".format(self.id)
