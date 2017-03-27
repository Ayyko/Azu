from .factory import character_factory


class Person:

    def __init__(self, **options):
        self.id = options.pop("id")
        self.given_name = options.pop("given_name_en")
        self.family_name = options.pop("family_name_en")
        self.given_name_jp = options.pop("given_name_jp")
        self.family_name_jp = options.pop("family_name_jp")
        self.birthday = options.pop("birthday")
        self.favorites = options.pop("member_favorites")
        self.more = options.pop("more")
        self._va_roles = options.pop("va_roles")
        self._staff_positions = options.pop("staff_positions")
        self._published_manga = options.pop("published_manga")


    def __str__(self):
        return "{}, {}".format(self.family_name, self.given_name)


    @property
    def get_voice_acting_roles(self) -> list:
        for character in self._va_roles:
            yield character_factory(character)

    @property
    def get_anime_staff_positions(self) -> list:

        # Better than get_va_roles but still could be a better way idk
        return NotImplemented

    @property
    def get_published_manga(self) -> list:
        """Builds a list of tuples in the form (Manga, role) where Manga is a Manga object and role is a str in the form 'Story'/'Art'/etc"""
        return NotImplemented
