# bases1/necromancer-wizard.py
"""
NecromancerWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=necromancer-wizard
"""
from creature_base import GlobalCreatureBaseClass


class NecromancerWizard(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - NecromancerWizard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 110, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 12, 'INT': 17, 'WIS': 12, 'CHAR': 11, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  110 (20d8 + 20) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 12 (+1) INT 17 (+3) WIS 12 (+1) CHA 11 (+0) Saving Throws  Int +7', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'arcane_burst', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The necromancer makes three Arcane Burst attacks."""
        return 'The necromancer makes three Arcane Burst attacks.'

    def arcane_burst_attack(self) -> str:
        """Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120 ft., one target. Hit: 25 (4d10 + 3) necrotic damage."""
        return 'Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120 ft., one target. Hit: 25 (4d10 + 3) necrotic damage.'

    def spellcasting_attack(self) -> str:
        """The necromancer casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 15):"""
        return 'The necromancer casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 15):'

