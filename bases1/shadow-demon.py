# bases1/shadow-demon.py
"""
ShadowDemon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shadow-demon
"""
from creature_base import GlobalCreatureBaseClass


class ShadowDemon(GlobalCreatureBaseClass):
    """
    Medium fiend (Demon) creature - ShadowDemon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 66, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 17, 'CON': 12, 'INT': 14, 'WIS': 13, 'CHAR': 14, 'armor_class': 13, 'alignment': 'chaotic evil Armor Class  13 Hit Points  66 (12d8 + 12) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['incorporeal_movement', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def incorporeal_movement(self) -> str:
        """The demon can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Light Sensitivity. While in bright light, """
        return 'The demon can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Light Sensitivity. While in bright light, '

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 10 (2d6 + 3) psychic damage or, if the demon had advantage on the attack roll, 17 (4d6 + 3) psychic damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 10 (2d6 + 3) psychic damage or, if the demon had advantage on the attack roll, 17 (4d6 + 3) psychic damage.'

