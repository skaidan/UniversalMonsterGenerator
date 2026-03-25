# bases1/githyanki-warrior.py
"""
GithyankiWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githyanki-warrior
"""
from creature_base import GlobalCreatureBaseClass


class GithyankiWarrior(GlobalCreatureBaseClass):
    """
    Medium humanoid (Gith) creature - GithyankiWarrior
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 49, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 12, 'INT': 13, 'WIS': 13, 'CHAR': 10, 'armor_class': 17, 'alignment': 'lawful evil Armor Class  17 (half plate) Hit Points  49 (9d8 + 9) Speed  30 ft. STR 15 (+2) DEX 14 (+2) CON 12 (+1) INT 13 (+1) WIS 13 (+1) CHA 10 (+0) Saving Throws  Con +3', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Gith)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting_(psionics)', 'multiattack', 'greatsword']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting_(psionics)(self) -> str:
        """The githyanki's innate spellcasting ability is Intelligence. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: jump, misty step, """
        return "The githyanki's innate spellcasting ability is Intelligence. It can innately cast the following spells, requiring no components:At will: mage hand (the hand is invisible)3/day each: jump, misty step, "

    def multiattack_attack(self) -> str:
        """The githyanki makes two greatsword attacks."""
        return 'The githyanki makes two greatsword attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage plus 7 (2d6) psychic damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage plus 7 (2d6) psychic damage.'

