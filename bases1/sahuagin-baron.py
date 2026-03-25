# bases1/sahuagin-baron.py
"""
SahuaginBaron creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sahuagin-baron
"""
from creature_base import GlobalCreatureBaseClass


class SahuaginBaron(GlobalCreatureBaseClass):
    """
    Large humanoid (Sahuagin) creature - SahuaginBaron
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 76, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 15, 'CON': 16, 'INT': 14, 'WIS': 13, 'CHAR': 17, 'armor_class': 16, 'alignment': 'lawful evil Armor Class  16 (breastplate) Hit Points  76 (9d10 + 27) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'humanoid (Sahuagin)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['blood_frenzy', 'multiattack', 'bite', 'claws', 'trident']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def blood_frenzy(self) -> str:
        """The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.Limited Amphibiousness. The sahuagin can breathe air and water, but he needs to be submerged """
        return "The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.Limited Amphibiousness. The sahuagin can breathe air and water, but he needs to be submerged "

    def multiattack_attack(self) -> str:
        """The sahuagin makes three attacks: one with his bite and two with his claws or trident."""
        return 'The sahuagin makes three attacks: one with his bite and two with his claws or trident.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.'

    def trident_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack.'

