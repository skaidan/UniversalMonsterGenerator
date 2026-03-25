# bases1/meenlock.py
"""
Meenlock creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=meenlock
"""
from creature_base import GlobalCreatureBaseClass


class Meenlock(GlobalCreatureBaseClass):
    """
    Small Fey creature - Meenlock
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 31, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 15, 'CON': 12, 'INT': 11, 'WIS': 10, 'CHAR': 8, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  31 (7d6 + 7) Speed  30 ft. STR 7 (-2) DEX 15 (+2) CON 12 (+1) INT 11 (+0) WIS 10 (+0) CHA 8 (-1) Skills  Perception +4', 'legendary': False, 'size': 'Small', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fear_aura', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fear_aura(self) -> str:
        """Any Beast or Humanoid that starts its turn within 10 feet of the meenlock must succeed on a DC 11 Wisdom saving throw or be frightened until the start of the creature's next turn.Light Sensitivity. Wh"""
        return "Any Beast or Humanoid that starts its turn within 10 feet of the meenlock must succeed on a DC 11 Wisdom saving throw or be frightened until the start of the creature's next turn.Light Sensitivity. Wh"

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage, and the target must succeed on a DC 11 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage, and the target must succeed on a DC 11 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

