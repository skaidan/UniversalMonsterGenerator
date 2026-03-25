# bases1/eidolon.py
"""
Eidolon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=eidolon
"""
from creature_base import GlobalCreatureBaseClass


class Eidolon(GlobalCreatureBaseClass):
    """
    Medium Undead creature - Eidolon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 63, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 8, 'CON': 9, 'INT': 14, 'WIS': 19, 'CHAR': 16, 'armor_class': 9, 'alignment': 'any alignment Armor Class  9 Hit Points  63 (18d8 - 18) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['incorporeal_movement', 'divine_dread']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def incorporeal_movement(self) -> str:
        """The eidolon can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object other than a sacred statue.Sacred Animat"""
        return 'The eidolon can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object other than a sacred statue.Sacred Animat'

    def divine_dread_attack(self) -> str:
        """Each creature within 60 feet of the eidolon that can see it must succeed on a DC 15 Wisdom saving throw or be frightened of it for 1 minute. While frightened in this way, the creature must take the Dash action and move away from the eidolon by the safest available route at the start of each of its turns, unless there is nowhere for it to move, in which case the creature also becomes stunned until it can move again. A frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to any eidolon's Divine Dread for the next 24 hours."""
        return "Each creature within 60 feet of the eidolon that can see it must succeed on a DC 15 Wisdom saving throw or be frightened of it for 1 minute. While frightened in this way, the creature must take the Dash action and move away from the eidolon by the safest available route at the start of each of its turns, unless there is nowhere for it to move, in which case the creature also becomes stunned until it can move again. A frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to any eidolon's Divine Dread for the next 24 hours."

