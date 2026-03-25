# bases1/swarm-of-insects.py
"""
SwarmOfInsects creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-insects
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfInsects(GlobalCreatureBaseClass):
    """
    Medium swarm of Tiny beasts creature - SwarmOfInsects
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 13, 'CON': 10, 'INT': 1, 'WIS': 7, 'CHAR': 1, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  22 (5d8) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'swarm of Tiny beasts', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['swarm', 'bites']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def swarm(self) -> str:
        """The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points."""
        return "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points."

    def bites_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 0 ft., one target in the swarm's space. Hit: 10 (4d4) piercing damage, or 5 (2d4) piercing damage if the swarm has half of its hit points or fewer."""
        return "Melee Weapon Attack: +3 to hit, reach 0 ft., one target in the swarm's space. Hit: 10 (4d4) piercing damage, or 5 (2d4) piercing damage if the swarm has half of its hit points or fewer."

