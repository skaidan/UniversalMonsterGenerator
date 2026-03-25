# bases1/berserker.py
"""
Berserker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=berserker
"""
from creature_base import GlobalCreatureBaseClass


class Berserker(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Berserker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 17, 'INT': 9, 'WIS': 11, 'CHAR': 9, 'armor_class': 13, 'alignment': 'any chaotic alignment Armor Class  13 (hide armor) Hit Points  67 (9d8 + 27) Speed  30 ft. STR 16 (+3) DEX 12 (+1) CON 17 (+3) INT 9 (-1) WIS 11 (+0) CHA 9 (-1) Senses  passive Perception 10 Languages  any one language (usually Common) Challenge  2 (450 XP) Reckless . At the start of its turn', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['reckless', 'greataxe']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def reckless(self) -> str:
        """At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."""
        return 'At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn.'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d12 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d12 + 3) slashing damage.'

