# bases1/water-weird.py
"""
WaterWeird creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=water-weird
"""
from creature_base import GlobalCreatureBaseClass


class WaterWeird(GlobalCreatureBaseClass):
    """
    Large elemental creature - WaterWeird
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 16, 'CON': 13, 'INT': 11, 'WIS': 10, 'CHAR': 10, 'armor_class': 13, 'alignment': 'neutral Armor Class  13 Hit Points  58 (9d10 + 9) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['invisible_in_water', 'constrict']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def invisible_in_water(self) -> str:
        """The water weird is invisible while fully immersed in water.Water Bound. The water weird dies if it leaves the water to which it is bound or if that water is destroyed."""
        return 'The water weird is invisible while fully immersed in water.Water Bound. The water weird dies if it leaves the water to which it is bound or if that water is destroyed.'

    def constrict_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 10 ft., one creature. Hit: 13 (3d6 + 3) bludgeoning damage. If the target is Medium or smaller, it is grappled (escape DC 13) and pulled 5 feet toward the water weird. Until this grapple ends, the target is restrained, the water weird tries to drown it, and the water weird can't constrict another target."""
        return "Melee Weapon Attack: +5 to hit, reach 10 ft., one creature. Hit: 13 (3d6 + 3) bludgeoning damage. If the target is Medium or smaller, it is grappled (escape DC 13) and pulled 5 feet toward the water weird. Until this grapple ends, the target is restrained, the water weird tries to drown it, and the water weird can't constrict another target."

