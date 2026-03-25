# bases1/goblin.py
"""
Goblin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=goblin
"""
from creature_base import GlobalCreatureBaseClass


class Goblin(GlobalCreatureBaseClass):
    """
    Small humanoid (Goblinoid) creature - Goblin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 14, 'CON': 10, 'INT': 10, 'WIS': 8, 'CHAR': 8, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (leather armor', 'legendary': False, 'size': 'Small', 'type': 'humanoid (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['nimble_escape', 'scimitar', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def nimble_escape(self) -> str:
        """The goblin can take the Disengage or Hide action as a bonus action on each of its turns."""
        return 'The goblin can take the Disengage or Hide action as a bonus action on each of its turns.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

