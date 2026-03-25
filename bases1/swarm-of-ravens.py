# bases1/swarm-of-ravens.py
"""
SwarmOfRavens creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-ravens
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfRavens(GlobalCreatureBaseClass):
    """
    Medium swarm of Tiny beasts creature - SwarmOfRavens
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 24, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 14, 'CON': 8, 'INT': 3, 'WIS': 12, 'CHAR': 6, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  24 (7d8 - 7) Speed  10 ft.', 'legendary': False, 'size': 'Medium', 'type': 'swarm of Tiny beasts', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['swarm', 'beaks']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def swarm(self) -> str:
        """The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny raven. The swarm can't regain hit points or gain temporary hit points."""
        return "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny raven. The swarm can't regain hit points or gain temporary hit points."

    def beaks_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one target in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer."

