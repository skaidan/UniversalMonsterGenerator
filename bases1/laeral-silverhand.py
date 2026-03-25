# bases1/laeral-silverhand.py
"""
LaeralSilverhand creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=laeral-silverhand
"""
from creature_base import GlobalCreatureBaseClass


class LaeralSilverhand(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - LaeralSilverhand
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 228, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 17, 'CON': 20, 'INT': 20, 'WIS': 20, 'CHAR': 19, 'armor_class': 18, 'alignment': 'chaotic good Armor Class  18 ( robe of the archmagi ) Hit Points  228 (24d8 + 120) Speed  30 ft. STR 13 (+1) DEX 17 (+3) CON 20 (+5) INT 20 (+5) WIS 20 (+5) CHA 19 (+4) Saving Throws  Int +11', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['special_equipment', 'multiattack', 'silver_hair', 'flame_tongue', 'spellfire_(recharges_after_a_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def special_equipment(self) -> str:
        """Laeral wears a white robe of the archmagi (accounted for in her statistics). She wields a flame tongue longsword.Magic Resistance. While wearing her robe of the archmagi, Laeral has advantage on savin"""
        return 'Laeral wears a white robe of the archmagi (accounted for in her statistics). She wields a flame tongue longsword.Magic Resistance. While wearing her robe of the archmagi, Laeral has advantage on savin'

    def multiattack_attack(self) -> str:
        """Laeral makes three attacks with her silver hair and flame tongue, in any combination. She can cast one of her cantrips or 1st-level spells before or after making these attacks."""
        return 'Laeral makes three attacks with her silver hair and flame tongue, in any combination. She can cast one of her cantrips or 1st-level spells before or after making these attacks.'

    def silver_hair_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 7 (2d6) force damage, and the target must succeed on a DC 19 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 7 (2d6) force damage, and the target must succeed on a DC 19 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def flame_tongue_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) slashing damage plus 7 (2d6) fire damage, or 6 (1d10 + 1) slashing damage plus 7 (2d6) fire damage when used with two hands."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) slashing damage plus 7 (2d6) fire damage, or 6 (1d10 + 1) slashing damage plus 7 (2d6) fire damage when used with two hands.'

    def spellfire_(recharges_after_a_long_rest)_attack(self) -> str:
        """Magical, heatless, silver fire harmlessly erupts from Laeral and surrounds her until she is incapacitated or until she uses an action to quench it. She gains one of the following benefits of her choice, which lasts until the silver fire ends:"""
        return 'Magical, heatless, silver fire harmlessly erupts from Laeral and surrounds her until she is incapacitated or until she uses an action to quench it. She gains one of the following benefits of her choice, which lasts until the silver fire ends:'

