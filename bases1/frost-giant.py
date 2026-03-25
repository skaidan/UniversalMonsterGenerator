# bases1/frost-giant.py
"""
FrostGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frost-giant
"""
from creature_base import GlobalCreatureBaseClass


class FrostGiant(GlobalCreatureBaseClass):
    """
    Huge giant creature - FrostGiant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 138, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 9, 'CON': 21, 'INT': 9, 'WIS': 10, 'CHAR': 12, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (patchwork armor) Hit Points  138 (12d12 + 60) Speed  40 ft. STR 23 (+6) DEX 9 (-1) CON 21 (+5) INT 9 (-1) WIS 10 (+0) CHA 12 (+1) Saving Throws  Con +8', 'legendary': False, 'size': 'Huge', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'greataxe', 'rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The giant makes two greataxe attacks."""
        return 'The giant makes two greataxe attacks.'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 25 (3d12 + 6) slashing damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 25 (3d12 + 6) slashing damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +9 to hit, range 60/240 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage."""
        return 'Ranged Weapon Attack: +9 to hit, range 60/240 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage.'

