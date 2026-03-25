# bases1/giant-rat.py
"""
GiantRat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-rat
"""
from creature_base import GlobalCreatureBaseClass


class GiantRat(GlobalCreatureBaseClass):
    """
    Small beast creature - GiantRat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 15, 'CON': 11, 'INT': 2, 'WIS': 10, 'CHAR': 4, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  7 (2d6) Speed  30 ft. STR 7 (-2) DEX 15 (+2) CON 11 (+0) INT 2 (-4) WIS 10 (+0) CHA 4 (-3) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The rat has advantage on Wisdom (Perception) checks that rely on smell.Pack Tactics. The rat has advantage on an attack roll against a creature if at least one of the rat's allies is within 5 feet of """
        return "The rat has advantage on Wisdom (Perception) checks that rely on smell.Pack Tactics. The rat has advantage on an attack roll against a creature if at least one of the rat's allies is within 5 feet of "

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

