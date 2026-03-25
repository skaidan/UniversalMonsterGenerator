# bases1/wight.py
"""
Wight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wight
"""
from creature_base import GlobalCreatureBaseClass


class Wight(GlobalCreatureBaseClass):
    """
    Medium undead creature - Wight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 16, 'INT': 10, 'WIS': 13, 'CHAR': 15, 'armor_class': 14, 'alignment': 'neutral evil Armor Class  14 (studded leather) Hit Points  45 (6d8 + 18) Speed  30 ft. STR 15 (+2) DEX 14 (+2) CON 16 (+3) INT 10 (+0) WIS 13 (+1) CHA 15 (+2) Skills  Perception +3', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['sunlight_sensitivity', 'multiattack', 'life_drain', 'longsword', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sunlight_sensitivity(self) -> str:
        """While in sunlight, the wight has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."""
        return 'While in sunlight, the wight has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.'

    def multiattack_attack(self) -> str:
        """The wight makes two longsword attacks or two longbow attacks. It can use its Life Drain in place of one longsword attack."""
        return 'The wight makes two longsword attacks or two longbow attacks. It can use its Life Drain in place of one longsword attack.'

    def life_drain_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) necrotic damage. The target must succeed on a DC 13 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. A humanoid slain by this attack rises 24 hours later as a zombie under the wight's control, unless the humanoid is restored to life or its body is destroyed. The wight can have no more than twelve zombies under its control at one time."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) necrotic damage. The target must succeed on a DC 13 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. A humanoid slain by this attack rises 24 hours later as a zombie under the wight's control, unless the humanoid is restored to life or its body is destroyed. The wight can have no more than twelve zombies under its control at one time."

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with two hands.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

