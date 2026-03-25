# bases1/young-blue-dragon.py
"""
YoungBlueDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-blue-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungBlueDragon(GlobalCreatureBaseClass):
    """
    Large dragon (Chromatic) creature - YoungBlueDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 152, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 10, 'CON': 19, 'INT': 14, 'WIS': 13, 'CHAR': 17, 'armor_class': 18, 'alignment': 'lawful evil Armor Class  18 (natural armor) Hit Points  152 (16d10 + 64) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'claw', 'lightning_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The dragon makes three attacks: one with its bite and two with its claws."""
        return 'The dragon makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) piercing damage plus 5 (1d10) lightning damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) piercing damage plus 5 (1d10) lightning damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage.'

    def lightning_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales lightning in an 60-foot line that is 5 feet wide. Each creature in that line must make a DC 16 Dexterity saving throw, taking 55 (10d10) lightning damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales lightning in an 60-foot line that is 5 feet wide. Each creature in that line must make a DC 16 Dexterity saving throw, taking 55 (10d10) lightning damage on a failed save, or half as much damage on a successful one.'

