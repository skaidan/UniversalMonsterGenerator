# bases1/pseudodragon.py
"""
Pseudodragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pseudodragon
"""
from creature_base import GlobalCreatureBaseClass


class Pseudodragon(GlobalCreatureBaseClass):
    """
    Tiny dragon creature - Pseudodragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 15, 'CON': 13, 'INT': 10, 'WIS': 12, 'CHAR': 10, 'armor_class': 13, 'alignment': 'neutral good Armor Class  13 (natural armor) Hit Points  7 (2d4 + 2) Speed  15 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_senses', 'bite', 'sting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_senses(self) -> str:
        """The pseudodragon has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell.Magic Resistance. The pseudodragon has advantage on saving throws against spells and other magical ef"""
        return 'The pseudodragon has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell.Magic Resistance. The pseudodragon has advantage on saving throws against spells and other magical ef'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

    def sting_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or become poisoned for 1 hour. If the saving throw fails by 5 or more, the target falls unconscious for the same duration, or until it takes damage or another creature uses an action to shake it awake."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or become poisoned for 1 hour. If the saving throw fails by 5 or more, the target falls unconscious for the same duration, or until it takes damage or another creature uses an action to shake it awake.'

