# bases1/swarm-of-quippers.py
"""
SwarmOfQuippers creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-quippers
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfQuippers(GlobalCreatureBaseClass):
    """
    Medium swarm of Tiny beasts creature - SwarmOfQuippers
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 28, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 16, 'CON': 9, 'INT': 1, 'WIS': 7, 'CHAR': 2, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  28 (8d8 - 8) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'swarm of Tiny beasts', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['blood_frenzy', 'bites']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def blood_frenzy(self) -> str:
        """The swarm has advantage on melee attack rolls against any creature that doesn't have all its hit points.Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move thro"""
        return "The swarm has advantage on melee attack rolls against any creature that doesn't have all its hit points.Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move thro"

    def bites_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 0 ft., one creature in the swarm's space. Hit: 14 (4d6) piercing damage, or 7 (2d6) piercing damage if the swarm has half of its hit points or fewer."""
        return "Melee Weapon Attack: +5 to hit, reach 0 ft., one creature in the swarm's space. Hit: 14 (4d6) piercing damage, or 7 (2d6) piercing damage if the swarm has half of its hit points or fewer."

