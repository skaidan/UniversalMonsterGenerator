# bases1/evoker-wizard.py
"""
EvokerWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=evoker-wizard
"""
from creature_base import GlobalCreatureBaseClass


class EvokerWizard(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - EvokerWizard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 121, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 12, 'INT': 17, 'WIS': 12, 'CHAR': 11, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  121 (22d8 + 22) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 12 (+1) INT 17 (+3) WIS 12 (+1) CHA 11 (+0) Saving Throws  Int +7', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'arcane_burst', 'sculpted_explosion_(recharge_4–6)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The evoker makes three Arcane Burst attacks."""
        return 'The evoker makes three Arcane Burst attacks.'

    def arcane_burst_attack(self) -> str:
        """Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120 ft., one target. Hit: 25 (4d10 + 3) force damage."""
        return 'Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120 ft., one target. Hit: 25 (4d10 + 3) force damage.'

    def sculpted_explosion_(recharge_4–6)_attack(self) -> str:
        """The evoker unleashes a magical explosion of a particular damage type: cold, fire, lightning, or thunder. The magic erupts in a 20-foot-radius sphere centered on a point within 150 feet of the evoker. Each creature in that area must make a DC 15 Dexterity saving throw. The evoker can select up to three creatures it can see in the area to ignore the spell, as the evoker sculpts the spell's energy around them. On a failed save, a creature takes 40 (9d8) damage of the chosen type and is knocked prone. On a successful save, a creature takes half as much damage and isn't knocked prone."""
        return "The evoker unleashes a magical explosion of a particular damage type: cold, fire, lightning, or thunder. The magic erupts in a 20-foot-radius sphere centered on a point within 150 feet of the evoker. Each creature in that area must make a DC 15 Dexterity saving throw. The evoker can select up to three creatures it can see in the area to ignore the spell, as the evoker sculpts the spell's energy around them. On a failed save, a creature takes 40 (9d8) damage of the chosen type and is knocked prone. On a successful save, a creature takes half as much damage and isn't knocked prone."

    def spellcasting_attack(self) -> str:
        """The evoker casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 15):"""
        return 'The evoker casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 15):'

