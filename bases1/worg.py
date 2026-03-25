# bases1/worg.py
"""
Worg creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=worg
"""
from creature_base import GlobalCreatureBaseClass


class Worg(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Worg
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 13, 'CON': 13, 'INT': 7, 'WIS': 11, 'CHAR': 8, 'armor_class': 13, 'alignment': 'neutral evil Armor Class  13 (natural armor) Hit Points  26 (4d10 + 4) Speed  50 ft. STR 16 (+3) DEX 13 (+1) CON 13 (+1) INT 7 (-2) WIS 11 (+0) CHA 8 (-1) Skills  Perception +4 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The worg has advantage on Wisdom (Perception) checks that rely on hearing or smell."""
        return 'The worg has advantage on Wisdom (Perception) checks that rely on hearing or smell.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.'

