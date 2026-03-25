# bases1/warhorse.py
"""
Warhorse creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warhorse
"""
from creature_base import GlobalCreatureBaseClass


class Warhorse(GlobalCreatureBaseClass):
    """
    Large beast creature - Warhorse
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 12, 'CON': 13, 'INT': 2, 'WIS': 12, 'CHAR': 7, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  19 (3d10 + 3) Speed  60 ft. STR 18 (+4) DEX 12 (+1) CON 13 (+1) INT 2 (-4) WIS 12 (+1) CHA 7 (-2) Senses  passive Perception 11 Languages  — Challenge  1/2 (100 XP) Trampling Charge . If the horse moves at least 20 feet straight toward a creature and then hits it with a hooves attack on the same turn', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['trampling_charge', 'hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def trampling_charge(self) -> str:
        """If the horse moves at least 20 feet straight toward a creature and then hits it with a hooves attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked prone. If"""
        return 'If the horse moves at least 20 feet straight toward a creature and then hits it with a hooves attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked prone. If'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

