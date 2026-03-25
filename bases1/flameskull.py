# bases1/flameskull.py
"""
Flameskull creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flameskull
"""
from creature_base import GlobalCreatureBaseClass


class Flameskull(GlobalCreatureBaseClass):
    """
    Tiny undead creature - Flameskull
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 40, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 17, 'CON': 14, 'INT': 16, 'WIS': 10, 'CHAR': 11, 'armor_class': 13, 'alignment': 'neutral evil Armor Class  13 Hit Points  40 (9d4 + 18) Speed  0 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['illumination', 'multiattack', 'fire_ray']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def illumination(self) -> str:
        """The flameskull sheds either dim light in a 15-foot radius, or bright light in a 15-foot radius and dim light for an additional 15 feet. It can switch between the options as an action.Magic Resistance."""
        return 'The flameskull sheds either dim light in a 15-foot radius, or bright light in a 15-foot radius and dim light for an additional 15 feet. It can switch between the options as an action.Magic Resistance.'

    def multiattack_attack(self) -> str:
        """The flameskull uses Fire Ray twice."""
        return 'The flameskull uses Fire Ray twice.'

    def fire_ray_attack(self) -> str:
        """Ranged Spell Attack: +5 to hit, range 30 ft., one target. Hit: 10 (3d6) fire damage."""
        return 'Ranged Spell Attack: +5 to hit, range 30 ft., one target. Hit: 10 (3d6) fire damage.'

