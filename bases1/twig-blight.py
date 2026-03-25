# bases1/twig-blight.py
"""
TwigBlight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=twig-blight
"""
from creature_base import GlobalCreatureBaseClass


class TwigBlight(GlobalCreatureBaseClass):
    """
    Small plant creature - TwigBlight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 4, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 13, 'CON': 12, 'INT': 4, 'WIS': 8, 'CHAR': 3, 'armor_class': 13, 'alignment': 'neutral evil Armor Class  13 (natural armor) Hit Points  4 (1d6 + 1) Speed  20 ft. STR 6 (-2) DEX 13 (+1) CON 12 (+1) INT 4 (-3) WIS 8 (-1) CHA 3 (-4) Skills  Stealth +3 Damage Vulnerabilities  fire Condition Immunities  blinded', 'legendary': False, 'size': 'Small', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the blight remains motionless, it is indistinguishable from a dead shrub."""
        return 'While the blight remains motionless, it is indistinguishable from a dead shrub.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.'

