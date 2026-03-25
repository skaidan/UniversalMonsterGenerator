# bases1/wolf.py
"""
Wolf creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wolf
"""
from creature_base import GlobalCreatureBaseClass


class Wolf(GlobalCreatureBaseClass):
    """
    Medium beast creature - Wolf
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 15, 'CON': 12, 'INT': 3, 'WIS': 12, 'CHAR': 6, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  11 (2d8 + 2) Speed  40 ft. STR 12 (+1) DEX 15 (+2) CON 12 (+1) INT 3 (-4) WIS 12 (+1) CHA 6 (-2) Skills  Perception +3', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The wolf has advantage on attack rolls against a creature if at least one of the wolf's allies is withi"""
        return "The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The wolf has advantage on attack rolls against a creature if at least one of the wolf's allies is withi"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) piercing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone.'

