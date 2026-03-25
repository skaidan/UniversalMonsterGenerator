# bases1/wild-dog-alpha.py
"""
WildDogAlpha creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wild-dog-alpha
"""
from creature_base import GlobalCreatureBaseClass


class WildDogAlpha(GlobalCreatureBaseClass):
    """
    Large beast creature - WildDogAlpha
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 15, 'CON': 13, 'INT': 3, 'WIS': 12, 'CHAR': 8, 'armor_class': 12, 'alignment': "unaligned Armor Class  12 Hit Points  26 (4d10 + 4) Speed  50 ft. STR 17 (+3) DEX 15 (+2) CON 13 (+1) INT 3 (-4) WIS 12 (+1) CHA 8 (-1) Skills  Perception +3 Senses  passive Perception 13 Languages  — Challenge  1 (200 XP) Keen Hearing and Smell . The wild dog alpha has advantage on Wisdom (Perception) checks that rely on hearing or smell. Pack Tactics . The wild dog alpha has advantage on an attack roll against a creature if at least one of the wild dog alpha's allies is within 5 feet of the creature and the ally isn't incapacitated. Pounce . If the wild dog alpha moves at least 20 feet straight toward a creature and then hits it with a bite attack on the same turn", 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The wild dog alpha has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The wild dog alpha has advantage on an attack roll against a creature if at least one of the """
        return 'The wild dog alpha has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The wild dog alpha has advantage on an attack roll against a creature if at least one of the '

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage.'

