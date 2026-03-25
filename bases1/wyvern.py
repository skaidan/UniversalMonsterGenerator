# bases1/wyvern.py
"""
Wyvern creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wyvern
"""
from creature_base import GlobalCreatureBaseClass


class Wyvern(GlobalCreatureBaseClass):
    """
    Large dragon creature - Wyvern
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 110, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 10, 'CON': 16, 'INT': 5, 'WIS': 12, 'CHAR': 6, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  110 (13d10 + 39) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'claws', 'stinger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The wyvern makes two attacks: one with its bite and one with its stinger. While flying, it can use its claws in place of one other attack."""
        return 'The wyvern makes two attacks: one with its bite and one with its stinger. While flying, it can use its claws in place of one other attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 11 (2d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 11 (2d6 + 4) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.'

    def stinger_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 11 (2d6 + 4) piercing damage. The target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 11 (2d6 + 4) piercing damage. The target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one.'

