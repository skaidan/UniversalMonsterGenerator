# bases1/azer.py
"""
Azer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=azer
"""
from creature_base import GlobalCreatureBaseClass


class Azer(GlobalCreatureBaseClass):
    """
    Medium elemental creature - Azer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 15, 'INT': 12, 'WIS': 13, 'CHAR': 10, 'armor_class': 17, 'alignment': 'lawful neutral Armor Class  17 (natural armor', 'legendary': False, 'size': 'Medium', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['heated_body', 'warhammer']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def heated_body(self) -> str:
        """A creature that touches the azer or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage.Heated Weapons. When the azer hits with a metal melee weapon, it deals an extra 3 ("""
        return 'A creature that touches the azer or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage.Heated Weapons. When the azer hits with a metal melee weapon, it deals an extra 3 ('

    def warhammer_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage, or 8 (1d10 + 3) bludgeoning damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage, or 8 (1d10 + 3) bludgeoning damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage.'

