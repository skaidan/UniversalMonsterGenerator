# bases1/quasit.py
"""
Quasit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quasit
"""
from creature_base import GlobalCreatureBaseClass


class Quasit(GlobalCreatureBaseClass):
    """
    Tiny Fiend (Demon creature - Quasit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 5, 'DEX': 17, 'CON': 10, 'INT': 7, 'WIS': 10, 'CHAR': 10, 'armor_class': 13, 'alignment': 'Shapechanger)', 'legendary': False, 'size': 'Tiny', 'type': 'Fiend (Demon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'claws_(bite_in_beast_form)', 'scare_(1/day)', 'invisibility']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The quasit can use its action to polymorph into a beast form that resembles a bat (speed 10 ft. fly 40 ft.), a centipede (40 ft., climb 40 ft.), or a toad (40 ft., swim 40 ft.), or back into its true """
        return 'The quasit can use its action to polymorph into a beast form that resembles a bat (speed 10 ft. fly 40 ft.), a centipede (40 ft., climb 40 ft.), or a toad (40 ft., swim 40 ft.), or back into its true '

    def claws_(bite_in_beast_form)_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage, and the target must succeed on a DC 10 Constitution saving throw or take 5 (2d4) poison damage and become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage, and the target must succeed on a DC 10 Constitution saving throw or take 5 (2d4) poison damage and become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def scare_(1/day)_attack(self) -> str:
        """One creature of the quasit's choice within 20 feet of it must succeed on a DC 10 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the quasit is within line of sight, ending the effect on itself on a success."""
        return "One creature of the quasit's choice within 20 feet of it must succeed on a DC 10 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the quasit is within line of sight, ending the effect on itself on a success."

    def invisibility_attack(self) -> str:
        """The quasit magically turns invisible until it attacks or uses Scare, or until its concentration ends (as if concentrating on a spell). Any equipment the quasit wears or carries is invisible with it."""
        return 'The quasit magically turns invisible until it attacks or uses Scare, or until its concentration ends (as if concentrating on a spell). Any equipment the quasit wears or carries is invisible with it.'

