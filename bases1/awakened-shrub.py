# bases1/awakened-shrub.py
"""
AwakenedShrub creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=awakened-shrub
"""
from creature_base import GlobalCreatureBaseClass


class AwakenedShrub(GlobalCreatureBaseClass):
    """
    Small plant creature - AwakenedShrub
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 8, 'CON': 11, 'INT': 10, 'WIS': 10, 'CHAR': 6, 'armor_class': 9, 'alignment': 'unaligned Armor Class  9 Hit Points  10 (3d6) Speed  20 ft. STR 3 (-4) DEX 8 (-1) CON 11 (+0) INT 10 (+0) WIS 10 (+0) CHA 6 (-2) Damage Vulnerabilities  fire Damage Resistances  piercing Senses  passive Perception 10 Languages  one language known by its creator Challenge  0 (10 XP) False Appearance . While the shrub remains motionless', 'legendary': False, 'size': 'Small', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'rake']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the shrub remains motionless, it is indistinguishable from a normal shrub."""
        return 'While the shrub remains motionless, it is indistinguishable from a normal shrub.'

    def rake_attack(self) -> str:
        """Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) slashing damage."""
        return 'Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) slashing damage.'

