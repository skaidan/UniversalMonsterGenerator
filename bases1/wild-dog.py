# bases1/wild-dog.py
"""
WildDog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wild-dog
"""
from creature_base import GlobalCreatureBaseClass


class WildDog(GlobalCreatureBaseClass):
    """
    Medium beast creature - WildDog
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 5, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 14, 'CON': 12, 'INT': 3, 'WIS': 12, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  5 (1d8 + 1) Speed  40 ft. STR 13 (+1) DEX 14 (+2) CON 12 (+1) INT 3 (-4) WIS 12 (+1) CHA 7 (-2) Skills  Perception +3 Senses  passive Perception 13 Languages  — Challenge  1/8 (25 XP) Keen Hearing and Smell . The wild dog has advantage on Wisdom (Perception) checks that rely on hearing or smell. Actions Bite .  Melee Weapon Attack : +3 to hit', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The wild dog has advantage on Wisdom (Perception) checks that rely on hearing or smell."""
        return 'The wild dog has advantage on Wisdom (Perception) checks that rely on hearing or smell.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage.'

