# bases1/kobold-scale-sorcerer.py
"""
KoboldScaleSorcerer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kobold-scale-sorcerer
"""
from creature_base import GlobalCreatureBaseClass


class KoboldScaleSorcerer(GlobalCreatureBaseClass):
    """
    Small Humanoid creature - KoboldScaleSorcerer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 15, 'CON': 14, 'INT': 10, 'WIS': 9, 'CHAR': 14, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (natural armor) Hit Points  27 (5d6 + 10) Speed  30 ft. STR 7 (-2) DEX 15 (+2) CON 14 (+2) INT 10 (+0) WIS 9 (-1) CHA 14 (+2) Skills  Arcana +2', 'legendary': False, 'size': 'Small', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pack_tactics', 'multiattack', 'dagger', 'chromatic_bolt', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pack_tactics(self) -> str:
        """The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated.Sunlight Sensitivity. While in su"""
        return "The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated.Sunlight Sensitivity. While in su"

    def multiattack_attack(self) -> str:
        """The kobold makes two Dagger or Chromatic Bolt attacks. It can replace one attack with a use of Spellcasting."""
        return 'The kobold makes two Dagger or Chromatic Bolt attacks. It can replace one attack with a use of Spellcasting.'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

    def chromatic_bolt_attack(self) -> str:
        """Ranged Spell Attack: +4 to hit, range 60 feet, one target. Hit: 9 (2d6 + 2) of a type of the kobold's choice: acid, cold, fire, lightning, poison, or thunder."""
        return "Ranged Spell Attack: +4 to hit, range 60 feet, one target. Hit: 9 (2d6 + 2) of a type of the kobold's choice: acid, cold, fire, lightning, poison, or thunder."

    def spellcasting_attack(self) -> str:
        """The kobold casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 12):"""
        return 'The kobold casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 12):'

