# bases1/ice-mephit.py
"""
IceMephit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ice-mephit
"""
from creature_base import GlobalCreatureBaseClass


class IceMephit(GlobalCreatureBaseClass):
    """
    Small elemental creature - IceMephit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 21, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 13, 'CON': 10, 'INT': 9, 'WIS': 11, 'CHAR': 12, 'armor_class': 11, 'alignment': 'neutral evil Armor Class  11 Hit Points  21 (6d6) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_burst', 'claws', 'frost_breath_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_burst(self) -> str:
        """When the mephit dies, it explodes in a burst of jagged ice. Each creature within 5 feet of it must make a DC 10 Dexterity saving throw, taking 4 (1d8) slashing damage on a failed save, or half as much"""
        return 'When the mephit dies, it explodes in a burst of jagged ice. Each creature within 5 feet of it must make a DC 10 Dexterity saving throw, taking 4 (1d8) slashing damage on a failed save, or half as much'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) slashing damage plus 2 (1d4) cold damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) slashing damage plus 2 (1d4) cold damage.'

    def frost_breath_(recharge_6)_attack(self) -> str:
        """The mephit exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC 10 Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one."""
        return 'The mephit exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC 10 Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one.'

