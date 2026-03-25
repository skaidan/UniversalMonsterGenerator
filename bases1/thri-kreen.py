# bases1/thri-kreen.py
"""
ThriKreen creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=thri-kreen
"""
from creature_base import GlobalCreatureBaseClass


class ThriKreen(GlobalCreatureBaseClass):
    """
    Medium humanoid (Thri-kreen) creature - ThriKreen
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 15, 'CON': 13, 'INT': 8, 'WIS': 12, 'CHAR': 7, 'armor_class': 15, 'alignment': 'chaotic neutral Armor Class  15 (natural armor) Hit Points  33 (6d8 + 6) Speed  40 ft. STR 12 (+1) DEX 15 (+2) CON 13 (+1) INT 8 (-1) WIS 12 (+1) CHA 7 (-2) Skills  Perception +3', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Thri-kreen)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['chameleon_carapace', 'multiattack', 'bite', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def chameleon_carapace(self) -> str:
        """The thri-kreen can change the color of its carapace to match the color and texture of its surroundings. As a result, it has advantage on Dexterity (Stealth) checks made to hide.Standing Leap. The thri"""
        return 'The thri-kreen can change the color of its carapace to match the color and texture of its surroundings. As a result, it has advantage on Dexterity (Stealth) checks made to hide.Standing Leap. The thri'

    def multiattack_attack(self) -> str:
        """The thri-kreen makes two attacks: one with its bite and one with its claws."""
        return 'The thri-kreen makes two attacks: one with its bite and one with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or be poisoned for 1 minute. If the saving throw fails by 5 or more, the target is also paralyzed while poisoned in this way. The poisoned target can repeat the saving throw on each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 4 (1d6 + 1) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or be poisoned for 1 minute. If the saving throw fails by 5 or more, the target is also paralyzed while poisoned in this way. The poisoned target can repeat the saving throw on each of its turns, ending the effect on itself on a success.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage.'

