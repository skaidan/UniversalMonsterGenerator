# bases1/dancing-item.py
"""
DancingItem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dancing-item
"""
from creature_base import GlobalCreatureBaseClass


class DancingItem(GlobalCreatureBaseClass):
    """
    Large construct creature - DancingItem
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 16, 'INT': 4, 'WIS': 10, 'CHAR': 6, 'armor_class': 16, 'alignment': '- Armor Class  16 (natural armor) Hit Points  10 + five times your bard level Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['immutable_form', 'force-empowered_slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def immutable_form(self) -> str:
        """The item is immune to any spell or effect that would alter its form.Irrepressible Dance. When any creature starts its turn within 10 feet of the item, the item can increase or decrease (your choice) t"""
        return 'The item is immune to any spell or effect that would alter its form.Irrepressible Dance. When any creature starts its turn within 10 feet of the item, the item can increase or decrease (your choice) t'

    def force-empowered_slam_attack(self) -> str:
        """Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target you can see. Hit: 1d10 + PB force damage."""
        return 'Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target you can see. Hit: 1d10 + PB force damage.'

