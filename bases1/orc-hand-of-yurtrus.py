# bases1/orc-hand-of-yurtrus.py
"""
OrcHandOfYurtrus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-hand-of-yurtrus
"""
from creature_base import GlobalCreatureBaseClass


class OrcHandOfYurtrus(GlobalCreatureBaseClass):
    """
    Medium humanoid (Orc) creature - OrcHandOfYurtrus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 30, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 11, 'CON': 16, 'INT': 11, 'WIS': 14, 'CHAR': 9, 'armor_class': 12, 'alignment': 'chaotic evil Armor Class  12 (hide armor) Hit Points  30 (4d8 + 12) Speed  30 ft. STR 12 (+1) DEX 11 (+0) CON 16 (+3) INT 11 (+0) WIS 14 (+2) CHA 9 (-1) Skills  Arcana +2', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Orc)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aggressive', 'touch_of_the_white_hand']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aggressive(self) -> str:
        """As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Spellcasting. The orc is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4"""
        return 'As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Spellcasting. The orc is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4'

    def touch_of_the_white_hand_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 9 (2d8) necrotic damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 9 (2d8) necrotic damage.'

