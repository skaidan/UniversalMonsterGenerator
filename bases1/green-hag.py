# bases1/green-hag.py
"""
GreenHag creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=green-hag
"""
from creature_base import GlobalCreatureBaseClass


class GreenHag(GlobalCreatureBaseClass):
    """
    Medium fey creature - GreenHag
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 82, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 12, 'CON': 16, 'INT': 13, 'WIS': 14, 'CHAR': 14, 'armor_class': 17, 'alignment': 'neutral evil Armor Class  17 (natural armor) Hit Points  82 (11d8 + 33) Speed  30 ft. STR 18 (+4) DEX 12 (+1) CON 16 (+3) INT 13 (+1) WIS 14 (+2) CHA 14 (+2) Skills  Arcana +3', 'legendary': False, 'size': 'Medium', 'type': 'fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'claws', 'illusory_appearance', 'invisible_passage']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The hag can breathe air and water.Innate Spellcasting. The hag's innate spellcasting ability is Charisma (spell save DC 12). She can innately cast the following spells, requiring no material component"""
        return "The hag can breathe air and water.Innate Spellcasting. The hag's innate spellcasting ability is Charisma (spell save DC 12). She can innately cast the following spells, requiring no material component"

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.'

    def illusory_appearance_attack(self) -> str:
        """The hag covers herself and anything she is wearing or carrying with a magical illusion that makes her look like another creature of her general size and humanoid shape. The illusion ends if the hag takes a bonus action to end it or if she dies. The changes wrought by this effect fail to hold up to physical inspection. For example, the hag could appear to have smooth skin, but someone touching her would feel her rough flesh. Otherwise, a creature must take an action to visually inspect the illusion and succeed on a DC 20 Intelligence (Investigation) check to discern that the hag is disguised."""
        return 'The hag covers herself and anything she is wearing or carrying with a magical illusion that makes her look like another creature of her general size and humanoid shape. The illusion ends if the hag takes a bonus action to end it or if she dies. The changes wrought by this effect fail to hold up to physical inspection. For example, the hag could appear to have smooth skin, but someone touching her would feel her rough flesh. Otherwise, a creature must take an action to visually inspect the illusion and succeed on a DC 20 Intelligence (Investigation) check to discern that the hag is disguised.'

    def invisible_passage_attack(self) -> str:
        """The hag magically turns invisible until she attacks or casts a spell, or until her concentration ends (as if concentrating on a spell). While invisible, she leaves no physical evidence of her passage, so she can be tracked only by magic. Any equipment she wears or carries is invisible with her."""
        return 'The hag magically turns invisible until she attacks or casts a spell, or until her concentration ends (as if concentrating on a spell). While invisible, she leaves no physical evidence of her passage, so she can be tracked only by magic. Any equipment she wears or carries is invisible with her.'

