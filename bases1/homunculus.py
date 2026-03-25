# bases1/homunculus.py
"""
Homunculus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=homunculus
"""
from creature_base import GlobalCreatureBaseClass


class Homunculus(GlobalCreatureBaseClass):
    """
    Tiny construct creature - Homunculus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 5, 'min_level': 1, 'level': 1, 'STR': 4, 'DEX': 15, 'CON': 11, 'INT': 10, 'WIS': 10, 'CHAR': 7, 'armor_class': 13, 'alignment': 'neutral Armor Class  13 (natural armor) Hit Points  5 (2d4) Speed  20 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['telepathic_bond', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def telepathic_bond(self) -> str:
        """While the homunculus is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically."""
        return 'While the homunculus is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or be poisoned for 1 minute. If the saving throw fails by 5 or more, the target is instead poisoned for 5 (1d10) minutes and unconscious while poisoned in this way."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or be poisoned for 1 minute. If the saving throw fails by 5 or more, the target is instead poisoned for 5 (1d10) minutes and unconscious while poisoned in this way.'

