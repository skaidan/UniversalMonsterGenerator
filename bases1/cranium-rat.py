# bases1/cranium-rat.py
"""
CraniumRat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cranium-rat
"""
from creature_base import GlobalCreatureBaseClass


class CraniumRat(GlobalCreatureBaseClass):
    """
    Tiny Aberration creature - CraniumRat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 2, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 14, 'CON': 10, 'INT': 4, 'WIS': 11, 'CHAR': 8, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  2 (1d4) Speed  30 ft. STR 2 (-4) DEX 14 (+2) CON 10 (+0) INT 4 (-3) WIS 11 (+0) CHA 8 (-1) Senses  darkvision 30 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['telepathic_shroud', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def telepathic_shroud(self) -> str:
        """The cranium rat is immune to any effect that would sense its emotions or read its thoughts, as well as to all divination spells."""
        return 'The cranium rat is immune to any effect that would sense its emotions or read its thoughts, as well as to all divination spells.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 1 piercing damage.'

