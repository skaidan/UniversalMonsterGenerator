# bases1/yochlol.py
"""
Yochlol creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yochlol
"""
from creature_base import GlobalCreatureBaseClass


class Yochlol(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon creature - Yochlol
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 18, 'INT': 13, 'WIS': 15, 'CHAR': 15, 'armor_class': 15, 'alignment': 'Shapechanger)', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack', 'slam_(bite_in_spider_form)', 'mist_form']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The yochlol can use its action to polymorph into a form that resembles a female drow or giant spider, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing """
        return 'The yochlol can use its action to polymorph into a form that resembles a female drow or giant spider, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing '

    def multiattack_attack(self) -> str:
        """The yochlol makes two melee attacks."""
        return 'The yochlol makes two melee attacks.'

    def slam_(bite_in_spider_form)_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft. (10 ft. in demon form), one target. Hit: 5 (1d6 + 2) bludgeoning (piercing in spider form) damage plus 21 (6d6) poison damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft. (10 ft. in demon form), one target. Hit: 5 (1d6 + 2) bludgeoning (piercing in spider form) damage plus 21 (6d6) poison damage.'

    def mist_form_attack(self) -> str:
        """The yochlol transforms into toxic mist or reverts to its true form. Any equipment it is wearing or carrying is also transformed. It reverts to its true form if it dies. While in mist form, the yochlol is incapacitated and can't speak. It has a flying speed of 30 feet, can hover, and can pass through any space that isn't airtight. It has advantage on Strength, Dexterity, and Constitution saving throws, and it is immune to nonmagical damage. While in mist form, the yochlol can enter a creature's space and stop there. Each time that creature starts its turn with the yochlol in its space, the creature must succeed on a DC 14 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target is incapacitated."""
        return "The yochlol transforms into toxic mist or reverts to its true form. Any equipment it is wearing or carrying is also transformed. It reverts to its true form if it dies. While in mist form, the yochlol is incapacitated and can't speak. It has a flying speed of 30 feet, can hover, and can pass through any space that isn't airtight. It has advantage on Strength, Dexterity, and Constitution saving throws, and it is immune to nonmagical damage. While in mist form, the yochlol can enter a creature's space and stop there. Each time that creature starts its turn with the yochlol in its space, the creature must succeed on a DC 14 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target is incapacitated."

