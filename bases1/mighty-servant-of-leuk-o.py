# bases1/mighty-servant-of-leuk-o.py
"""
MightyServantOfLeukO creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mighty-servant-of-leuk-o
"""
from creature_base import GlobalCreatureBaseClass


class MightyServantOfLeukO(GlobalCreatureBaseClass):
    """
    Huge construct creature - MightyServantOfLeukO
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 310, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 14, 'CON': 20, 'INT': 1, 'WIS': 14, 'CHAR': 10, 'armor_class': 22, 'alignment': '- Armor Class  22 (natural armor) Hit Points  310 (27d12 + 135) Speed  60 ft. STR 30 (+10) DEX 14 (+2) CON 20 (+5) INT 1 (-5) WIS 14 (+2) CHA 10 (+0) Saving Throws  Wis +9', 'legendary': False, 'size': 'Huge', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['immutable_existence', 'destructive_fist', 'crushing_leap']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def immutable_existence(self) -> str:
        """The servant is immune to any spell or effect that would alter its form or send it to another plane of existence.Magic Resistant Construction. The servant has advantage on saving throws against spells """
        return 'The servant is immune to any spell or effect that would alter its form or send it to another plane of existence.Magic Resistant Construction. The servant has advantage on saving throws against spells '

    def destructive_fist_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +17 to hit, reach 10 ft. or range 120 ft., one target. Hit: 36 (4d12 + 10) force damage. If the target is an object, it takes triple damage."""
        return 'Melee or Ranged Weapon Attack: +17 to hit, reach 10 ft. or range 120 ft., one target. Hit: 36 (4d12 + 10) force damage. If the target is an object, it takes triple damage.'

    def crushing_leap_attack(self) -> str:
        """If the servant jumps at least 25 feet as part of its movement, it can then use this action to land on its feet in a space that contains one or more other creatures. Each of those creatures is pushed to an unoccupied space within 5 feet of the servant and must make a DC 25 Dexterity saving throw. On a failed save, a creature takes 26 (4d12) bludgeoning damage and is knocked prone. On a successful save, a creature takes half as much damage and isn't knocked prone."""
        return "If the servant jumps at least 25 feet as part of its movement, it can then use this action to land on its feet in a space that contains one or more other creatures. Each of those creatures is pushed to an unoccupied space within 5 feet of the servant and must make a DC 25 Dexterity saving throw. On a failed save, a creature takes 26 (4d12) bludgeoning damage and is knocked prone. On a successful save, a creature takes half as much damage and isn't knocked prone."

