# bases1/derro.py
"""
Derro creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=derro
"""
from creature_base import GlobalCreatureBaseClass


class Derro(GlobalCreatureBaseClass):
    """
    Small Aberration creature - Derro
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 12, 'INT': 11, 'WIS': 5, 'CHAR': 9, 'armor_class': 13, 'alignment': 'typically Chaotic Evil Armor Class  13 (leather armor) Hit Points  13 (3d6 + 3) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 12 (+1) INT 11 (+0) WIS 5 (-3) CHA 9 (-1) Skills  Stealth +4 Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Small', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'hooked_spear', 'light_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The derro has advantage on saving throws against spells and other magical effects.Sunlight Sensitivity. While in sunlight, the derro has disadvantage on attack rolls, as well as on Wisdom (Perception)"""
        return 'The derro has advantage on saving throws against spells and other magical effects.Sunlight Sensitivity. While in sunlight, the derro has disadvantage on attack rolls, as well as on Wisdom (Perception)'

    def hooked_spear_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage. If the target is Medium or smaller, the derro can choose to deal no damage and knock it prone."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage. If the target is Medium or smaller, the derro can choose to deal no damage and knock it prone.'

    def light_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

