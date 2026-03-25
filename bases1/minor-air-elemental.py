# bases1/minor-air-elemental.py
"""
MinorAirElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=minor-air-elemental
"""
from creature_base import GlobalCreatureBaseClass


class MinorAirElemental(GlobalCreatureBaseClass):
    """
    Tiny elemental creature - MinorAirElemental
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 16, 'min_level': 1, 'level': 1, 'STR': 5, 'DEX': 16, 'CON': 12, 'INT': 3, 'WIS': 10, 'CHAR': 6, 'armor_class': 13, 'alignment': 'neutral Armor Class  13 Hit Points  16 (6d4 + 6) Speed  0 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['air_form', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def air_form(self) -> str:
        """The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 0 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage. If the target was already hit by a minor air elemental's slam attack this turn, it must make a successful DC 11 Strength saving throw or fall prone."""
        return "Melee Weapon Attack: +5 to hit, reach 0 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage. If the target was already hit by a minor air elemental's slam attack this turn, it must make a successful DC 11 Strength saving throw or fall prone."

