# bases1/umber-hulk.py
"""
UmberHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=umber-hulk
"""
from creature_base import GlobalCreatureBaseClass


class UmberHulk(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - UmberHulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 13, 'CON': 16, 'INT': 9, 'WIS': 10, 'CHAR': 10, 'armor_class': 18, 'alignment': 'chaotic evil Armor Class  18 (natural armor) Hit Points  93 (11d10 + 33) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['confusing_caze', 'multiattack', 'claw', 'mandibles']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def confusing_caze(self) -> str:
        """When a creature starts its turn within 30 feet of the umber hulk and is able to see the umber hulk's eyes, the umber hulk can magically force it to make a DC 15 Charisma saving throw, unless the umber"""
        return "When a creature starts its turn within 30 feet of the umber hulk and is able to see the umber hulk's eyes, the umber hulk can magically force it to make a DC 15 Charisma saving throw, unless the umber"

    def multiattack_attack(self) -> str:
        """The umber hulk makes three attacks: two with its claws and one with its mandibles."""
        return 'The umber hulk makes three attacks: two with its claws and one with its mandibles.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage.'

    def mandibles_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage.'

