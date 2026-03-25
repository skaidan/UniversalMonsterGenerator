# bases1/bullywug-knight.py
"""
BullywugKnight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bullywug-knight
"""
from creature_base import GlobalCreatureBaseClass


class BullywugKnight(GlobalCreatureBaseClass):
    """
    Medium humanoid creature - BullywugKnight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 66, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 13, 'INT': 9, 'WIS': 11, 'CHAR': 14, 'armor_class': 18, 'alignment': 'typically Lawful Good Armor Class  18 (plate) Hit Points  66 (12d8 + 12) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'glaive']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The knight can breathe air and water.Speak with Frogs and Toads. The knight can communicate simple concepts to frogs and toads when it speaks in Bullywug.Standing Leap. The knight's long jump is up to"""
        return "The knight can breathe air and water.Speak with Frogs and Toads. The knight can communicate simple concepts to frogs and toads when it speaks in Bullywug.Standing Leap. The knight's long jump is up to"

    def multiattack_attack(self) -> str:
        """The knight makes two Glaive attacks."""
        return 'The knight makes two Glaive attacks.'

    def glaive_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit:8 (1d10 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit:8 (1d10 + 3) slashing damage.'

