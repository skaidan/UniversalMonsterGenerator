# bases1/blink-dog.py
"""
BlinkDog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=blink-dog
"""
from creature_base import GlobalCreatureBaseClass


class BlinkDog(GlobalCreatureBaseClass):
    """
    Medium fey creature - BlinkDog
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 17, 'CON': 12, 'INT': 10, 'WIS': 13, 'CHAR': 11, 'armor_class': 13, 'alignment': 'lawful good Armor Class  13 Hit Points  22 (4d8 + 4) Speed  40 ft. STR 12 (+1) DEX 17 (+3) CON 12 (+1) INT 10 (+0) WIS 13 (+1) CHA 11 (+0) Skills  Perception +3', 'legendary': False, 'size': 'Medium', 'type': 'fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite', 'teleport_(recharge_4-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The dog has advantage on Wisdom (Perception) checks that rely on hearing or smell."""
        return 'The dog has advantage on Wisdom (Perception) checks that rely on hearing or smell.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage.'

    def teleport_(recharge_4-6)_attack(self) -> str:
        """The dog magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the dog can make one bite attack."""
        return 'The dog magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the dog can make one bite attack.'

