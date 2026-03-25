# bases1/dragon-turtle.py
"""
DragonTurtle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragon-turtle
"""
from creature_base import GlobalCreatureBaseClass


class DragonTurtle(GlobalCreatureBaseClass):
    """
    Gargantuan dragon creature - DragonTurtle
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 341, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 10, 'CON': 20, 'INT': 10, 'WIS': 12, 'CHAR': 12, 'armor_class': 20, 'alignment': 'neutral Armor Class  20 (natural armor) Hit Points  341 (22d20 + 110) Speed  20 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'bite', 'claw', 'tail', 'steam_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The dragon turtle can breathe air and water."""
        return 'The dragon turtle can breathe air and water.'

    def multiattack_attack(self) -> str:
        """The dragon turtle makes three attacks: one with its bite and two with its claws. It can make one tail attack in place of its two claw attacks."""
        return 'The dragon turtle makes three attacks: one with its bite and two with its claws. It can make one tail attack in place of its two claw attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 26 (3d12 + 7) piercing damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 26 (3d12 + 7) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 16 (2d8 + 7) slashing damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 16 (2d8 + 7) slashing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 26 (3d12 + 7) bludgeoning damage. If the target is a creature, it must succeed on a DC 20 Strength saving throw or be pushed up to 10 feet away from the dragon turtle and knocked prone."""
        return 'Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 26 (3d12 + 7) bludgeoning damage. If the target is a creature, it must succeed on a DC 20 Strength saving throw or be pushed up to 10 feet away from the dragon turtle and knocked prone.'

    def steam_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon turtle exhales scalding steam in a 60-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 52 (15d 6) fire damage on a failed save, or half as much damage on a successful one. Being underwater doesn't grant resistance against this damage."""
        return "The dragon turtle exhales scalding steam in a 60-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 52 (15d 6) fire damage on a failed save, or half as much damage on a successful one. Being underwater doesn't grant resistance against this damage."

