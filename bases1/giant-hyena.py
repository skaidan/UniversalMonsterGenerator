# bases1/giant-hyena.py
"""
GiantHyena creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-hyena
"""
from creature_base import GlobalCreatureBaseClass


class GiantHyena(GlobalCreatureBaseClass):
    """
    Large beast creature - GiantHyena
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 14, 'INT': 2, 'WIS': 12, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  45 (6d10 + 12) Speed  50 ft. STR 16 (+3) DEX 14 (+2) CON 14 (+2) INT 2 (-4) WIS 12 (+1) CHA 7 (-2) Skills  Perception +3 Senses  passive Perception 13 Languages  — Challenge  1 (200 XP) Rampage . When the hyena reduces a creature to 0 hit points with a melee attack on its turn', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['rampage', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def rampage(self) -> str:
        """When the hyena reduces a creature to 0 hit points with a melee attack on its turn, the hyena can take a bonus action to move up to half its speed and make a bite attack."""
        return 'When the hyena reduces a creature to 0 hit points with a melee attack on its turn, the hyena can take a bonus action to move up to half its speed and make a bite attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage.'

