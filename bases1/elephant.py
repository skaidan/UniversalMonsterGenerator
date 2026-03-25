# bases1/elephant.py
"""
Elephant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=elephant
"""
from creature_base import GlobalCreatureBaseClass


class Elephant(GlobalCreatureBaseClass):
    """
    Huge beast creature - Elephant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 76, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 9, 'CON': 17, 'INT': 3, 'WIS': 11, 'CHAR': 6, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  76 (8d12 + 24) Speed  40 ft. STR 22 (+6) DEX 9 (-1) CON 17 (+3) INT 3 (-4) WIS 11 (+0) CHA 6 (-2) Senses  passive Perception 10 Languages  — Challenge  4 (1100 XP) Trampling Charge . If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['trampling_charge', 'gore', 'stomp']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def trampling_charge(self) -> str:
        """If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. I"""
        return 'If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. I'

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) piercing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) piercing damage.'

    def stomp_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one prone creature. Hit: 22 (3d10 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one prone creature. Hit: 22 (3d10 + 6) bludgeoning damage.'

