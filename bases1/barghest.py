# bases1/barghest.py
"""
Barghest creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=barghest
"""
from creature_base import GlobalCreatureBaseClass


class Barghest(GlobalCreatureBaseClass):
    """
    Large Fiend creature - Barghest
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 15, 'CON': 14, 'INT': 13, 'WIS': 12, 'CHAR': 14, 'armor_class': 17, 'alignment': 'typically Neutral Evil Armor Class  17 (natural armor) Hit Points  60 (8d10 + 16) Speed  60 ft. (30 ft. in goblin form) STR 19 (+4) DEX 15 (+2) CON 14 (+2) INT 13 (+1) WIS 12 (+1) CHA 14 (+2) Skills  Deception +4', 'legendary': False, 'size': 'Large', 'type': 'Fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fire_banishment', 'multiattack', 'bite', 'claw', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fire_banishment(self) -> str:
        """When the barghest starts its turn engulfed in flames that are at least 10 feet high or wide, it must succeed on a DC 15 Charisma saving throw or be instantly banished to Gehenna.Soul Feeding. The barg"""
        return 'When the barghest starts its turn engulfed in flames that are at least 10 feet high or wide, it must succeed on a DC 15 Charisma saving throw or be instantly banished to Gehenna.Soul Feeding. The barg'

    def multiattack_attack(self) -> str:
        """The barghest makes one Bite attack and one Claw attack."""
        return 'The barghest makes one Bite attack and one Claw attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage.'

    def spellcasting_attack(self) -> str:
        """The barghest casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 12):"""
        return 'The barghest casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 12):'

