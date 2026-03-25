# bases1/stone-giant.py
"""
StoneGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-giant
"""
from creature_base import GlobalCreatureBaseClass


class StoneGiant(GlobalCreatureBaseClass):
    """
    Huge giant creature - StoneGiant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 126, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 15, 'CON': 20, 'INT': 10, 'WIS': 12, 'CHAR': 9, 'armor_class': 17, 'alignment': 'neutral Armor Class  17 (natural armor) Hit Points  126 (11d12 + 55) Speed  40 ft. STR 23 (+6) DEX 15 (+2) CON 20 (+5) INT 10 (+0) WIS 12 (+1) CHA 9 (-1) Saving Throws  Dex +5', 'legendary': False, 'size': 'Huge', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['stone_camouflage', 'multiattack', 'greatclub', 'rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def stone_camouflage(self) -> str:
        """The giant has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."""
        return 'The giant has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.'

    def multiattack_attack(self) -> str:
        """The giant makes two greatclub attacks."""
        return 'The giant makes two greatclub attacks.'

    def greatclub_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +9 to hit, range 60/240 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage. If the target is a creature, it must succeed on a DC 17 Strength saving throw or be knocked prone."""
        return 'Ranged Weapon Attack: +9 to hit, range 60/240 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage. If the target is a creature, it must succeed on a DC 17 Strength saving throw or be knocked prone.'

