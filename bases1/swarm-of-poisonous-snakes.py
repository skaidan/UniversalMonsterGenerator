# bases1/swarm-of-poisonous-snakes.py
"""
SwarmOfPoisonousSnakes creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-poisonous-snakes
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfPoisonousSnakes(GlobalCreatureBaseClass):
    """
    Medium swarm of Tiny beasts creature - SwarmOfPoisonousSnakes
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 36, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 18, 'CON': 11, 'INT': 1, 'WIS': 10, 'CHAR': 3, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 Hit Points  36 (8d8) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'swarm of Tiny beasts', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['swarm', 'bites']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def swarm(self) -> str:
        """The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny snake. The swarm can't regain hit points or gain temporary hit points."""
        return "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny snake. The swarm can't regain hit points or gain temporary hit points."

    def bites_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 0 ft., one creature in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer. The target must make a DC 10 Constitution saving throw, taking 14 (4d6) poison damage on a failed save, or half as much damage on a successful one."""
        return "Melee Weapon Attack: +6 to hit, reach 0 ft., one creature in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer. The target must make a DC 10 Constitution saving throw, taking 14 (4d6) poison damage on a failed save, or half as much damage on a successful one."

