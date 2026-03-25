# bases1/violet-fungus.py
"""
VioletFungus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=violet-fungus
"""
from creature_base import GlobalCreatureBaseClass


class VioletFungus(GlobalCreatureBaseClass):
    """
    Medium plant creature - VioletFungus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 1, 'CON': 10, 'INT': 1, 'WIS': 3, 'CHAR': 1, 'armor_class': 5, 'alignment': 'unaligned Armor Class  5 Hit Points  18 (4d8) Speed  5 ft. STR 3 (-4) DEX 1 (-5) CON 10 (+0) INT 1 (-5) WIS 3 (-4) CHA 1 (-5) Condition Immunities  blinded', 'legendary': False, 'size': 'Medium', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'multiattack', 'rotting_touch']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the violet fungus remains motionless, it is indistinguishable from an ordinary fungus."""
        return 'While the violet fungus remains motionless, it is indistinguishable from an ordinary fungus.'

    def multiattack_attack(self) -> str:
        """The fungus makes 1d4 Rotting Touch attacks."""
        return 'The fungus makes 1d4 Rotting Touch attacks.'

    def rotting_touch_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 10 ft., one creature. Hit: 4 (1d8) necrotic damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 10 ft., one creature. Hit: 4 (1d8) necrotic damage.'

