# bases1/minor-water-elemental.py
"""
MinorWaterElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=minor-water-elemental
"""
from creature_base import GlobalCreatureBaseClass


class MinorWaterElemental(GlobalCreatureBaseClass):
    """
    Small elemental creature - MinorWaterElemental
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 17, 'INT': 3, 'WIS': 10, 'CHAR': 8, 'armor_class': 13, 'alignment': 'neutral Armor Class  13 (natural armor) Hit Points  39 (6d6 + 18) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['water_form', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def water_form(self) -> str:
        """The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.Freeze. If the elemental takes cold damage, it partially freez"""
        return "The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.Freeze. If the elemental takes cold damage, it partially freez"

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage. If the target has been hit by another minor water elemental's slam attack this round, it must succeed on a DC 11 Strength saving throw or be pushed 5 feet in a direction of this elemental's choice."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage. If the target has been hit by another minor water elemental's slam attack this round, it must succeed on a DC 11 Strength saving throw or be pushed 5 feet in a direction of this elemental's choice."

