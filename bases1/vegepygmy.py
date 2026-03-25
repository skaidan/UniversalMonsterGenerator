# bases1/vegepygmy.py
"""
Vegepygmy creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vegepygmy
"""
from creature_base import GlobalCreatureBaseClass


class Vegepygmy(GlobalCreatureBaseClass):
    """
    Small Plant creature - Vegepygmy
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 14, 'CON': 13, 'INT': 6, 'WIS': 11, 'CHAR': 7, 'armor_class': 13, 'alignment': 'typically Neutral Armor Class  13 (natural armor) Hit Points  13 (3d6 + 3) Speed  30 ft. STR 7 (-2) DEX 14 (+2) CON 13 (+1) INT 6 (-2) WIS 11 (+0) CHA 7 (-2) Skills  Perception +2', 'legendary': False, 'size': 'Small', 'type': 'Plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['plant_camouflage', 'claws', 'sling']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def plant_camouflage(self) -> str:
        """The vegepygmy has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring vegetation.Regeneration. The vegepygmy regains 3 hit points at the start of its turn. If it takes"""
        return 'The vegepygmy has advantage on Dexterity (Stealth) checks it makes in any terrain with ample obscuring vegetation.Regeneration. The vegepygmy regains 3 hit points at the start of its turn. If it takes'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.'

    def sling_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.'

