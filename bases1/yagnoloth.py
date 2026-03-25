# bases1/yagnoloth.py
"""
Yagnoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yagnoloth
"""
from creature_base import GlobalCreatureBaseClass


class Yagnoloth(GlobalCreatureBaseClass):
    """
    Large Fiend (Yugoloth) creature - Yagnoloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 147, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 14, 'CON': 21, 'INT': 16, 'WIS': 15, 'CHAR': 18, 'armor_class': 17, 'alignment': 'typically Neutral Evil Armor Class  17 (natural armor) Hit Points  147 (14d10 + 70) Speed  40 ft. STR 19 (+4) DEX 14 (+2) CON 21 (+5) INT 16 (+3) WIS 15 (+2) CHA 18 (+4) Saving Throws  Dex +6', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'electrified_touch', 'massive_arm', 'battlefield_cunning_(recharge_4–6)', 'life_leech', 'spellcasting', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The yagnoloth has advantage on saving throws against spells and other magical effects."""
        return 'The yagnoloth has advantage on saving throws against spells and other magical effects.'

    def multiattack_attack(self) -> str:
        """The yagnoloth makes one Electrified Touch attack and one Massive Arm attack, or it makes one Massive Arm attack and uses Battlefield Cunning, if available, or Teleport."""
        return 'The yagnoloth makes one Electrified Touch attack and one Massive Arm attack, or it makes one Massive Arm attack and uses Battlefield Cunning, if available, or Teleport.'

    def electrified_touch_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 27 (6d8) lightning damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 27 (6d8) lightning damage.'

    def massive_arm_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 15 ft., one target. Hit: 23 (3d12 + 4) force damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or become stunned until the end of the yagnoloth's next turn."""
        return "Melee Weapon Attack: +8 to hit, reach 15 ft., one target. Hit: 23 (3d12 + 4) force damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or become stunned until the end of the yagnoloth's next turn."

    def battlefield_cunning_(recharge_4–6)_attack(self) -> str:
        """Up to two allied yugoloths within 60 feet of the yagnoloth that can hear it can use their reactions to make one melee attack each."""
        return 'Up to two allied yugoloths within 60 feet of the yagnoloth that can hear it can use their reactions to make one melee attack each.'

    def life_leech_attack(self) -> str:
        """The yagnoloth touches one incapacitated creature within 15 feet of it. The target takes 36 (7d8 + 4) necrotic damage, and the yagnoloth gains temporary hit points equal to half the damage dealt. The target must succeed on a DC 16 Constitution saving throw, or its hit point maximum is reduced by an amount equal to half the necrotic damage taken. This reduction lasts until the target finishes a long rest, and the target dies if its hit point maximum is reduced to 0."""
        return 'The yagnoloth touches one incapacitated creature within 15 feet of it. The target takes 36 (7d8 + 4) necrotic damage, and the yagnoloth gains temporary hit points equal to half the damage dealt. The target must succeed on a DC 16 Constitution saving throw, or its hit point maximum is reduced by an amount equal to half the necrotic damage taken. This reduction lasts until the target finishes a long rest, and the target dies if its hit point maximum is reduced to 0.'

    def spellcasting_attack(self) -> str:
        """The yagnoloth casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 16):"""
        return 'The yagnoloth casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 16):'

    def teleport_attack(self) -> str:
        """The yagnoloth teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."""
        return 'The yagnoloth teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see.'

