# bases1/dire-wolf.py
"""
DireWolf creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dire-wolf
"""
from creature_base import GlobalCreatureBaseClass


class DireWolf(GlobalCreatureBaseClass):
    """
    Large beast creature - DireWolf
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 37, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 15, 'CON': 15, 'INT': 3, 'WIS': 12, 'CHAR': 7, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  37 (5d10 + 10) Speed  50 ft. STR 17 (+3) DEX 15 (+2) CON 15 (+2) INT 3 (-4) WIS 12 (+1) CHA 7 (-2) Skills  Perception +3', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is wit"""
        return "The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is wit"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.'

