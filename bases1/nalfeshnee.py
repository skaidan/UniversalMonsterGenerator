# bases1/nalfeshnee.py
"""
Nalfeshnee creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nalfeshnee
"""
from creature_base import GlobalCreatureBaseClass


class Nalfeshnee(GlobalCreatureBaseClass):
    """
    Large fiend (Demon) creature - Nalfeshnee
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 184, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 10, 'CON': 22, 'INT': 19, 'WIS': 12, 'CHAR': 15, 'armor_class': 18, 'alignment': 'chaotic evil Armor Class  18 (natural armor) Hit Points  184 (16d10 + 96) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'bite', 'claw', 'horror_nimbus_(recharge_5-6)', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The nalfeshnee has advantage on saving throws against spells and other magical effects."""
        return 'The nalfeshnee has advantage on saving throws against spells and other magical effects.'

    def multiattack_attack(self) -> str:
        """The nalfeshnee uses Horror Nimbus if it can. It then makes three attacks: one with its bite and two with its claws."""
        return 'The nalfeshnee uses Horror Nimbus if it can. It then makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 32 (5d10 + 5) piercing damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 32 (5d10 + 5) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 15 (3d6 + 5) slashing damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 15 (3d6 + 5) slashing damage.'

    def horror_nimbus_(recharge_5-6)_attack(self) -> str:
        """The nalfeshnee magically emits scintillating, multicolored light. Each creature within 15 feet of the nalfeshnee that can see the light must succeed on a DC 15 Wisdom saving throw or be frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the nalfeshnee's Horror Nimbus for the next 24 hours."""
        return "The nalfeshnee magically emits scintillating, multicolored light. Each creature within 15 feet of the nalfeshnee that can see the light must succeed on a DC 15 Wisdom saving throw or be frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the nalfeshnee's Horror Nimbus for the next 24 hours."

    def teleport_attack(self) -> str:
        """The nalfeshnee magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see."""
        return 'The nalfeshnee magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.'

