# bases1/blackguard.py
"""
Blackguard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=blackguard
"""
from creature_base import GlobalCreatureBaseClass


class Blackguard(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Paladin) creature - Blackguard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 119, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 11, 'CON': 18, 'INT': 11, 'WIS': 14, 'CHAR': 15, 'armor_class': 18, 'alignment': 'typically Neutral Evil Armor Class  18 (plate) Hit Points  119 (14d8 + 56) Speed  30 ft. STR 18 (+4) DEX 11 (+0) CON 18 (+4) INT 11 (+0) WIS 14 (+2) CHA 15 (+2) Saving Throws  Wis +5', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Paladin)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'glaive', 'shortbow', 'dreadful_aspect_(recharges_after_a_short_or_long_rest)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The blackguard makes three attacks, using Glaive, Shortbow, or both."""
        return 'The blackguard makes three attacks, using Glaive, Shortbow, or both.'

    def glaive_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 9 (1d10 + 4) slashing damage plus 9 (2d8) necrotic damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 9 (1d10 + 4) slashing damage plus 9 (2d8) necrotic damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def dreadful_aspect_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """Each enemy within 30 feet of the blackguard must succeed on a DC 13 Wisdom saving throw or be frightened of the blackguard for 1 minute. If a frightened target ends its turn more than 30 feet away from the blackguard, the target can repeat the saving throw, ending the effect on itself on a success."""
        return 'Each enemy within 30 feet of the blackguard must succeed on a DC 13 Wisdom saving throw or be frightened of the blackguard for 1 minute. If a frightened target ends its turn more than 30 feet away from the blackguard, the target can repeat the saving throw, ending the effect on itself on a success.'

    def spellcasting_attack(self) -> str:
        """The blackguard casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 13):"""
        return 'The blackguard casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 13):'

