# bases1/wood-woad.py
"""
WoodWoad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wood-woad
"""
from creature_base import GlobalCreatureBaseClass


class WoodWoad(GlobalCreatureBaseClass):
    """
    Medium Plant creature - WoodWoad
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 12, 'CON': 16, 'INT': 10, 'WIS': 13, 'CHAR': 8, 'armor_class': 18, 'alignment': 'typically Lawful Neutral Armor Class  18 (natural armor', 'legendary': False, 'size': 'Medium', 'type': 'Plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['plant_camouflage', 'multiattack', 'club']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def plant_camouflage(self) -> str:
        """The wood woad has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring vegetation.Regeneration. The wood woad regains 10 hit points at the start of its turn if it is in"""
        return 'The wood woad has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring vegetation.Regeneration. The wood woad regains 10 hit points at the start of its turn if it is in'

    def multiattack_attack(self) -> str:
        """The wood woad makes two Club attacks."""
        return 'The wood woad makes two Club attacks.'

    def club_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (4d4 + 4) force damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (4d4 + 4) force damage.'

