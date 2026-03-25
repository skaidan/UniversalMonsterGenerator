# bases1/draconic-spirit.py
"""
DraconicSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draconic-spirit
"""
from creature_base import GlobalCreatureBaseClass


class DraconicSpirit(GlobalCreatureBaseClass):
    """
    Large dragon creature - DraconicSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 14, 'CON': 17, 'INT': 10, 'WIS': 14, 'CHAR': 14, 'armor_class': 14, 'alignment': 'neutral Armor Class  14 + the level of the spell (natural armor) Hit Points  50 + 10 for each spell level above 5th (the dragon has a number of Hit Dice [d10s] equal to the level of the spell) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shared_resistances', 'multiattack', 'rend', 'breath_weapon']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shared_resistances(self) -> str:
        """When you summon the dragon, choose one of its damage resistances. You have resistance to the chosen damage type until the spell ends."""
        return 'When you summon the dragon, choose one of its damage resistances. You have resistance to the chosen damage type until the spell ends.'

    def multiattack_attack(self) -> str:
        """The dragon makes a number of Rend attacks equal to half the spell's level (rounded down), and it uses Breath Weapon."""
        return "The dragon makes a number of Rend attacks equal to half the spell's level (rounded down), and it uses Breath Weapon."

    def rend_attack(self) -> str:
        """Melee Weapon Attack: your spell attack modifier to hit, reach 10 ft., one target. Hit: 1d6 + 4 + the spell's level piercing damage."""
        return "Melee Weapon Attack: your spell attack modifier to hit, reach 10 ft., one target. Hit: 1d6 + 4 + the spell's level piercing damage."

    def breath_weapon_attack(self) -> str:
        """The dragon exhales destructive energy in a 30-foot cone. Each creature in that area must make a Dexterity saving throw against your spell save DC. A creature takes 2d6 damage of a type this dragon has resistance to (your choice) on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales destructive energy in a 30-foot cone. Each creature in that area must make a Dexterity saving throw against your spell save DC. A creature takes 2d6 damage of a type this dragon has resistance to (your choice) on a failed save, or half as much damage on a successful one.'

