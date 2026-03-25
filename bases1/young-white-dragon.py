# bases1/young-white-dragon.py
"""
YoungWhiteDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-white-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungWhiteDragon(GlobalCreatureBaseClass):
    """
    Large dragon (Chromatic) creature - YoungWhiteDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 133, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 18, 'INT': 6, 'WIS': 11, 'CHAR': 12, 'armor_class': 17, 'alignment': 'chaotic evil Armor Class  17 (natural armor) Hit Points  133 (14d10 + 56) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['ice_walk', 'multiattack', 'bite', 'claw', 'cold_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def ice_walk(self) -> str:
        """The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra moment."""
        return "The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra moment."

    def multiattack_attack(self) -> str:
        """The dragon makes three attacks: one with its bite and two with its claws."""
        return 'The dragon makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) piercing damage plus 4 (1d8) cold damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15 (2d10 + 4) piercing damage plus 4 (1d8) cold damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.'

    def cold_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales an icy blast in a 30-foot cone. Each creature in that area must make a DC 15 Constitution saving throw, taking 45 (10d8) cold damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales an icy blast in a 30-foot cone. Each creature in that area must make a DC 15 Constitution saving throw, taking 45 (10d8) cold damage on a failed save, or half as much damage on a successful one.'

