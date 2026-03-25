# bases1/swarm-of-rats.py
"""
SwarmOfRats creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-rats
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfRats(GlobalCreatureBaseClass):
    """
    Medium swarm of Tiny beasts creature - SwarmOfRats
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 24, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 11, 'CON': 9, 'INT': 2, 'WIS': 10, 'CHAR': 3, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  24 (7d8 - 7) Speed  30 ft. STR 9 (-1) DEX 11 (+0) CON 9 (-1) INT 2 (-4) WIS 10 (+0) CHA 3 (-4) Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'swarm of Tiny beasts', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'bites']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The swarm has advantage on Wisdom (Perception) checks that rely on smell.Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough fo"""
        return "The swarm has advantage on Wisdom (Perception) checks that rely on smell.Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough fo"

    def bites_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 0 ft., one target in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer."""
        return "Melee Weapon Attack: +2 to hit, reach 0 ft., one target in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer."

