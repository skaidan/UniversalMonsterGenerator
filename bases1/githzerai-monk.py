# bases1/githzerai-monk.py
"""
GithzeraiMonk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githzerai-monk
"""
from creature_base import GlobalCreatureBaseClass


class GithzeraiMonk(GlobalCreatureBaseClass):
    """
    Medium humanoid (Gith) creature - GithzeraiMonk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 38, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 15, 'CON': 12, 'INT': 13, 'WIS': 14, 'CHAR': 10, 'armor_class': 14, 'alignment': 'lawful neutral Armor Class  14 Hit Points  38 (7d8 + 7) Speed  30 ft. STR 12 (+1) DEX 15 (+2) CON 12 (+1) INT 13 (+1) WIS 14 (+2) CHA 10 (+0) Saving Throws  Str +3', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Gith)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting_(psionics)', 'multiattack', 'unarmed_strike']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting_(psionics)(self) -> str:
        """The githzerai's innate spellcasting ability is Wisdom. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: feather fall, jump, see """
        return "The githzerai's innate spellcasting ability is Wisdom. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: feather fall, jump, see "

    def multiattack_attack(self) -> str:
        """The githzerai makes two unarmed strikes."""
        return 'The githzerai makes two unarmed strikes.'

    def unarmed_strike_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage plus 9 (2d8) psychic damage. This is a magic weapon attack."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage plus 9 (2d8) psychic damage. This is a magic weapon attack.'

