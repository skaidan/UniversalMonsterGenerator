# bases1/lion.py
"""
Lion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lion
"""
from creature_base import GlobalCreatureBaseClass


class Lion(GlobalCreatureBaseClass):
    """
    Large beast creature - Lion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 15, 'CON': 13, 'INT': 3, 'WIS': 12, 'CHAR': 8, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  26 (4d10 + 4) Speed  50 ft. STR 17 (+3) DEX 15 (+2) CON 13 (+1) INT 3 (-4) WIS 12 (+1) CHA 8 (-1) Skills  Perception +3', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The lion has advantage on Wisdom (Perception) checks that rely on smell.Pack Tactics. The lion has advantage on an attack roll against a creature if at least one of the lion's allies is within 5 feet """
        return "The lion has advantage on Wisdom (Perception) checks that rely on smell.Pack Tactics. The lion has advantage on an attack roll against a creature if at least one of the lion's allies is within 5 feet "

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

