# bases1/retriever.py
"""
Retriever creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=retriever
"""
from creature_base import GlobalCreatureBaseClass


class Retriever(GlobalCreatureBaseClass):
    """
    Large Construct creature - Retriever
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 210, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 16, 'CON': 20, 'INT': 3, 'WIS': 11, 'CHAR': 4, 'armor_class': 19, 'alignment': 'typically Lawful Evil Armor Class  19 (natural armor) Hit Points  210 (20d10 + 100) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['faultless_tracker', 'multiattack', 'foreleg', 'force_beam', 'paralyzing_beam_(recharge_5–6)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def faultless_tracker(self) -> str:
        """The retriever is given a quarry by its master. The quarry can be a specific creature or object the master is personally acquainted with, or it can be a general type of creature or object the master ha"""
        return 'The retriever is given a quarry by its master. The quarry can be a specific creature or object the master is personally acquainted with, or it can be a general type of creature or object the master ha'

    def multiattack_attack(self) -> str:
        """The retriever makes two Foreleg attacks, and it uses Force Beam or Paralyzing Beam, if available."""
        return 'The retriever makes two Foreleg attacks, and it uses Force Beam or Paralyzing Beam, if available.'

    def foreleg_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 15 (2d8 + 6) slashing damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 15 (2d8 + 6) slashing damage.'

    def force_beam_attack(self) -> str:
        """The retriever targets one creature it can see within 60 feet of it. The target must make a DC 16 Dexterity saving throw, taking 27 (5d10) force damage on a failed save, or half as much damage on a successful one."""
        return 'The retriever targets one creature it can see within 60 feet of it. The target must make a DC 16 Dexterity saving throw, taking 27 (5d10) force damage on a failed save, or half as much damage on a successful one.'

    def paralyzing_beam_(recharge_5–6)_attack(self) -> str:
        """The retriever targets one creature it can see within 60 feet of it. The target must succeed on a DC 18 Constitution saving throw or be paralyzed for 1 minute. The paralyzed target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If the paralyzed creature is Medium or smaller, the retriever can pick it up as part of the retriever's move and walk or climb with it at full speed."""
        return "The retriever targets one creature it can see within 60 feet of it. The target must succeed on a DC 18 Constitution saving throw or be paralyzed for 1 minute. The paralyzed target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If the paralyzed creature is Medium or smaller, the retriever can pick it up as part of the retriever's move and walk or climb with it at full speed."

    def spellcasting_attack(self) -> str:
        """The retriever casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 13):"""
        return 'The retriever casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 13):'

