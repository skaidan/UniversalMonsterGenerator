# bases1/goblin-boss.py
"""
GoblinBoss creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=goblin-boss
"""
from creature_base import GlobalCreatureBaseClass


class GoblinBoss(GlobalCreatureBaseClass):
    """
    Small humanoid (Goblinoid) creature - GoblinBoss
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 21, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 10, 'INT': 10, 'WIS': 8, 'CHAR': 10, 'armor_class': 17, 'alignment': 'neutral evil Armor Class  17 (chain shirt', 'legendary': False, 'size': 'Small', 'type': 'humanoid (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['nimble_escape', 'multiattack', 'scimitar', 'javelin']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def nimble_escape(self) -> str:
        """The goblin can take the Disengage or Hide action as a bonus action on each of its turns."""
        return 'The goblin can take the Disengage or Hide action as a bonus action on each of its turns.'

    def multiattack_attack(self) -> str:
        """The goblin makes two attacks with its scimitar. The second attack has disadvantage."""
        return 'The goblin makes two attacks with its scimitar. The second attack has disadvantage.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 3 (1d6) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 3 (1d6) piercing damage.'

