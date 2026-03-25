# bases1/chuul.py
"""
Chuul creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=chuul
"""
from creature_base import GlobalCreatureBaseClass


class Chuul(GlobalCreatureBaseClass):
    """
    Large aberration creature - Chuul
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 10, 'CON': 16, 'INT': 5, 'WIS': 11, 'CHAR': 5, 'armor_class': 16, 'alignment': 'chaotic evil Armor Class  16 (natural armor) Hit Points  93 (11d10 + 33) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'pincer', 'tentacles']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The chuul can breathe air and water.Sense Magic. The chuul senses magic within 120 feet of it at will. This trait otherwise works like the detect magic spell but isn't itself magical."""
        return "The chuul can breathe air and water.Sense Magic. The chuul senses magic within 120 feet of it at will. This trait otherwise works like the detect magic spell but isn't itself magical."

    def multiattack_attack(self) -> str:
        """The chuul makes two pincer attacks. If the chuul is grappling a creature, the chuul can also use its tentacles once."""
        return 'The chuul makes two pincer attacks. If the chuul is grappling a creature, the chuul can also use its tentacles once.'

    def pincer_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage. The target is grappled (escape DC 14) if it is a Large or smaller creature and the chuul doesn't have two other creatures grappled."""
        return "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage. The target is grappled (escape DC 14) if it is a Large or smaller creature and the chuul doesn't have two other creatures grappled."

    def tentacles_attack(self) -> str:
        """One creature grappled by the chuul must succeed on a DC 13 Constitution saving throw or be poisoned for 1 minute. Until this poison ends, the target is paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'One creature grappled by the chuul must succeed on a DC 13 Constitution saving throw or be poisoned for 1 minute. Until this poison ends, the target is paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

