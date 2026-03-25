# bases1/warlock-of-the-archfey.py
"""
WarlockOfTheArchfey creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warlock-of-the-archfey
"""
from creature_base import GlobalCreatureBaseClass


class WarlockOfTheArchfey(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - WarlockOfTheArchfey
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 16, 'CON': 11, 'INT': 11, 'WIS': 12, 'CHAR': 18, 'armor_class': 13, 'alignment': 'any alignment Armor Class  13 (16 with  mage armor ) Hit Points  67 (15d8) Speed  30 ft. STR 9 (-1) DEX 16 (+3) CON 11 (+0) INT 11 (+0) WIS 12 (+1) CHA 18 (+4) Saving Throws  Wis +3', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'rapier', 'bewildering_word', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The warlock makes two Rapier attacks, or it uses Bewildering Word twice."""
        return 'The warlock makes two Rapier attacks, or it uses Bewildering Word twice.'

    def rapier_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 7 (2d6) force damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 7 (2d6) force damage.'

    def bewildering_word_attack(self) -> str:
        """The warlock utters a magical bewilderment, targeting one creature it can see within 60 feet of it. The target must succeed on a DC 14 Wisdom saving throw or take 9 (2d8) psychic damage and have disadvantage on attack rolls until the end of the warlock's next turn."""
        return "The warlock utters a magical bewilderment, targeting one creature it can see within 60 feet of it. The target must succeed on a DC 14 Wisdom saving throw or take 9 (2d8) psychic damage and have disadvantage on attack rolls until the end of the warlock's next turn."

    def spellcasting_attack(self) -> str:
        """The warlock casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 14):"""
        return 'The warlock casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 14):'

