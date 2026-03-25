# bases1/owlbear.py
"""
Owlbear creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=owlbear
"""
from creature_base import GlobalCreatureBaseClass


class Owlbear(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Owlbear
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 59, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 12, 'CON': 17, 'INT': 3, 'WIS': 12, 'CHAR': 7, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  59 (7d10 + 21) Speed  40 ft. STR 20 (+5) DEX 12 (+1) CON 17 (+3) INT 3 (-4) WIS 12 (+1) CHA 7 (-2) Skills  Perception +3 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight_and_smell', 'multiattack', 'beak', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight_and_smell(self) -> str:
        """The owlbear has advantage on Wisdom (Perception) checks that rely on sight or smell."""
        return 'The owlbear has advantage on Wisdom (Perception) checks that rely on sight or smell.'

    def multiattack_attack(self) -> str:
        """The owlbear makes two attacks: one with its beak and one with its claws."""
        return 'The owlbear makes two attacks: one with its beak and one with its claws.'

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 10 (1d10 + 5) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 10 (1d10 + 5) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage.'

