# bases1/illusionist-wizard.py
"""
IllusionistWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=illusionist-wizard
"""
from creature_base import GlobalCreatureBaseClass


class IllusionistWizard(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - IllusionistWizard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 44, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 13, 'INT': 16, 'WIS': 11, 'CHAR': 12, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  44 (8d8 + 8) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 13 (+1) INT 16 (+3) WIS 11 (+0) CHA 12 (+1) Saving Throws  Int +5', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'arcane_burst', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The illusionist makes two Arcane Burst attacks."""
        return 'The illusionist makes two Arcane Burst attacks.'

    def arcane_burst_attack(self) -> str:
        """Melee or Ranged Spell Attack: +5 to hit, reach 5 ft. or range 120 ft., one target. Hit: 14 (2d10 + 3) psychic damage."""
        return 'Melee or Ranged Spell Attack: +5 to hit, reach 5 ft. or range 120 ft., one target. Hit: 14 (2d10 + 3) psychic damage.'

    def spellcasting_attack(self) -> str:
        """The illusionist casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 13):"""
        return 'The illusionist casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 13):'

