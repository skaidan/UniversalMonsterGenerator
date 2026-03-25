# bases1/ankylosaurus.py
"""
Ankylosaurus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ankylosaurus
"""
from creature_base import GlobalCreatureBaseClass


class Ankylosaurus(GlobalCreatureBaseClass):
    """
    Huge beast creature - Ankylosaurus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 11, 'CON': 15, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  68 (8d12 + 16) Speed  30 ft. STR 19 (+4) DEX 11 (+0) CON 15 (+2) INT 2 (-4) WIS 12 (+1) CHA 5 (-3) Senses  passive Perception 11 Languages  — Challenge  3 (700 XP) Actions Tail .  Melee Weapon Attack : +7 to hit', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['tail']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 18 (4d6 + 4) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 18 (4d6 + 4) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone.'

