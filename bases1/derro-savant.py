# bases1/derro-savant.py
"""
DerroSavant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=derro-savant
"""
from creature_base import GlobalCreatureBaseClass


class DerroSavant(GlobalCreatureBaseClass):
    """
    Small Aberration (Sorcerer) creature - DerroSavant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 36, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 12, 'INT': 11, 'WIS': 5, 'CHAR': 14, 'armor_class': 13, 'alignment': 'typically Chaotic Evil Armor Class  13 (leather armor) Hit Points  36 (8d6 + 8) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 12 (+1) INT 11 (+0) WIS 5 (-3) CHA 14 (+2) Skills  Stealth +4 Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Small', 'type': 'Aberration (Sorcerer)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'quarterstaff', 'chromatic_beam', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The derro has advantage on saving throws against spells and other magical effects.Sunlight Sensitivity. While in sunlight, the derro has disadvantage on attack rolls, as well as on Wisdom (Perception)"""
        return 'The derro has advantage on saving throws against spells and other magical effects.Sunlight Sensitivity. While in sunlight, the derro has disadvantage on attack rolls, as well as on Wisdom (Perception)'

    def quarterstaff_attack(self) -> str:
        """Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) bludgeoning damage."""
        return 'Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) bludgeoning damage.'

    def chromatic_beam_attack(self) -> str:
        """The derro launches a brilliant beam of magical energy in a 5-foot-wide line that is 60 feet long. Each creature in the line must make a DC 12 Dexterity saving throw, taking 21 (6d6) radiant damage on a failed save, or half as much damage on a successful one."""
        return 'The derro launches a brilliant beam of magical energy in a 5-foot-wide line that is 60 feet long. Each creature in the line must make a DC 12 Dexterity saving throw, taking 21 (6d6) radiant damage on a failed save, or half as much damage on a successful one.'

    def spellcasting_attack(self) -> str:
        """The derro casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 12):"""
        return 'The derro casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 12):'

