# bases1/fomorian.py
"""
Fomorian creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fomorian
"""
from creature_base import GlobalCreatureBaseClass


class Fomorian(GlobalCreatureBaseClass):
    """
    Huge giant creature - Fomorian
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 149, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 10, 'CON': 20, 'INT': 9, 'WIS': 14, 'CHAR': 6, 'armor_class': 14, 'alignment': 'chaotic evil Armor Class  14 (natural armor) Hit Points  149 (13d12 + 65) Speed  30 ft. STR 23 (+6) DEX 10 (+0) CON 20 (+5) INT 9 (-1) WIS 14 (+2) CHA 6 (-2) Skills  Perception +8', 'legendary': False, 'size': 'Huge', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'greatclub', 'evil_eye', 'curse_of_the_evil_eye_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The fomorian attacks twice with its greatclub or makes one greatclub attack and uses Evil Eye once."""
        return 'The fomorian attacks twice with its greatclub or makes one greatclub attack and uses Evil Eye once.'

    def greatclub_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage.'

    def evil_eye_attack(self) -> str:
        """The fomorian magically forces a creature it can see within 60 feet of it to make a DC 14 Charisma saving throw. The creature takes 27 (6d8) psychic damage on a failed save, or half as much damage on a successful one."""
        return 'The fomorian magically forces a creature it can see within 60 feet of it to make a DC 14 Charisma saving throw. The creature takes 27 (6d8) psychic damage on a failed save, or half as much damage on a successful one.'

    def curse_of_the_evil_eye_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """With a stare, the fomorian uses Evil Eye, but on a failed save, the creature is also cursed with magical deformities. While deformed, the creature has its speed halved and has disadvantage on ability checks, saving throws, and attacks based on Strength or Dexterity. The transformed creature can repeat the saving throw whenever it finishes a long rest, ending the effect on a success."""
        return 'With a stare, the fomorian uses Evil Eye, but on a failed save, the creature is also cursed with magical deformities. While deformed, the creature has its speed halved and has disadvantage on ability checks, saving throws, and attacks based on Strength or Dexterity. The transformed creature can repeat the saving throw whenever it finishes a long rest, ending the effect on a success.'

