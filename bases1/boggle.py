# bases1/boggle.py
"""
Boggle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=boggle
"""
from creature_base import GlobalCreatureBaseClass


class Boggle(GlobalCreatureBaseClass):
    """
    Small Fey creature - Boggle
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 18, 'CON': 13, 'INT': 6, 'WIS': 12, 'CHAR': 7, 'armor_class': 14, 'alignment': 'typically Chaotic Neutral Armor Class  14 Hit Points  18 (4d6 + 4) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pummel', 'oil_puddle', '&nbsp;_slippery_oil', '&nbsp;_sticky_oil']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pummel_attack(self) -> str:
        """Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) bludgeoning damage."""
        return 'Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) bludgeoning damage.'

    def oil_puddle_attack(self) -> str:
        """The boggle creates a puddle of nonflammable oil. The puddle is 1 inch deep and covers the ground in the boggle's space. The puddle is difficult terrain for all creatures except boggles and lasts for 1 hour. The oil has one of the following additional effects of the boggle's choice:"""
        return "The boggle creates a puddle of nonflammable oil. The puddle is 1 inch deep and covers the ground in the boggle's space. The puddle is difficult terrain for all creatures except boggles and lasts for 1 hour. The oil has one of the following additional effects of the boggle's choice:"

    def &nbsp;_slippery_oil_attack(self) -> str:
        """Any non-boggle creature that enters the puddle or starts its turn there must succeed on a DC 11 Dexterity saving throw or fall prone."""
        return 'Any non-boggle creature that enters the puddle or starts its turn there must succeed on a DC 11 Dexterity saving throw or fall prone.'

    def &nbsp;_sticky_oil_attack(self) -> str:
        """Any non-boggle creature that enters the puddle or starts its turn there must succeed on a DC 11 Strength saving throw or be restrained. On its turn, a creature can use an action to try to extricate itself, ending the effect and moving into the nearest unoccupied space of its choice with a successful DC 11 Strength check."""
        return 'Any non-boggle creature that enters the puddle or starts its turn there must succeed on a DC 11 Strength saving throw or be restrained. On its turn, a creature can use an action to try to extricate itself, ending the effect and moving into the nearest unoccupied space of its choice with a successful DC 11 Strength check.'

