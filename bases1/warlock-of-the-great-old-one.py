# bases1/warlock-of-the-great-old-one.py
"""
WarlockOfTheGreatOldOne creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=warlock-of-the-great-old-one
"""
from creature_base import GlobalCreatureBaseClass


class WarlockOfTheGreatOldOne(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - WarlockOfTheGreatOldOne
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 91, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 16, 'CON': 15, 'INT': 12, 'WIS': 12, 'CHAR': 18, 'armor_class': 13, 'alignment': 'any alignment Armor Class  13 (16 with  mage armor ) Hit Points  91 (14d8 + 28) Speed  30 ft. STR 9 (-1) DEX 16 (+3) CON 15 (+2) INT 12 (+1) WIS 12 (+1) CHA 18 (+4) Saving Throws  Wis +4', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['whispering_aura', 'multiattack', 'dagger', 'howling_void', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def whispering_aura(self) -> str:
        """At the start of each of the warlock's turns, each creature of its choice within 10 feet of it must succeed on a DC 15 Wisdom saving throw or take 10 (3d6) psychic damage, provided that the warlock isn"""
        return "At the start of each of the warlock's turns, each creature of its choice within 10 feet of it must succeed on a DC 15 Wisdom saving throw or take 10 (3d6) psychic damage, provided that the warlock isn"

    def multiattack_attack(self) -> str:
        """The warlock makes two Dagger attacks."""
        return 'The warlock makes two Dagger attacks.'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 10 (3d6) psychic damage."""
        return 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 10 (3d6) psychic damage.'

    def howling_void_attack(self) -> str:
        """The warlock opens a momentary extraplanar rift within 60 feet of it. The rift is a scream-filled, 20-foot cube. Each creature in that area must make a DC 15 Wisdom saving throw. On a failed save, a creature takes 9 (2d8) psychic damage and is frightened of the warlock until the start of the warlock's next turn. On a successful save, a creature takes half as much damage and isn't frightened."""
        return "The warlock opens a momentary extraplanar rift within 60 feet of it. The rift is a scream-filled, 20-foot cube. Each creature in that area must make a DC 15 Wisdom saving throw. On a failed save, a creature takes 9 (2d8) psychic damage and is frightened of the warlock until the start of the warlock's next turn. On a successful save, a creature takes half as much damage and isn't frightened."

    def spellcasting_attack(self) -> str:
        """The warlock casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 15):"""
        return 'The warlock casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 15):'

