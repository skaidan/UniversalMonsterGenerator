# bases1/deathlock.py
"""
Deathlock creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deathlock
"""
from creature_base import GlobalCreatureBaseClass


class Deathlock(GlobalCreatureBaseClass):
    """
    Medium Undead (Warlock) creature - Deathlock
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 36, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 15, 'CON': 10, 'INT': 14, 'WIS': 12, 'CHAR': 16, 'armor_class': 12, 'alignment': 'typically Neutral Evil Armor Class  12 (15 with  mage armor ) Hit Points  36 (8d8) Speed  30 ft. STR 11 (+0) DEX 15 (+2) CON 10 (+0) INT 14 (+2) WIS 12 (+1) CHA 16 (+3) Saving Throws  Int +4', 'legendary': False, 'size': 'Medium', 'type': 'Undead (Warlock)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['turn_resistance', 'multiattack', 'deathly_claw', 'grave_bolt', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def turn_resistance(self) -> str:
        """The deathlock has advantage on saving throws against any effect that turns Undead.Unusual Nature. The deathlock doesn't require air, food, drink, or sleep."""
        return "The deathlock has advantage on saving throws against any effect that turns Undead.Unusual Nature. The deathlock doesn't require air, food, drink, or sleep."

    def multiattack_attack(self) -> str:
        """The deathlock makes two Deathly Claw or Grave Bolt attacks."""
        return 'The deathlock makes two Deathly Claw or Grave Bolt attacks.'

    def deathly_claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) necrotic damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) necrotic damage.'

    def grave_bolt_attack(self) -> str:
        """Ranged Spell Attack: +5 to hit, range 120 ft., one target. Hit: 14 (2d10 + 3) necrotic damage."""
        return 'Ranged Spell Attack: +5 to hit, range 120 ft., one target. Hit: 14 (2d10 + 3) necrotic damage.'

    def spellcasting_attack(self) -> str:
        """The deathlock casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 13):"""
        return 'The deathlock casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 13):'

