# bases1/lizardfolk.py
"""
Lizardfolk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lizardfolk
"""
from creature_base import GlobalCreatureBaseClass


class Lizardfolk(GlobalCreatureBaseClass):
    """
    Medium humanoid (Lizardfolk) creature - Lizardfolk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 13, 'INT': 7, 'WIS': 12, 'CHAR': 7, 'armor_class': 15, 'alignment': 'neutral Armor Class  15 (natural armor', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Lizardfolk)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'multiattack', 'bite', 'heavy_club', 'javelin', 'spiked_shield']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The lizardfolk can hold its breath for 15 minutes."""
        return 'The lizardfolk can hold its breath for 15 minutes.'

    def multiattack_attack(self) -> str:
        """The lizardfolk makes two melee attacks, each one with a different weapon."""
        return 'The lizardfolk makes two melee attacks, each one with a different weapon.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def heavy_club_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def spiked_shield_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

