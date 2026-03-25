# bases1/conjurer-wizard.py
"""
ConjurerWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=conjurer-wizard
"""
from creature_base import GlobalCreatureBaseClass


class ConjurerWizard(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - ConjurerWizard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 11, 'INT': 17, 'WIS': 12, 'CHAR': 11, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  58 (13d8) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 11 (+0) INT 17 (+3) WIS 12 (+1) CHA 11 (+0) Saving Throws  Int +6', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'arcane_burst', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The conjurer makes three Arcane Burst attacks."""
        return 'The conjurer makes three Arcane Burst attacks.'

    def arcane_burst_attack(self) -> str:
        """Melee or Ranged Spell Attack: +8 to hit, reach 5 ft. or range 120 ft., one target. Hit: 19 (3d10 + 3) force damage."""
        return 'Melee or Ranged Spell Attack: +8 to hit, reach 5 ft. or range 120 ft., one target. Hit: 19 (3d10 + 3) force damage.'

    def spellcasting_attack(self) -> str:
        """The conjurer casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 14):"""
        return 'The conjurer casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 14):'

