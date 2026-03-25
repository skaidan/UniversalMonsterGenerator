# bases1/acolyte.py
"""
Acolyte creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=acolyte
"""
from creature_base import GlobalCreatureBaseClass


class Acolyte(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Acolyte
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 9, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 10, 'CON': 10, 'INT': 10, 'WIS': 14, 'CHAR': 11, 'armor_class': 10, 'alignment': 'any alignment Armor Class  10 Hit Points  9 (2d8) Speed  30 ft. STR 10 (+0) DEX 10 (+0) CON 10 (+0) INT 10 (+0) WIS 14 (+2) CHA 11 (+0) Skills  Medicine +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['spellcasting', 'club']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def spellcasting(self) -> str:
        """The acolyte is a 1st-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). The acolyte has the following cleric spells prepared:Cantrips (at will): li"""
        return 'The acolyte is a 1st-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). The acolyte has the following cleric spells prepared:Cantrips (at will): li'

    def club_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.'

