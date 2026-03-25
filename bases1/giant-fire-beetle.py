# bases1/giant-fire-beetle.py
"""
GiantFireBeetle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-fire-beetle
"""
from creature_base import GlobalCreatureBaseClass


class GiantFireBeetle(GlobalCreatureBaseClass):
    """
    Small beast creature - GiantFireBeetle
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 4, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 10, 'CON': 12, 'INT': 1, 'WIS': 7, 'CHAR': 3, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  4 (1d6 + 1) Speed  30 ft. STR 8 (-1) DEX 10 (+0) CON 12 (+1) INT 1 (-5) WIS 7 (-2) CHA 3 (-4) Senses  blindsight 30 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['illumination', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def illumination(self) -> str:
        """The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 feet."""
        return 'The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 feet.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) slashing damage."""
        return 'Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) slashing damage.'

