# bases1/magmin.py
"""
Magmin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=magmin
"""
from creature_base import GlobalCreatureBaseClass


class Magmin(GlobalCreatureBaseClass):
    """
    Small elemental creature - Magmin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 9, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 15, 'CON': 12, 'INT': 8, 'WIS': 11, 'CHAR': 10, 'armor_class': 14, 'alignment': 'chaotic neutral Armor Class  14 (natural armor) Hit Points  9 (2d6 + 2) Speed  30 ft. STR 7 (-2) DEX 15 (+2) CON 12 (+1) INT 8 (-1) WIS 11 (+0) CHA 10 (+0) Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Small', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_burst', 'touch']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_burst(self) -> str:
        """When the magmin dies, it explodes in a burst of fire and magma. Each creature within 10 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as muc"""
        return 'When the magmin dies, it explodes in a burst of fire and magma. Each creature within 10 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as muc'

    def touch_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d6) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 3 (1d6) fire damage at the end of each of its turns."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d6) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 3 (1d6) fire damage at the end of each of its turns.'

