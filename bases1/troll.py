# bases1/troll.py
"""
Troll creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=troll
"""
from creature_base import GlobalCreatureBaseClass


class Troll(GlobalCreatureBaseClass):
    """
    Large giant creature - Troll
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 84, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 20, 'INT': 7, 'WIS': 9, 'CHAR': 7, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (natural armor) Hit Points  84 (8d10 + 40) Speed  30 ft. STR 18 (+4) DEX 13 (+1) CON 20 (+5) INT 7 (-2) WIS 9 (-1) CHA 7 (-2) Skills  Perception +2 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The troll has advantage on Wisdom (Perception) checks that rely on smell.Regeneration. The troll regains 10 hit points at the start of its turn. If the troll takes acid or fire damage, this trait does"""
        return 'The troll has advantage on Wisdom (Perception) checks that rely on smell.Regeneration. The troll regains 10 hit points at the start of its turn. If the troll takes acid or fire damage, this trait does'

    def multiattack_attack(self) -> str:
        """The troll makes three attacks: one with its bite and two with its claws."""
        return 'The troll makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.'

