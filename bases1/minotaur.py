# bases1/minotaur.py
"""
Minotaur creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=minotaur
"""
from creature_base import GlobalCreatureBaseClass


class Minotaur(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Minotaur
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 76, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 11, 'CON': 16, 'INT': 6, 'WIS': 16, 'CHAR': 9, 'armor_class': 14, 'alignment': 'chaotic evil Armor Class  14 (natural armor) Hit Points  76 (9d10 + 27) Speed  40 ft. STR 18 (+4) DEX 11 (+0) CON 16 (+3) INT 6 (-2) WIS 16 (+3) CHA 9 (-1) Skills  Perception +7 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'greataxe', 'gore']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the minotaur moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it"""
        return 'If the minotaur moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 17 (2d12 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 17 (2d12 + 4) slashing damage.'

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage.'

