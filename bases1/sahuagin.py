# bases1/sahuagin.py
"""
Sahuagin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sahuagin
"""
from creature_base import GlobalCreatureBaseClass


class Sahuagin(GlobalCreatureBaseClass):
    """
    Medium humanoid (Sahuagin) creature - Sahuagin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 11, 'CON': 12, 'INT': 12, 'WIS': 13, 'CHAR': 9, 'armor_class': 12, 'alignment': 'lawful evil Armor Class  12 (natural armor) Hit Points  22 (4d8 + 4) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Sahuagin)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['blood_frenzy', 'multiattack', 'bite', 'claws', 'spear']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def blood_frenzy(self) -> str:
        """The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.Limited Amphibiousness. The sahuagin can breathe air and water, but it needs to be submerged """
        return "The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.Limited Amphibiousness. The sahuagin can breathe air and water, but it needs to be submerged "

    def multiattack_attack(self) -> str:
        """The sahuagin makes two melee attacks: one with its bite and one with its claws or spear."""
        return 'The sahuagin makes two melee attacks: one with its bite and one with its claws or spear.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) slashing damage.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.'

