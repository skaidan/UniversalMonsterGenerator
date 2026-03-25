# bases1/sahuagin-priestess.py
"""
SahuaginPriestess creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sahuagin-priestess
"""
from creature_base import GlobalCreatureBaseClass


class SahuaginPriestess(GlobalCreatureBaseClass):
    """
    Medium humanoid (Sahuagin) creature - SahuaginPriestess
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 11, 'CON': 12, 'INT': 12, 'WIS': 14, 'CHAR': 13, 'armor_class': 12, 'alignment': 'lawful evil Armor Class  12 (natural armor) Hit Points  33 (6d8 + 6) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Sahuagin)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['blood_frenzy', 'multiattack', 'bite', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def blood_frenzy(self) -> str:
        """The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.Limited Amphibiousness. The sahuagin can breathe air and water, but she needs to be submerged"""
        return "The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.Limited Amphibiousness. The sahuagin can breathe air and water, but she needs to be submerged"

    def multiattack_attack(self) -> str:
        """The sahuagin makes two attacks: one with her bite and one with her claws."""
        return 'The sahuagin makes two attacks: one with her bite and one with her claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) slashing damage.'

