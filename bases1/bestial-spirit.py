# bases1/bestial-spirit.py
"""
BestialSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bestial-spirit
"""
from creature_base import GlobalCreatureBaseClass


class BestialSpirit(GlobalCreatureBaseClass):
    """
    Small beast creature - BestialSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 20, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 11, 'CON': 16, 'INT': 4, 'WIS': 14, 'CHAR': 5, 'armor_class': 11, 'alignment': '- Armor Class  11 + the level of the spell (natural armor) Hit Points  20 (Air only) or 30 (Land and Water only) + 5 for each spell level above 2nd Speed  30 ft.; climb 30 ft. (Land only); fly 60 ft. (Air only); swim 30 ft. (Water only) STR 18 (+4) DEX 11 (+0) CON 16 (+3) INT 4 (-3) WIS 14 (+2) CHA 5 (-3) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['flyby_(air_only)', 'multiattack', 'maul']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def flyby_(air_only)(self) -> str:
        """The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach.Pack Tactics (Land and Water Only). The beast has advantage on an attack roll against a creature if at least one of """
        return "The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach.Pack Tactics (Land and Water Only). The beast has advantage on an attack roll against a creature if at least one of "

    def multiattack_attack(self) -> str:
        """The beast makes a number of attacks equal to half this spell's level (rounded down)."""
        return "The beast makes a number of attacks equal to half this spell's level (rounded down)."

    def maul_attack(self) -> str:
        """Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target. Hit: 1d8 + 4 + the spell's level piercing damage."""
        return "Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target. Hit: 1d8 + 4 + the spell's level piercing damage."

