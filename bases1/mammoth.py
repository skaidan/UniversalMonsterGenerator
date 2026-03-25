# bases1/mammoth.py
"""
Mammoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mammoth
"""
from creature_base import GlobalCreatureBaseClass


class Mammoth(GlobalCreatureBaseClass):
    """
    Huge beast creature - Mammoth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 126, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 9, 'CON': 21, 'INT': 3, 'WIS': 11, 'CHAR': 6, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  126 (11d12 + 55) Speed  40 ft. STR 24 (+7) DEX 9 (-1) CON 21 (+5) INT 3 (-4) WIS 11 (+0) CHA 6 (-2) Senses  passive Perception 10 Languages  — Challenge  6 (2300 XP) Trampling Charge . If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['trampling_charge', 'gore', 'stomp']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def trampling_charge(self) -> str:
        """If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 18 Strength saving throw or be knocked prone. If"""
        return 'If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 18 Strength saving throw or be knocked prone. If'

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 25 (4d8 + 7) piercing damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 25 (4d8 + 7) piercing damage.'

    def stomp_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one prone creature. Hit: 29 (4d10 + 7) bludgeoning damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one prone creature. Hit: 29 (4d10 + 7) bludgeoning damage.'

