# bases1/mezzoloth.py
"""
Mezzoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mezzoloth
"""
from creature_base import GlobalCreatureBaseClass


class Mezzoloth(GlobalCreatureBaseClass):
    """
    Medium fiend (Yugoloth) creature - Mezzoloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 11, 'CON': 16, 'INT': 7, 'WIS': 10, 'CHAR': 11, 'armor_class': 18, 'alignment': 'neutral evil Armor Class  18 (natural armor) Hit Points  75 (10d8 + 30) Speed  40 ft. STR 18 (+4) DEX 11 (+0) CON 16 (+3) INT 7 (-2) WIS 10 (+0) CHA 11 (+0) Skills  Perception +3 Damage Resistances  cold', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'multiattack', 'claws', 'trident', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The mezzoloth's innate spellcasting ability is Charisma (spell save DC 11). The mezzoloth can innately cast the following spells, requiring no material components:2/day each: darkness, dispel magic1/d"""
        return "The mezzoloth's innate spellcasting ability is Charisma (spell save DC 11). The mezzoloth can innately cast the following spells, requiring no material components:2/day each: darkness, dispel magic1/d"

    def multiattack_attack(self) -> str:
        """The mezzoloth makes two attacks: one with its claws and one with its trident."""
        return 'The mezzoloth makes two attacks: one with its claws and one with its trident.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) slashing damage.'

    def trident_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 7 (1d6 + 4) piercing damage, or 8 (1d8 + 4) piercing damage when held with two claws and used to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 7 (1d6 + 4) piercing damage, or 8 (1d8 + 4) piercing damage when held with two claws and used to make a melee attack.'

    def teleport_attack(self) -> str:
        """The mezzoloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."""
        return 'The mezzoloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see.'

