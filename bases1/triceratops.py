# bases1/triceratops.py
"""
Triceratops creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=triceratops
"""
from creature_base import GlobalCreatureBaseClass


class Triceratops(GlobalCreatureBaseClass):
    """
    Huge beast creature - Triceratops
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 95, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 9, 'CON': 17, 'INT': 2, 'WIS': 11, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  95 (10d12 + 30) Speed  50 ft. STR 22 (+6) DEX 9 (-1) CON 17 (+3) INT 2 (-4) WIS 11 (+0) CHA 5 (-3) Senses  passive Perception 10 Languages  — Challenge  5 (1800 XP) Trampling Charge . If the triceratops moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['trampling_charge', 'gore', 'stomp']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def trampling_charge(self) -> str:
        """If the triceratops moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone"""
        return 'If the triceratops moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone'

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 24 (4d8 + 6) piercing damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 24 (4d8 + 6) piercing damage.'

    def stomp_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one prone creature. Hit: 22 (3d10 + 6) bludgeoning damage"""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one prone creature. Hit: 22 (3d10 + 6) bludgeoning damage'

