# bases1/jackal.py
"""
Jackal creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=jackal
"""
from creature_base import GlobalCreatureBaseClass


class Jackal(GlobalCreatureBaseClass):
    """
    Small beast creature - Jackal
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 3, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 15, 'CON': 11, 'INT': 3, 'WIS': 12, 'CHAR': 6, 'armor_class': 12, 'alignment': "unaligned Armor Class  12 Hit Points  3 (1d6) Speed  40 ft. STR 8 (-1) DEX 15 (+2) CON 11 (+0) INT 3 (-4) WIS 12 (+1) CHA 6 (-2) Skills  Perception +3 Senses  passive Perception 13 Languages  — Challenge  0 (10 XP) Keen Hearing and Smell . The jackal has advantage on Wisdom (Perception) checks that rely on hearing or smell. Pack Tactics . The jackal has advantage on an attack roll against a creature if at least one of the jackal's allies is within 5 feet of the creature and the ally isn't incapacitated. Actions Bite .  Melee Weapon Attack : +1 to hit", 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The jackal has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The jackal has advantage on an attack roll against a creature if at least one of the jackal's allies """
        return "The jackal has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The jackal has advantage on an attack roll against a creature if at least one of the jackal's allies "

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) piercing damage."""
        return 'Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) piercing damage.'

