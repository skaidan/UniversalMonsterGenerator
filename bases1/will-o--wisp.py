# bases1/will-o--wisp.py
"""
WillOWisp creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=will-o--wisp
"""
from creature_base import GlobalCreatureBaseClass


class WillOWisp(GlobalCreatureBaseClass):
    """
    Tiny undead creature - WillOWisp
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 28, 'CON': 10, 'INT': 13, 'WIS': 14, 'CHAR': 11, 'armor_class': 19, 'alignment': 'chaotic evil Armor Class  19 Hit Points  22 (9d4) Speed  0 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['consume_life', 'shock', 'invisibility']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def consume_life(self) -> str:
        """As a bonus action, the will-o'-wisp can target one creature it can see within 5 feet of it that has 0 hit points and is still alive. The target must succeed on a DC 10 Constitution saving throw agains"""
        return "As a bonus action, the will-o'-wisp can target one creature it can see within 5 feet of it that has 0 hit points and is still alive. The target must succeed on a DC 10 Constitution saving throw agains"

    def shock_attack(self) -> str:
        """Melee Spell Attack: +4 to hit, reach 5 ft., one creature. Hit: 9 (2d8) lightning damage."""
        return 'Melee Spell Attack: +4 to hit, reach 5 ft., one creature. Hit: 9 (2d8) lightning damage.'

    def invisibility_attack(self) -> str:
        """The will-o'-wisp and its light magically become invisible until it attacks or uses its Consume Life, or until its concentration ends (as if concentrating on a spell)."""
        return "The will-o'-wisp and its light magically become invisible until it attacks or uses its Consume Life, or until its concentration ends (as if concentrating on a spell)."

