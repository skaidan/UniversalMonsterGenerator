# bases1/young-silver-dragon.py
"""
YoungSilverDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-silver-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungSilverDragon(GlobalCreatureBaseClass):
    """
    Large dragon (Metallic) creature - YoungSilverDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 168, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 10, 'CON': 21, 'INT': 14, 'WIS': 11, 'CHAR': 19, 'armor_class': 18, 'alignment': 'lawful good Armor Class  18 (natural armor) Hit Points  168 (16d10 + 80) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon (Metallic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'claw', 'breath_weapons_(recharge_5-6)', 'cold_breath', 'paralyzing_breath']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The dragon makes three attacks: one with its bite and two with its claws."""
        return 'The dragon makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.'

    def breath_weapons_(recharge_5-6)_attack(self) -> str:
        """The dragon uses one of the following breath weapons."""
        return 'The dragon uses one of the following breath weapons.'

    def cold_breath_attack(self) -> str:
        """The dragon exhales an icy blast in a 30-foot cone. Each creature in that area must make a DC 17 Constitution saving throw, taking 54 (12d8) cold damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales an icy blast in a 30-foot cone. Each creature in that area must make a DC 17 Constitution saving throw, taking 54 (12d8) cold damage on a failed save, or half as much damage on a successful one.'

    def paralyzing_breath_attack(self) -> str:
        """The dragon exhales paralyzing gas in a 30-foot cone. Each creature in that area must succeed on a DC 17 Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The dragon exhales paralyzing gas in a 30-foot cone. Each creature in that area must succeed on a DC 17 Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

