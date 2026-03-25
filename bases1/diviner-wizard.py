# bases1/diviner-wizard.py
"""
DivinerWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=diviner-wizard
"""
from creature_base import GlobalCreatureBaseClass


class DivinerWizard(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - DivinerWizard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 90, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 11, 'INT': 18, 'WIS': 12, 'CHAR': 11, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  90 (20d8) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 11 (+0) INT 18 (+4) WIS 12 (+1) CHA 11 (+0) Saving Throws  Int +7', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'arcane_burst', 'overwhelming_revelation_(recharge_5–6)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The diviner makes three Arcane Burst attacks."""
        return 'The diviner makes three Arcane Burst attacks.'

    def arcane_burst_attack(self) -> str:
        """Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120 ft., one target. Hit: 20 (3d10 + 4) radiant damage."""
        return 'Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120 ft., one target. Hit: 20 (3d10 + 4) radiant damage.'

    def overwhelming_revelation_(recharge_5–6)_attack(self) -> str:
        """The diviner magically creates a burst of illumination in a 10-foot-radius sphere centered on a point within 120 feet of it. Each creature in that area must make a DC 15 Wisdom saving throw. On a failed save, a creature takes 45 (10d8) psychic damage and is stunned until the end of the diviner's next turn. On a successful save, the creature takes half as much damage and isn't stunned."""
        return "The diviner magically creates a burst of illumination in a 10-foot-radius sphere centered on a point within 120 feet of it. Each creature in that area must make a DC 15 Wisdom saving throw. On a failed save, a creature takes 45 (10d8) psychic damage and is stunned until the end of the diviner's next turn. On a successful save, the creature takes half as much damage and isn't stunned."

    def spellcasting_attack(self) -> str:
        """The diviner casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 15):"""
        return 'The diviner casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 15):'

