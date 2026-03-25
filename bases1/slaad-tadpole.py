# bases1/slaad-tadpole.py
"""
SlaadTadpole creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=slaad-tadpole
"""
from creature_base import GlobalCreatureBaseClass


class SlaadTadpole(GlobalCreatureBaseClass):
    """
    Tiny aberration creature - SlaadTadpole
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 15, 'CON': 10, 'INT': 3, 'WIS': 5, 'CHAR': 3, 'armor_class': 12, 'alignment': 'chaotic neutral Armor Class  12 Hit Points  10 (4d4) Speed  30 ft. STR 7 (-2) DEX 15 (+2) CON 10 (+0) INT 3 (-4) WIS 5 (-3) CHA 3 (-4) Skills  Stealth +4 Damage Resistances  acid', 'legendary': False, 'size': 'Tiny', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The slaad has Advantage on saving throws against spells and other magical effects."""
        return 'The slaad has Advantage on saving throws against spells and other magical effects.'

    def bite_attack(self) -> str:
        """Melee Attack Roll: +4, reach 5 ft. Hit: 5 (1d6 + 2) Piercing damage."""
        return 'Melee Attack Roll: +4, reach 5 ft. Hit: 5 (1d6 + 2) Piercing damage.'

