# bases1/barlgura.py
"""
Barlgura creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=barlgura
"""
from creature_base import GlobalCreatureBaseClass


class Barlgura(GlobalCreatureBaseClass):
    """
    Large fiend (Demon) creature - Barlgura
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 7, 'WIS': 14, 'CHAR': 9, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (natural armor) Hit Points  68 (8d10 + 24) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'multiattack', 'bite', 'fist']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The barlgura's spellcasting ability is Wisdom (spell save DC 13). The barlgura can innately cast the following spells, requiring no material components:1/day each: entangle, phantasmal force2/day each"""
        return "The barlgura's spellcasting ability is Wisdom (spell save DC 13). The barlgura can innately cast the following spells, requiring no material components:1/day each: entangle, phantasmal force2/day each"

    def multiattack_attack(self) -> str:
        """The barlgura makes three attacks: one with its bite and two with its fists."""
        return 'The barlgura makes three attacks: one with its bite and two with its fists.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) bludgeoning damage.'

