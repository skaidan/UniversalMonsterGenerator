# bases1/archdruid.py
"""
Archdruid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=archdruid
"""
from creature_base import GlobalCreatureBaseClass


class Archdruid(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Druid) creature - Archdruid
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 154, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 14, 'CON': 12, 'INT': 12, 'WIS': 20, 'CHAR': 11, 'armor_class': 14, 'alignment': 'any alignment Armor Class  14 (hide armor) Hit Points  154 (28d8 + 28) Speed  30 ft. STR 14 (+2) DEX 14 (+2) CON 12 (+1) INT 12 (+1) WIS 20 (+5) CHA 11 (+0) Saving Throws  Int +5', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Druid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'staff', 'wildfire', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The archdruid makes three Staff or Wildfire attacks. It can replace one attack with a use of Spellcasting."""
        return 'The archdruid makes three Staff or Wildfire attacks. It can replace one attack with a use of Spellcasting.'

    def staff_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage plus 21 (6d6) poison damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage plus 21 (6d6) poison damage.'

    def wildfire_attack(self) -> str:
        """Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 26 (6d6 + 5) fire damage, and the target is blinded until the start of the druid's next turn."""
        return "Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 26 (6d6 + 5) fire damage, and the target is blinded until the start of the druid's next turn."

    def spellcasting_attack(self) -> str:
        """The archdruid casts one of the following spells, using Wisdom as the spellcasting ability (spell save DC 17):"""
        return 'The archdruid casts one of the following spells, using Wisdom as the spellcasting ability (spell save DC 17):'

