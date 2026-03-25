# bases1/balor.py
"""
Balor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=balor
"""
from creature_base import GlobalCreatureBaseClass


class Balor(GlobalCreatureBaseClass):
    """
    Huge fiend (Demon) creature - Balor
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 262, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 15, 'CON': 22, 'INT': 20, 'WIS': 16, 'CHAR': 22, 'armor_class': 19, 'alignment': 'chaotic evil Armor Class  19 (natural armor) Hit Points  262 (21d12 + 126) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_throes', 'multiattack', 'longsword', 'whip', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_throes(self) -> str:
        """When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successful"""
        return 'When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successful'

    def multiattack_attack(self) -> str:
        """The balor makes two attacks: one with its longsword and one with its whip."""
        return 'The balor makes two attacks: one with its longsword and one with its whip.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) slashing damage plus 13 (3d8) lightning damage. If the balor scores a critical hit, it rolls damage dice three times, instead of twice."""
        return 'Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 21 (3d8 + 8) slashing damage plus 13 (3d8) lightning damage. If the balor scores a critical hit, it rolls damage dice three times, instead of twice.'

    def whip_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 30 ft., one target. Hit: 15 (2d6 + 8) slashing damage plus 10 (3d6) fire damage, and the target must succeed on a DC 20 Strength saving throw or be pulled up to 25 feet toward the balor."""
        return 'Melee Weapon Attack: +14 to hit, reach 30 ft., one target. Hit: 15 (2d6 + 8) slashing damage plus 10 (3d6) fire damage, and the target must succeed on a DC 20 Strength saving throw or be pulled up to 25 feet toward the balor.'

    def teleport_attack(self) -> str:
        """The balor magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see."""
        return 'The balor magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.'

