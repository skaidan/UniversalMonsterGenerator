# bases1/warlock-of-the-fiend.py
"""
WarlockOfTheFiend creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warlock-of-the-fiend
"""
from creature_base import GlobalCreatureBaseClass


class WarlockOfTheFiend(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - WarlockOfTheFiend
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 78, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 16, 'CON': 15, 'INT': 12, 'WIS': 12, 'CHAR': 18, 'armor_class': 13, 'alignment': 'any alignment Armor Class  13 (16 with  mage armor ) Hit Points  78 (12d8 + 24) Speed  30 ft. STR 10 (+0) DEX 16 (+3) CON 15 (+2) INT 12 (+1) WIS 12 (+1) CHA 18 (+4) Saving Throws  Wis +4', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['dark_ones_own_luck_(recharges_after_a_short_or_long_rest)', 'multiattack', 'scimitar', 'hellfire', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def dark_ones_own_luck_(recharges_after_a_short_or_long_rest)(self) -> str:
        """When the warlock makes an ability check or saving throw, it can add a d10 to the roll. It can do this after the roll is made but before any of the roll's effects occur."""
        return "When the warlock makes an ability check or saving throw, it can add a d10 to the roll. It can do this after the roll is made but before any of the roll's effects occur."

    def multiattack_attack(self) -> str:
        """The warlock makes three Scimitar attacks."""
        return 'The warlock makes three Scimitar attacks.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage plus 14 (4d6) fire damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage plus 14 (4d6) fire damage.'

    def hellfire_attack(self) -> str:
        """Green flame explodes in a 10-foot-radius sphere centered on a point within 120 feet of the warlock. Each creature in that area must make a DC 15 Dexterity saving throw, taking 16 (3d10) fire damage and 11 (2d10) necrotic damage on a failed save, or half as much damage on a successful one."""
        return 'Green flame explodes in a 10-foot-radius sphere centered on a point within 120 feet of the warlock. Each creature in that area must make a DC 15 Dexterity saving throw, taking 16 (3d10) fire damage and 11 (2d10) necrotic damage on a failed save, or half as much damage on a successful one.'

    def spellcasting_attack(self) -> str:
        """The warlock casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 15):"""
        return 'The warlock casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 15):'

