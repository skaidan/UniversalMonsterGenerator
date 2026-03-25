# bases1/pteranodon.py
"""
Pteranodon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pteranodon
"""
from creature_base import GlobalCreatureBaseClass


class Pteranodon(GlobalCreatureBaseClass):
    """
    Medium beast creature - Pteranodon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 15, 'CON': 10, 'INT': 2, 'WIS': 9, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  13 (3d8) Speed  10 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['flyby', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def flyby(self) -> str:
        """The pteranodon doesn't provoke an opportunity attack when it flies out of an enemy's reach."""
        return "The pteranodon doesn't provoke an opportunity attack when it flies out of an enemy's reach."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage.'

