# bases1/winter-wolf.py
"""
WinterWolf creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=winter-wolf
"""
from creature_base import GlobalCreatureBaseClass


class WinterWolf(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - WinterWolf
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 14, 'INT': 7, 'WIS': 12, 'CHAR': 8, 'armor_class': 13, 'alignment': 'neutral evil Armor Class  13 (natural armor) Hit Points  75 (10d10 + 20) Speed  50 ft. STR 18 (+4) DEX 13 (+1) CON 14 (+2) INT 7 (-2) WIS 12 (+1) CHA 8 (-1) Skills  Perception +5', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite', 'cold_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is wit"""
        return "The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is wit"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone.'

    def cold_breath_(recharge_5-6)_attack(self) -> str:
        """The wolf exhales a blast of freezing wind in a 15-foot cone. Each creature in that area must make a DC 12 Dexterity saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one."""
        return 'The wolf exhales a blast of freezing wind in a 15-foot cone. Each creature in that area must make a DC 12 Dexterity saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one.'

