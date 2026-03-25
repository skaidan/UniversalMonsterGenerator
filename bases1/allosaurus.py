# bases1/allosaurus.py
"""
Allosaurus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=allosaurus
"""
from creature_base import GlobalCreatureBaseClass


class Allosaurus(GlobalCreatureBaseClass):
    """
    Large beast creature - Allosaurus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 51, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 13, 'CON': 17, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  51 (6d10 + 18) Speed  60 ft. STR 19 (+4) DEX 13 (+1) CON 17 (+3) INT 2 (-4) WIS 12 (+1) CHA 5 (-3) Skills  Perception +5 Senses  passive Perception 15 Languages  — Challenge  2 (450 XP) Pounce . If the allosaurus moves at least 30 feet straight toward a creature and then hits it with a claw attack on the same turn', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pounce', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pounce(self) -> str:
        """If the allosaurus moves at least 30 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone."""
        return 'If the allosaurus moves at least 30 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 15 (2d10 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 15 (2d10 + 4) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage.'

