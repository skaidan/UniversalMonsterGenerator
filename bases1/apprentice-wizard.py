# bases1/apprentice-wizard.py
"""
ApprenticeWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=apprentice-wizard
"""
from creature_base import GlobalCreatureBaseClass


class ApprenticeWizard(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - ApprenticeWizard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 10, 'CON': 10, 'INT': 14, 'WIS': 10, 'CHAR': 11, 'armor_class': 10, 'alignment': 'any alignment Armor Class  10 (13 with  mage armor ) Hit Points  13 (3d8) Speed  30 ft. STR 10 (+0) DEX 10 (+0) CON 10 (+0) INT 14 (+2) WIS 10 (+0) CHA 11 (+0) Skills  Arcana +4', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['arcane_burst', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def arcane_burst_attack(self) -> str:
        """Melee or Ranged Spell Attack: +4 to hit, reach 5 ft. or range 120 ft., one target. Hit: 7 (1d10 + 2) force damage."""
        return 'Melee or Ranged Spell Attack: +4 to hit, reach 5 ft. or range 120 ft., one target. Hit: 7 (1d10 + 2) force damage.'

    def spellcasting_attack(self) -> str:
        """The apprentice casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 12):"""
        return 'The apprentice casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 12):'

