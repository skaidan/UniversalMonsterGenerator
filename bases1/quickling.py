# bases1/quickling.py
"""
Quickling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quickling
"""
from creature_base import GlobalCreatureBaseClass


class Quickling(GlobalCreatureBaseClass):
    """
    Tiny Fey creature - Quickling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 4, 'DEX': 23, 'CON': 13, 'INT': 10, 'WIS': 12, 'CHAR': 7, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 Hit Points  10 (3d4 + 3) Speed  120 ft. STR 4 (-3) DEX 23 (+6) CON 13 (+1) INT 10 (+0) WIS 12 (+1) CHA 7 (-2) Skills  Acrobatics +8', 'legendary': False, 'size': 'Tiny', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['blurred_movement', 'multiattack', 'dagger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def blurred_movement(self) -> str:
        """Attack rolls against the quickling have disadvantage unless it is incapacitated or its speed is 0.Evasion. If the quickling is subjected to an effect that allows it to make a Dexterity saving throw to"""
        return 'Attack rolls against the quickling have disadvantage unless it is incapacitated or its speed is 0.Evasion. If the quickling is subjected to an effect that allows it to make a Dexterity saving throw to'

    def multiattack_attack(self) -> str:
        """The quickling makes three Dagger attacks."""
        return 'The quickling makes three Dagger attacks.'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +8 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 8 (1d4 + 6) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +8 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 8 (1d4 + 6) piercing damage.'

