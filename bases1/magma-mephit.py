# bases1/magma-mephit.py
"""
MagmaMephit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=magma-mephit
"""
from creature_base import GlobalCreatureBaseClass


class MagmaMephit(GlobalCreatureBaseClass):
    """
    Small elemental creature - MagmaMephit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 12, 'CON': 12, 'INT': 7, 'WIS': 10, 'CHAR': 10, 'armor_class': 11, 'alignment': 'neutral evil Armor Class  11 Hit Points  22 (5d6 + 5) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_burst', 'claws', 'fire_breath_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_burst(self) -> str:
        """When the mephit dies, it explodes in a burst of lava. Each creature within 5 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on"""
        return 'When the mephit dies, it explodes in a burst of lava. Each creature within 5 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) slashing damage plus 2 (1d4) fire damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) slashing damage plus 2 (1d4) fire damage.'

    def fire_breath_(recharge_6)_attack(self) -> str:
        """The mephit exhales a 15-foot cone of fire. Each creature in that area must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one."""
        return 'The mephit exhales a 15-foot cone of fire. Each creature in that area must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one.'

