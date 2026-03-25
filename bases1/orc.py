# bases1/orc.py
"""
Orc creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc
"""
from creature_base import GlobalCreatureBaseClass


class Orc(GlobalCreatureBaseClass):
    """
    Medium humanoid (Orc) creature - Orc
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 15, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 16, 'INT': 7, 'WIS': 11, 'CHAR': 10, 'armor_class': 13, 'alignment': 'chaotic evil Armor Class  13 (hide armor) Hit Points  15 (2d8 + 6) Speed  30 ft. STR 16 (+3) DEX 12 (+1) CON 16 (+3) INT 7 (-2) WIS 11 (+0) CHA 10 (+0) Skills  Intimidation +2 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Orc)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aggressive', 'greataxe', 'javelin']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aggressive(self) -> str:
        """As a bonus action, the orc can move up to its speed toward a hostile creature that it can see."""
        return 'As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d12 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d12 + 3) slashing damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

