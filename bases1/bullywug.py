# bases1/bullywug.py
"""
Bullywug creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bullywug
"""
from creature_base import GlobalCreatureBaseClass


class Bullywug(GlobalCreatureBaseClass):
    """
    Medium humanoid (Bullywug) creature - Bullywug
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 12, 'CON': 13, 'INT': 7, 'WIS': 10, 'CHAR': 7, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (hide armor', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Bullywug)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'bite', 'spear']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The bullywug can breathe air and water.Speak with Frogs and Toads. The bullywug can communicate simple concepts to frogs and toads when it speaks in Bullywug.Swamp Camouflage. The bullywug has advanta"""
        return 'The bullywug can breathe air and water.Speak with Frogs and Toads. The bullywug can communicate simple concepts to frogs and toads when it speaks in Bullywug.Swamp Camouflage. The bullywug has advanta'

    def multiattack_attack(self) -> str:
        """The bullywug makes two melee attacks: one with its bite and one with its spear."""
        return 'The bullywug makes two melee attacks: one with its bite and one with its spear.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.'

