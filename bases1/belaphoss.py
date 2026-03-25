# bases1/belaphoss.py
"""
Belaphoss creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=belaphoss
"""
from creature_base import GlobalCreatureBaseClass


class Belaphoss(GlobalCreatureBaseClass):
    """
    Huge fiend (Demon) creature - Belaphoss
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 262, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 15, 'CON': 22, 'INT': 20, 'WIS': 16, 'CHAR': 22, 'armor_class': 19, 'alignment': 'chaotic evil Armor Class  19 (natural armor) Hit Points  262 (21d12 + 126) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_throes', 'multiattack', 'greataxe', 'whip', 'abyssal_storm_(recharge_5–6)', 'teleport', 'winged_barrage']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_throes(self) -> str:
        """When Belaphoss dies, he explodes, and each creature within 30 feet of him must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successfu"""
        return 'When Belaphoss dies, he explodes, and each creature within 30 feet of him must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successfu'

    def multiattack_attack(self) -> str:
        """Belaphoss makes two attacks: one with his greataxe and one with his whip."""
        return 'Belaphoss makes two attacks: one with his greataxe and one with his whip.'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 24 (3d10 + 8) slashing damage plus 13 (3d8) fire damage. If Belaphoss scores a critical hit, he rolls damage dice three times, instead of twice."""
        return 'Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 24 (3d10 + 8) slashing damage plus 13 (3d8) fire damage. If Belaphoss scores a critical hit, he rolls damage dice three times, instead of twice.'

    def whip_attack(self) -> str:
        """Melee Weapon Attack: +14 to hit, reach 30 ft., one target. Hit: 15 (2d6 + 8) slashing damage plus 10 (3d6) fire damage, and the target must succeed on a DC 20 Strength saving throw or be pulled up to 25 feet toward Belaphoss."""
        return 'Melee Weapon Attack: +14 to hit, reach 30 ft., one target. Hit: 15 (2d6 + 8) slashing damage plus 10 (3d6) fire damage, and the target must succeed on a DC 20 Strength saving throw or be pulled up to 25 feet toward Belaphoss.'

    def abyssal_storm_(recharge_5–6)_attack(self) -> str:
        """Belaphoss surrounds himself with explosive fire that fills a 30-foot sphere centered on him and spreads around corners. Each creature in the fire must make a Dexterity saving throw, taking 28 (8d6) fire damage and 28 (8d6) bludgeoning damage on a failed save, or half as much damage on a successful one. Belaphoss is immune to this damage. Objects in the area are subject to it, and the fire ignites flammable objects in the area that aren't being worn or carried."""
        return "Belaphoss surrounds himself with explosive fire that fills a 30-foot sphere centered on him and spreads around corners. Each creature in the fire must make a Dexterity saving throw, taking 28 (8d6) fire damage and 28 (8d6) bludgeoning damage on a failed save, or half as much damage on a successful one. Belaphoss is immune to this damage. Objects in the area are subject to it, and the fire ignites flammable objects in the area that aren't being worn or carried."

    def teleport_attack(self) -> str:
        """Belaphoss magically teleports, along with any equipment he is wearing or carrying, up to 120 feet to an unoccupied space he can see."""
        return 'Belaphoss magically teleports, along with any equipment he is wearing or carrying, up to 120 feet to an unoccupied space he can see.'

    def winged_barrage_attack(self) -> str:
        """Belaphoss beats his wings. Each creature in a 20-foot cube originating from him must make a DC 20 Dexterity saving throw. On a failure, a target takes 29 (6d6 + 8) bludgeoning damage and is pushed 20 feet away from Belaphoss. On a success, the target takes half the bludgeoning damage and isn't pushed. Belaphoss can then fly up to half his flying speed."""
        return "Belaphoss beats his wings. Each creature in a 20-foot cube originating from him must make a DC 20 Dexterity saving throw. On a failure, a target takes 29 (6d6 + 8) bludgeoning damage and is pushed 20 feet away from Belaphoss. On a success, the target takes half the bludgeoning damage and isn't pushed. Belaphoss can then fly up to half his flying speed."

