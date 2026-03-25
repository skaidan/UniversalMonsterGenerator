# bases1/fire-elemental.py
"""
FireElemental creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-elemental
"""
from creature_base import GlobalCreatureBaseClass


class FireElemental(GlobalCreatureBaseClass):
    """
    Large elemental creature - FireElemental
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 102, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 17, 'CON': 16, 'INT': 6, 'WIS': 10, 'CHAR': 7, 'armor_class': 13, 'alignment': 'neutral Armor Class  13 Hit Points  102 (12d10 + 36) Speed  50 ft. STR 10 (+0) DEX 17 (+3) CON 16 (+3) INT 6 (-2) WIS 10 (+0) CHA 7 (-2) Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fire_form', 'multiattack', 'touch']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fire_form(self) -> str:
        """The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire da"""
        return 'The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire da'

    def multiattack_attack(self) -> str:
        """The elemental makes two touch attacks."""
        return 'The elemental makes two touch attacks.'

    def touch_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 5 (1d10) fire damage at the start of each of its turns."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 5 (1d10) fire damage at the start of each of its turns.'

