# bases1/lich.py
"""
Lich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lich
"""
from creature_base import GlobalCreatureBaseClass


class Lich(GlobalCreatureBaseClass):
    """
    Medium undead creature - Lich
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 135, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 16, 'CON': 16, 'INT': 20, 'WIS': 14, 'CHAR': 16, 'armor_class': 17, 'alignment': 'any evil alignment Armor Class  17 (natural armor) Hit Points  135 (18d8 + 54) Speed  30 ft. STR 11 (+0) DEX 16 (+3) CON 16 (+3) INT 20 (+5) WIS 14 (+2) CHA 16 (+3) Saving Throws  Con +10', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(3/day)', 'paralyzing_touch']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(3/day)(self) -> str:
        """If the lich fails a saving throw, it can choose to succeed instead.Rejuvenation. If it has a phylactery, a destroyed lich gains a new body in 1d10 days, regaining all its hit points and becoming activ"""
        return 'If the lich fails a saving throw, it can choose to succeed instead.Rejuvenation. If it has a phylactery, a destroyed lich gains a new body in 1d10 days, regaining all its hit points and becoming activ'

    def paralyzing_touch_attack(self) -> str:
        """Melee Spell Attack: +12 to hit, reach 5 ft., one creature. Hit: 10 (3d6) cold damage. The target must succeed on a DC 18 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Spell Attack: +12 to hit, reach 5 ft., one creature. Hit: 10 (3d6) cold damage. The target must succeed on a DC 18 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

