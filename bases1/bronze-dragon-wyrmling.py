# bases1/bronze-dragon-wyrmling.py
"""
BronzeDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bronze-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class BronzeDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Metallic) creature - BronzeDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 15, 'INT': 12, 'WIS': 11, 'CHAR': 15, 'armor_class': 17, 'alignment': 'lawful good Armor Class  17 (natural armor) Hit Points  32 (5d8 + 10) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Metallic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'bite', 'breath_weapons_(recharge_5-6)', 'lightning_breath', 'repulsion_breath']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The dragon can breathe air and water."""
        return 'The dragon can breathe air and water.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage.'

    def breath_weapons_(recharge_5-6)_attack(self) -> str:
        """The dragon uses one of the following breath weapons."""
        return 'The dragon uses one of the following breath weapons.'

    def lightning_breath_attack(self) -> str:
        """The dragon exhales lightning in a 40-foot line that is 5 feet wide. Each creature in that line must make a DC 12 Dexterity saving throw, taking 16 (3d10) lightning damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales lightning in a 40-foot line that is 5 feet wide. Each creature in that line must make a DC 12 Dexterity saving throw, taking 16 (3d10) lightning damage on a failed save, or half as much damage on a successful one.'

    def repulsion_breath_attack(self) -> str:
        """The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 12 Strength saving throw. On a failed save, the creature is pushed 30 feet away from the dragon."""
        return 'The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 12 Strength saving throw. On a failed save, the creature is pushed 30 feet away from the dragon.'

