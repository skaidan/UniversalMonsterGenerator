# bases1/tribal-warrior.py
"""
TribalWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tribal-warrior
"""
from creature_base import GlobalCreatureBaseClass


class TribalWarrior(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - TribalWarrior
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 11, 'CON': 12, 'INT': 8, 'WIS': 11, 'CHAR': 8, 'armor_class': 12, 'alignment': "any alignment Armor Class  12 (hide armor) Hit Points  11 (2d8 + 2) Speed  30 ft. STR 13 (+1) DEX 11 (+0) CON 12 (+1) INT 8 (-1) WIS 11 (+0) CHA 8 (-1) Senses  passive Perception 10 Languages  any one language Challenge  1/8 (25 XP) Pack Tactics . The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated. Actions Spear .  Melee or Ranged Weapon Attack : +3 to hit", 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pack_tactics', 'spear']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pack_tactics(self) -> str:
        """The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated."""
        return "The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated."

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack.'

