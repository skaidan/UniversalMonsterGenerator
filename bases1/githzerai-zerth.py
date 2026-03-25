# bases1/githzerai-zerth.py
"""
GithzeraiZerth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githzerai-zerth
"""
from creature_base import GlobalCreatureBaseClass


class GithzeraiZerth(GlobalCreatureBaseClass):
    """
    Medium humanoid (Gith) creature - GithzeraiZerth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 84, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 18, 'CON': 15, 'INT': 16, 'WIS': 17, 'CHAR': 12, 'armor_class': 17, 'alignment': 'lawful neutral Armor Class  17 Hit Points  84 (13d8 + 26) Speed  30 ft. STR 13 (+1) DEX 18 (+4) CON 15 (+2) INT 16 (+3) WIS 17 (+3) CHA 12 (+1) Saving Throws  Str +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Gith)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting_(psionics)', 'multiattack', 'unarmed_strike']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting_(psionics)(self) -> str:
        """The githzerai's innate spellcasting ability is Wisdom. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: feather fall, jump, see """
        return "The githzerai's innate spellcasting ability is Wisdom. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: feather fall, jump, see "

    def multiattack_attack(self) -> str:
        """The githzerai makes two unarmed strikes."""
        return 'The githzerai makes two unarmed strikes.'

    def unarmed_strike_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage plus 13 (3d8) psychic damage. This is a magic weapon attack."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage plus 13 (3d8) psychic damage. This is a magic weapon attack.'

