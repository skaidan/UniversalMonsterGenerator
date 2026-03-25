# bases1/faerie-dragon.py
"""
FaerieDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=faerie-dragon
"""
from creature_base import GlobalCreatureBaseClass


class FaerieDragon(GlobalCreatureBaseClass):
    """
    Tiny dragon creature - FaerieDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 14, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 20, 'CON': 13, 'INT': 14, 'WIS': 12, 'CHAR': 16, 'armor_class': 15, 'alignment': 'chaotic good Armor Class  15 Hit Points  14 (4d4 + 4) Speed  10 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'bite', 'euphoria_breath_(recharge_5-6)', '&nbsp;_1-4', '&nbsp;_5-6']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The dragon's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast a number of spells, requiring no material components. As the dragon ages and changes color, it gains addit"""
        return "The dragon's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast a number of spells, requiring no material components. As the dragon ages and changes color, it gains addit"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 1 piercing damage.'

    def euphoria_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales a puff of euphoria gas at one creature within 5 feet of it. The target must succeed on a DC 11 Wisdom saving throw, or for 1 minute, the target can't take reactions and must roll a d6 at the start of each of its turns to determine its behavior during the turn:"""
        return "The dragon exhales a puff of euphoria gas at one creature within 5 feet of it. The target must succeed on a DC 11 Wisdom saving throw, or for 1 minute, the target can't take reactions and must roll a d6 at the start of each of its turns to determine its behavior during the turn:"

    def &nbsp;_1-4_attack(self) -> str:
        """The target takes no action or bonus action and uses all of its movement to move in a random direction."""
        return 'The target takes no action or bonus action and uses all of its movement to move in a random direction.'

    def &nbsp;_5-6_attack(self) -> str:
        """The target doesn't move, and the only thing it can do on its turn is make a DC 11 Wisdom saving throw, ending the effect on itself on a success."""
        return "The target doesn't move, and the only thing it can do on its turn is make a DC 11 Wisdom saving throw, ending the effect on itself on a success."

