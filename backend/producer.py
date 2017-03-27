from .generic import Generic


class Producer:

    def __init__(self, **options):
        self.id = options.pop("id")
        self.name = options.pop("name")


    def __str__(self):
        return self.name

        # anything else?

    @property
    def get_anime(self) -> list:
        """Builds a list of Anime objects pr"""
        # TODO: scrape the producer's page and build a list of Anime objects. How to build those? probably cache all Anime/Manga objects?? Maybe db :thinking:
        return NotImplemented

    @property
    def anime_produced(self) -> int:
        """Returns the number of anime produced by a studio"""
        # docs should stress this is much better than len(self.get_anime) if only the number of anime is needed, but worse if both the list and number are needed
        # TODO: scrape the producer's page and grab the number of anime produced
        return NotImplemented

    @property
    def url(self) -> str:
        return "https://myanimelist.net/anime/producer/{}".format(self.id)
