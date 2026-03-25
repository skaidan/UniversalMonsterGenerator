# bases1/androsphinx.py
"""
Androsphinx creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=androsphinx
"""
from creature_base import GlobalCreatureBaseClass


class Androsphinx(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Androsphinx
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 199, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 10, 'CON': 20, 'INT': 16, 'WIS': 18, 'CHAR': 23, 'armor_class': 17, 'alignment': 'lawful neutral Armor Class  17 (natural armor) Hit Points  199 (19d10 + 95) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['inscrutable', 'multiattack', 'claw', 'roar_(3/day)', 'first_roar', 'second_roar', 'third_roar']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def inscrutable(self) -> str:
        """The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intention"""
        return "The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intention"

    def multiattack_attack(self) -> str:
        """The sphinx makes two claw attacks."""
        return 'The sphinx makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 17 (2d10 + 6) slashing damage."""
        return 'Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 17 (2d10 + 6) slashing damage.'

    def roar_(3/day)_attack(self) -> str:
        """The sphinx emits a magical roar. Each time it roars before finishing a long rest, the roar is louder and the effect is different, as detailed below. Each creature within 500 feet of the sphinx and able to hear the roar must make a saving throw."""
        return 'The sphinx emits a magical roar. Each time it roars before finishing a long rest, the roar is louder and the effect is different, as detailed below. Each creature within 500 feet of the sphinx and able to hear the roar must make a saving throw.'

    def first_roar_attack(self) -> str:
        """Each creature that fails a DC 18 Wisdom saving throw is frightened for 1 minute. A frightened creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Each creature that fails a DC 18 Wisdom saving throw is frightened for 1 minute. A frightened creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def second_roar_attack(self) -> str:
        """Each creature that fails a DC 18 Wisdom saving throw is deafened and frightened for 1 minute. A frightened creature is paralyzed and can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Each creature that fails a DC 18 Wisdom saving throw is deafened and frightened for 1 minute. A frightened creature is paralyzed and can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def third_roar_attack(self) -> str:
        """Each creature makes a DC 18 Constitution saving throw. On a failed save, a creature takes 44 (8d10) thunder damage and is knocked prone. On a successful save, the creature takes half as much damage and isn't knocked prone."""
        return "Each creature makes a DC 18 Constitution saving throw. On a failed save, a creature takes 44 (8d10) thunder damage and is knocked prone. On a successful save, the creature takes half as much damage and isn't knocked prone."

