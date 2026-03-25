# bases1/drow-house-captain.py
"""
DrowHouseCaptain creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-house-captain
"""
from creature_base import GlobalCreatureBaseClass


class DrowHouseCaptain(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Elf) creature - DrowHouseCaptain
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 162, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 19, 'CON': 15, 'INT': 12, 'WIS': 14, 'CHAR': 13, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (chain mail) Hit Points  162 (25d8 + 50) Speed  30 ft. STR 14 (+2) DEX 19 (+4) CON 15 (+2) INT 12 (+1) WIS 14 (+2) CHA 13 (+1) Saving Throws  Dex +8', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'multiattack', 'scimitar', 'whip', 'hand_crossbow', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in sunlight, the drow has disadvantage on attack rolls, as well as on W"""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in sunlight, the drow has disadvantage on attack rolls, as well as on W"

    def multiattack_attack(self) -> str:
        """The drow makes two Scimitar attacks and one Whip or Hand Crossbow attack."""
        return 'The drow makes two Scimitar attacks and one Whip or Hand Crossbow attack.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage plus 14 (4d6) poison damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage plus 14 (4d6) poison damage.'

    def whip_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 6 (1d4 + 4) slashing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 6 (1d4 + 4) slashing damage.'

    def hand_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +8 to hit, range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target regains consciousness if it takes damage or if another creature takes an action to shake it."""
        return 'Ranged Weapon Attack: +8 to hit, range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target regains consciousness if it takes damage or if another creature takes an action to shake it.'

    def spellcasting_attack(self) -> str:
        """The drow casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 13):"""
        return 'The drow casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 13):'

