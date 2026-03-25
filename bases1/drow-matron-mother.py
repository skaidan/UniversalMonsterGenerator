# bases1/drow-matron-mother.py
"""
DrowMatronMother creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-matron-mother
"""
from creature_base import GlobalCreatureBaseClass


class DrowMatronMother(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Cleric creature - DrowMatronMother
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 247, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 18, 'CON': 16, 'INT': 17, 'WIS': 21, 'CHAR': 22, 'armor_class': 17, 'alignment': 'Elf)', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Cleric', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['special_equipment', 'multiattack', 'demon_staff', 'tentacle_rod', 'divine_flame_(2/day)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def special_equipment(self) -> str:
        """The drow wields a tentacle rod.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in sunlight, the drow has """
        return "The drow wields a tentacle rod.Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Sunlight Sensitivity. While in sunlight, the drow has "

    def multiattack_attack(self) -> str:
        """The drow makes two Demon Staff attacks or one Demon Staff attack and three Tentacle Rod attacks."""
        return 'The drow makes two Demon Staff attacks or one Demon Staff attack and three Tentacle Rod attacks.'

    def demon_staff_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage, or 8 (1d8 + 4) bludgeoning damage if used with two hands, plus 14 (4d6) psychic damage. The target must succeed on a DC 19 Wisdom saving throw or become frightened of the drow for 1 minute. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage, or 8 (1d8 + 4) bludgeoning damage if used with two hands, plus 14 (4d6) psychic damage. The target must succeed on a DC 19 Wisdom saving throw or become frightened of the drow for 1 minute. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def tentacle_rod_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 15 ft., one creature. Hit: 3 (1d6) bludgeoning damage. If the target is hit three times by the rod on one turn, the target must succeed on a DC 15 Constitution saving throw or suffer the following effects for 1 minute: the target's speed is halved, it has disadvantage on Dexterity saving throws, and it can't use reactions. Moreover, on each of its turns, it can take either an action or a bonus action, but not both. At the end of each of its turns, it can repeat the saving throw, ending the effect on itself on a success."""
        return "Melee Weapon Attack: +9 to hit, reach 15 ft., one creature. Hit: 3 (1d6) bludgeoning damage. If the target is hit three times by the rod on one turn, the target must succeed on a DC 15 Constitution saving throw or suffer the following effects for 1 minute: the target's speed is halved, it has disadvantage on Dexterity saving throws, and it can't use reactions. Moreover, on each of its turns, it can take either an action or a bonus action, but not both. At the end of each of its turns, it can repeat the saving throw, ending the effect on itself on a success."

    def divine_flame_(2/day)_attack(self) -> str:
        """A 10-foot-radius, 40-foot-high column of divine fire sprouts in an area up to 120 feet away from the drow. Each creature in the column must make a DC 20 Dexterity saving throw, taking 14 (4d6) fire damage and 14 (4d6) radiant damage on a failed save, or half as much damage on a successful one."""
        return 'A 10-foot-radius, 40-foot-high column of divine fire sprouts in an area up to 120 feet away from the drow. Each creature in the column must make a DC 20 Dexterity saving throw, taking 14 (4d6) fire damage and 14 (4d6) radiant damage on a failed save, or half as much damage on a successful one.'

    def spellcasting_attack(self) -> str:
        """The drow casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 20):"""
        return 'The drow casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 20):'

