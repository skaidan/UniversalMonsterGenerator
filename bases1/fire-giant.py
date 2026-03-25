# bases1/fire-giant.py
"""
FireGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-giant
"""
from creature_base import GlobalCreatureBaseClass


class FireGiant(GlobalCreatureBaseClass):
    """
    Huge giant creature - FireGiant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 162, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 9, 'CON': 23, 'INT': 10, 'WIS': 14, 'CHAR': 13, 'armor_class': 18, 'alignment': 'lawful evil Armor Class  18 (plate) Hit Points  162 (13d12 + 78) Speed  30 ft. STR 25 (+7) DEX 9 (-1) CON 23 (+6) INT 10 (+0) WIS 14 (+2) CHA 13 (+1) Saving Throws  Dex +3', 'legendary': False, 'size': 'Huge', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'greatsword', 'rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The giant makes two greatsword attacks."""
        return 'The giant makes two greatsword attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 28 (6d6 + 7) slashing damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 28 (6d6 + 7) slashing damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +11 to hit, range 60/240 ft., one target. Hit: 29 (4d10 + 7) bludgeoning damage."""
        return 'Ranged Weapon Attack: +11 to hit, range 60/240 ft., one target. Hit: 29 (4d10 + 7) bludgeoning damage.'

