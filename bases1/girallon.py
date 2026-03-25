# bases1/girallon.py
"""
Girallon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=girallon
"""
from creature_base import GlobalCreatureBaseClass


class Girallon(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - Girallon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 59, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 16, 'CON': 16, 'INT': 5, 'WIS': 12, 'CHAR': 7, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  59 (7d10 + 21) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The girallon makes one Bite attack and four Claw attacks."""
        return 'The girallon makes one Bite attack and four Claw attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 7 (1d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 7 (1d6 + 4) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 7 (1d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 7 (1d6 + 4) slashing damage.'

