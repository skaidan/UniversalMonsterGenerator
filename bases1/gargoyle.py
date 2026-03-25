# bases1/gargoyle.py
"""
Gargoyle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gargoyle
"""
from creature_base import GlobalCreatureBaseClass


class Gargoyle(GlobalCreatureBaseClass):
    """
    Medium elemental creature - Gargoyle
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 11, 'CON': 16, 'INT': 6, 'WIS': 11, 'CHAR': 7, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (natural armor) Hit Points  52 (7d8 + 21) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'multiattack', 'bite', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the gargoyle remains motionless, it is indistinguishable from an inanimate statue."""
        return 'While the gargoyle remains motionless, it is indistinguishable from an inanimate statue.'

    def multiattack_attack(self) -> str:
        """The gargoyle makes two attacks: one with its bite and one with its claws."""
        return 'The gargoyle makes two attacks: one with its bite and one with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage.'

