# bases1/ghast.py
"""
Ghast creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ghast
"""
from creature_base import GlobalCreatureBaseClass


class Ghast(GlobalCreatureBaseClass):
    """
    Medium undead creature - Ghast
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 36, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 17, 'CON': 10, 'INT': 11, 'WIS': 10, 'CHAR': 8, 'armor_class': 13, 'alignment': 'chaotic evil Armor Class  13 Hit Points  36 (8d8) Speed  30 ft. STR 16 (+3) DEX 17 (+3) CON 10 (+0) INT 11 (+0) WIS 10 (+0) CHA 8 (-1) Damage Resistances  necrotic Damage Immunities  poison Condition Immunities  charmed', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['stench', 'bite', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def stench(self) -> str:
        """Any creature that starts its turn within 5 feet of the ghast must succeed on a DC 10 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creatu"""
        return 'Any creature that starts its turn within 5 feet of the ghast must succeed on a DC 10 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creatu'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 12 (2d8 + 3) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 12 (2d8 + 3) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage. If the target is a creature other than an undead, it must succeed on a DC 10 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage. If the target is a creature other than an undead, it must succeed on a DC 10 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

