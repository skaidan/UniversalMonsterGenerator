# bases1/orc-claw-of-luthic.py
"""
OrcClawOfLuthic creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-claw-of-luthic
"""
from creature_base import GlobalCreatureBaseClass


class OrcClawOfLuthic(GlobalCreatureBaseClass):
    """
    Medium humanoid (Orc) creature - OrcClawOfLuthic
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 15, 'CON': 16, 'INT': 10, 'WIS': 15, 'CHAR': 11, 'armor_class': 14, 'alignment': 'chaotic evil Armor Class  14 (hide armor) Hit Points  45 (6d8 + 18) Speed  30 ft. STR 14 (+2) DEX 15 (+2) CON 16 (+3) INT 10 (+0) WIS 15 (+2) CHA 11 (+0) Skills  Intimidation +2', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Orc)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aggressive', 'multiattack', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aggressive(self) -> str:
        """As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Spellcasting. The orc is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4"""
        return 'As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Spellcasting. The orc is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4'

    def multiattack_attack(self) -> str:
        """The orc makes two claw attacks, or four claw attacks if it has fewer than half of its hit points remaining."""
        return 'The orc makes two claw attacks, or four claw attacks if it has fewer than half of its hit points remaining.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage.'

