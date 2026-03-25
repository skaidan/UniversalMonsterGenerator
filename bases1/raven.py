# bases1/raven.py
"""
Raven creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=raven
"""
from creature_base import GlobalCreatureBaseClass


class Raven(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Raven
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 14, 'CON': 8, 'INT': 2, 'WIS': 12, 'CHAR': 6, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  1 (1d4 - 1) Speed  10 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['mimicry', 'beak']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def mimicry(self) -> str:
        """The raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC """
        return 'The raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC '

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 piercing damage.'

