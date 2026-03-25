# bases1/abjurer-wizard.py
"""
AbjurerWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=abjurer-wizard
"""
from creature_base import GlobalCreatureBaseClass


class AbjurerWizard(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - AbjurerWizard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 104, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 14, 'INT': 18, 'WIS': 12, 'CHAR': 11, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  104 (16d8 32) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 14 (+2) INT 18 (+4) WIS 12 (+1) CHA 11 (+0) Saving Throws  Int +8', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'arcane_burst', 'force_blast', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The abjurer makes three Arcane Burst attacks."""
        return 'The abjurer makes three Arcane Burst attacks.'

    def arcane_burst_attack(self) -> str:
        """Melee or Ranged Spell Attack: +6 to hit, reach 5 ft. or range 120 ft., one target. Hit: 20 (3d10 + 4) force damage."""
        return 'Melee or Ranged Spell Attack: +6 to hit, reach 5 ft. or range 120 ft., one target. Hit: 20 (3d10 + 4) force damage.'

    def force_blast_attack(self) -> str:
        """Each creature in a 20-foot cube originating from the abjurer must make a DC 16 Constitution saving throw. On a failed save, a creature takes 36 (8d8) force damage and is pushed up to 10 feet away from the abjurer. On a successful save, a creature takes half as much damage and isn't pushed."""
        return "Each creature in a 20-foot cube originating from the abjurer must make a DC 16 Constitution saving throw. On a failed save, a creature takes 36 (8d8) force damage and is pushed up to 10 feet away from the abjurer. On a successful save, a creature takes half as much damage and isn't pushed."

    def spellcasting_attack(self) -> str:
        """The abjurer casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 16):"""
        return 'The abjurer casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 16):'

