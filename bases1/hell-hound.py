# bases1/hell-hound.py
"""
HellHound creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hell-hound
"""
from creature_base import GlobalCreatureBaseClass


class HellHound(GlobalCreatureBaseClass):
    """
    Medium fiend creature - HellHound
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 14, 'INT': 6, 'WIS': 13, 'CHAR': 6, 'armor_class': 15, 'alignment': 'lawful evil Armor Class  15 (natural armor) Hit Points  45 (7d8 + 14) Speed  50 ft. STR 17 (+3) DEX 12 (+1) CON 14 (+2) INT 6 (-2) WIS 13 (+1) CHA 6 (-2) Skills  Perception +5 Damage Immunities  fire Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite', 'fire_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The hound has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The hound has advantage on an attack roll against a creature if at least one of the hound's allies is """
        return "The hound has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The hound has advantage on an attack roll against a creature if at least one of the hound's allies is "

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 7 (2d6) fire damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 7 (2d6) fire damage.'

    def fire_breath_(recharge_5-6)_attack(self) -> str:
        """The hound exhales fire in a 15-foot cone. Each creature in that area must make a DC 12 Dexterity saving throw, taking 21 (6d6) fire damage on a failed save, or half as much damage on a successful one."""
        return 'The hound exhales fire in a 15-foot cone. Each creature in that area must make a DC 12 Dexterity saving throw, taking 21 (6d6) fire damage on a failed save, or half as much damage on a successful one.'

