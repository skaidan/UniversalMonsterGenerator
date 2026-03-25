# bases1/skull-lord.py
"""
SkullLord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=skull-lord
"""
from creature_base import GlobalCreatureBaseClass


class SkullLord(GlobalCreatureBaseClass):
    """
    Medium Undead (Sorcerer) creature - SkullLord
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 112, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 16, 'CON': 17, 'INT': 16, 'WIS': 15, 'CHAR': 21, 'armor_class': 18, 'alignment': 'typically Lawful Evil Armor Class  18 (plate) Hit Points  112 (15d8 + 45) Speed  30 ft. STR 14 (+2) DEX 16 (+3) CON 17 (+3) INT 16 (+3) WIS 15 (+2) CHA 21 (+5) Skills  Athletics +7', 'legendary': False, 'size': 'Medium', 'type': 'Undead (Sorcerer)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['evasion', 'multiattack', 'bone_staff', 'deathly_ray', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def evasion(self) -> str:
        """If the skull lord is subjected to an effect that allows it to make a Dexterity saving throw to take only half the damage, the skull lord instead takes no damage if it succeeds on the saving throw and """
        return 'If the skull lord is subjected to an effect that allows it to make a Dexterity saving throw to take only half the damage, the skull lord instead takes no damage if it succeeds on the saving throw and '

    def multiattack_attack(self) -> str:
        """The skull lord makes three Bone Staff or Deathly Ray attacks."""
        return 'The skull lord makes three Bone Staff or Deathly Ray attacks.'

    def bone_staff_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage plus 21 (6d6) necrotic damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage plus 21 (6d6) necrotic damage.'

    def deathly_ray_attack(self) -> str:
        """Ranged Spell Attack: +10 to hit, range 60 ft., one target. Hit: 27 (5d8 + 5) necrotic damage."""
        return 'Ranged Spell Attack: +10 to hit, range 60 ft., one target. Hit: 27 (5d8 + 5) necrotic damage.'

    def spellcasting_attack(self) -> str:
        """The skull, lord casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 18):"""
        return 'The skull, lord casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 18):'

