# bases1/basilisk.py
"""
Basilisk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=basilisk
"""
from creature_base import GlobalCreatureBaseClass


class Basilisk(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - Basilisk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 8, 'CON': 15, 'INT': 2, 'WIS': 8, 'CHAR': 7, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  52 (8d8 + 16) Speed  20 ft. STR 16 (+3) DEX 8 (-1) CON 15 (+2) INT 2 (-4) WIS 8 (-1) CHA 7 (-2) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['petrifying_gaze', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def petrifying_gaze(self) -> str:
        """If a creature starts its turn within 30 feet of the basilisk and the two of them can see each other, the basilisk can force the creature to make a DC 12 Constitution saving throw if the basilisk isn't"""
        return "If a creature starts its turn within 30 feet of the basilisk and the two of them can see each other, the basilisk can force the creature to make a DC 12 Constitution saving throw if the basilisk isn't"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage plus 7 (2d6) poison damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage plus 7 (2d6) poison damage.'

