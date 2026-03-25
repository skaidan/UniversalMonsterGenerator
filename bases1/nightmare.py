# bases1/nightmare.py
"""
Nightmare creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nightmare
"""
from creature_base import GlobalCreatureBaseClass


class Nightmare(GlobalCreatureBaseClass):
    """
    Large fiend creature - Nightmare
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 10, 'WIS': 13, 'CHAR': 15, 'armor_class': 13, 'alignment': 'neutral evil Armor Class  13 (natural armor) Hit Points  68 (8d10 + 24) Speed  60 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['confer_fire_resistance', 'hooves', 'ethereal_stride']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def confer_fire_resistance(self) -> str:
        """The nightmare can grant resistance to fire damage to anyone riding it.Illumination. The nightmare sheds bright light in a 10-foot radius and dim light for an additional 10 feet."""
        return 'The nightmare can grant resistance to fire damage to anyone riding it.Illumination. The nightmare sheds bright light in a 10-foot radius and dim light for an additional 10 feet.'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage plus 7 (2d6) fire damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) bludgeoning damage plus 7 (2d6) fire damage.'

    def ethereal_stride_attack(self) -> str:
        """The nightmare and up to three willing creatures within 5 feet of it magically enter the Ethereal Plane from the Material Plane, or vice versa."""
        return 'The nightmare and up to three willing creatures within 5 feet of it magically enter the Ethereal Plane from the Material Plane, or vice versa.'

