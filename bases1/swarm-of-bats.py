# bases1/swarm-of-bats.py
"""
SwarmOfBats creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-bats
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfBats(GlobalCreatureBaseClass):
    """
    Medium swarm of Tiny beasts creature - SwarmOfBats
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 5, 'DEX': 15, 'CON': 10, 'INT': 2, 'WIS': 12, 'CHAR': 4, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  22 (5d8) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'swarm of Tiny beasts', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['echolocation', 'bites']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def echolocation(self) -> str:
        """The swarm can't use its blindsight while deafened.Keen Hearing. The swarm has advantage on Wisdom (Perception) checks that rely on hearing.Swarm. The swarm can occupy another creature's space and vice"""
        return "The swarm can't use its blindsight while deafened.Keen Hearing. The swarm has advantage on Wisdom (Perception) checks that rely on hearing.Swarm. The swarm can occupy another creature's space and vice"

    def bites_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 0 ft., one creature in the swarm's space. Hit: 5 (2d4) piercing damage, or 2 (1d4) piercing damage if the swarm has half of its hit points or fewer."""
        return "Melee Weapon Attack: +4 to hit, reach 0 ft., one creature in the swarm's space. Hit: 5 (2d4) piercing damage, or 2 (1d4) piercing damage if the swarm has half of its hit points or fewer."

