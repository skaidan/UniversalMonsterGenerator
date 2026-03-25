# bases1/young-red-dragon.py
"""
YoungRedDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-red-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungRedDragon(GlobalCreatureBaseClass):
    """
    Large dragon (Chromatic) creature - YoungRedDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 178, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 10, 'CON': 21, 'INT': 14, 'WIS': 11, 'CHAR': 19, 'armor_class': 18, 'alignment': 'chaotic evil Armor Class  18 (natural armor) Hit Points  178 (17d10 + 85) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'claw', 'fire_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The dragon makes three attacks: one with its bite and two with its claws."""
        return 'The dragon makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 3 (1d6) fire damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 3 (1d6) fire damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.'

    def fire_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales fire in a 30-foot cone. Each creature in that area must make a DC 17 Dexterity saving throw, taking 56 (16d6) fire damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales fire in a 30-foot cone. Each creature in that area must make a DC 17 Dexterity saving throw, taking 56 (16d6) fire damage on a failed save, or half as much damage on a successful one.'

