# bases1/young-bronze-dragon.py
"""
YoungBronzeDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-bronze-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungBronzeDragon(GlobalCreatureBaseClass):
    """
    Large dragon (Metallic) creature - YoungBronzeDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 142, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 10, 'CON': 19, 'INT': 14, 'WIS': 13, 'CHAR': 17, 'armor_class': 18, 'alignment': 'lawful good Armor Class  18 (natural armor) Hit Points  142 (15d10 + 60) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon (Metallic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'bite', 'claw', 'breath_weapons_(recharge_5-6)', 'lightning_breath', 'repulsion_breath']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The dragon can breathe air and water."""
        return 'The dragon can breathe air and water.'

    def multiattack_attack(self) -> str:
        """The dragon makes three attacks: one with its bite and two with its claws."""
        return 'The dragon makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) piercing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage.'

    def breath_weapons_(recharge_5-6)_attack(self) -> str:
        """The dragon uses one of the following breath weapons."""
        return 'The dragon uses one of the following breath weapons.'

    def lightning_breath_attack(self) -> str:
        """The dragon exhales lightning in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 15 Dexterity saving throw, taking 55 (10d10) lightning damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales lightning in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 15 Dexterity saving throw, taking 55 (10d10) lightning damage on a failed save, or half as much damage on a successful one.'

    def repulsion_breath_attack(self) -> str:
        """The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 15 Strength saving throw. On a failed save, the creature is pushed 40 feet away from the dragon."""
        return 'The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 15 Strength saving throw. On a failed save, the creature is pushed 40 feet away from the dragon.'

