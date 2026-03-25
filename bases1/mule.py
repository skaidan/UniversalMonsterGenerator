# bases1/mule.py
"""
Mule creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mule
"""
from creature_base import GlobalCreatureBaseClass


class Mule(GlobalCreatureBaseClass):
    """
    Medium beast creature - Mule
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 10, 'CON': 13, 'INT': 2, 'WIS': 10, 'CHAR': 5, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  11 (2d8 + 2) Speed  40 ft. STR 14 (+2) DEX 10 (+0) CON 13 (+1) INT 2 (-4) WIS 10 (+0) CHA 5 (-3) Senses  passive Perception 10 Languages  — Challenge  1/8 (25 XP) Beast of Burden . The mule is considered to be a Large animal for the purpose of determining its carrying capacity. Sure-Footed . The mule has advantage on Strength and Dexterity saving throws made against effects that would knock it prone. Actions Hooves .  Melee Weapon Attack : +2 to hit', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['beast_of_burden', 'hooves']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def beast_of_burden(self) -> str:
        """The mule is considered to be a Large animal for the purpose of determining its carrying capacity.Sure-Footed. The mule has advantage on Strength and Dexterity saving throws made against effects that w"""
        return 'The mule is considered to be a Large animal for the purpose of determining its carrying capacity.Sure-Footed. The mule has advantage on Strength and Dexterity saving throws made against effects that w'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage.'

