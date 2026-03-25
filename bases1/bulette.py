# bases1/bulette.py
"""
Bulette creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bulette
"""
from creature_base import GlobalCreatureBaseClass


class Bulette(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Bulette
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 94, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 11, 'CON': 21, 'INT': 2, 'WIS': 10, 'CHAR': 5, 'armor_class': 17, 'alignment': 'unaligned Armor Class  17 (natural armor) Hit Points  94 (9d10 + 45) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['standing_leap', 'bite', 'deadly_leap']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def standing_leap(self) -> str:
        """The bulette's long jump is up to 30 feet and its high jump is up to 15 feet, with or without a running start."""
        return "The bulette's long jump is up to 30 feet and its high jump is up to 15 feet, with or without a running start."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 30 (4d12 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 30 (4d12 + 4) piercing damage.'

    def deadly_leap_attack(self) -> str:
        """If the bulette jumps at least 15 feet as part of its movement, it can then use this action to land on its feet in a space that contains one or more other creatures. Each of those creatures must succeed on a DC 16 Strength or Dexterity saving throw (target's choice) or be knocked prone and take 14 (3d6 + 4) bludgeoning damage plus 14 (3d6 + 4) slashing damage. On a successful save, the creature takes only half the damage, isn't knocked prone, and is pushed 5 feet out of the bulette's space into an unoccupied space of the creature's choice. If no unoccupied space is within range, the creature instead falls prone in the bulette's space."""
        return "If the bulette jumps at least 15 feet as part of its movement, it can then use this action to land on its feet in a space that contains one or more other creatures. Each of those creatures must succeed on a DC 16 Strength or Dexterity saving throw (target's choice) or be knocked prone and take 14 (3d6 + 4) bludgeoning damage plus 14 (3d6 + 4) slashing damage. On a successful save, the creature takes only half the damage, isn't knocked prone, and is pushed 5 feet out of the bulette's space into an unoccupied space of the creature's choice. If no unoccupied space is within range, the creature instead falls prone in the bulette's space."

