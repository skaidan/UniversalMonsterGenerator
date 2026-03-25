# bases1/brass-dragon-wyrmling.py
"""
BrassDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=brass-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class BrassDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Metallic) creature - BrassDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 16, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 13, 'INT': 10, 'WIS': 11, 'CHAR': 13, 'armor_class': 16, 'alignment': 'chaotic good Armor Class  16 (natural armor) Hit Points  16 (3d8 + 3) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Metallic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite', 'breath_weapons_(recharge_5-6)', 'fire_breath', 'sleep_breath']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10 + 2) piercing damage.'

    def breath_weapons_(recharge_5-6)_attack(self) -> str:
        """The dragon uses one of the following breath weapons."""
        return 'The dragon uses one of the following breath weapons.'

    def fire_breath_attack(self) -> str:
        """The dragon exhales fire in an 20-foot line that is 5 feet wide. Each creature in that line must make a DC 11 Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales fire in an 20-foot line that is 5 feet wide. Each creature in that line must make a DC 11 Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one.'

    def sleep_breath_attack(self) -> str:
        """The dragon exhales sleep gas in a 15-foot cone. Each creature in that area must succeed on a DC 11 Constitution saving throw or fall unconscious for 1 minute. This effect ends for a creature if the creature takes damage or someone uses an action to wake it."""
        return 'The dragon exhales sleep gas in a 15-foot cone. Each creature in that area must succeed on a DC 11 Constitution saving throw or fall unconscious for 1 minute. This effect ends for a creature if the creature takes damage or someone uses an action to wake it.'

