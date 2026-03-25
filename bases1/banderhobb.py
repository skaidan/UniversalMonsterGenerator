# bases1/banderhobb.py
"""
Banderhobb creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=banderhobb
"""
from creature_base import GlobalCreatureBaseClass


class Banderhobb(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - Banderhobb
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 84, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 12, 'CON': 20, 'INT': 11, 'WIS': 14, 'CHAR': 8, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  84 (8d10 + 40) Speed  30 ft. STR 20 (+5) DEX 12 (+1) CON 20 (+5) INT 11 (+0) WIS 14 (+2) CHA 8 (-1) Skills  Athletics +8', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['resonant_connection', 'multiattack', 'bite', 'tongue', 'shadow_step', 'swallow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def resonant_connection(self) -> str:
        """If the banderhobb has even a tiny piece of a creature or an object in its possession, such as a lock of hair or a splinter of wood, it knows the most direct route to that creature or object if it is w"""
        return 'If the banderhobb has even a tiny piece of a creature or an object in its possession, such as a lock of hair or a splinter of wood, it knows the most direct route to that creature or object if it is w'

    def multiattack_attack(self) -> str:
        """The banderhobb makes one Bite attack and one Tongue attack. It can replace one attack with a use of Shadow Step."""
        return 'The banderhobb makes one Bite attack and one Tongue attack. It can replace one attack with a use of Shadow Step.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (3d6 + 5) piercing damage, and the target is grappled (escape DC 16) if it is a Large or smaller creature. Until this grapple ends, the target is restrained, and the banderhobb can't use its Bite attack or Tongue attack on another target."""
        return "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (3d6 + 5) piercing damage, and the target is grappled (escape DC 16) if it is a Large or smaller creature. Until this grapple ends, the target is restrained, and the banderhobb can't use its Bite attack or Tongue attack on another target."

    def tongue_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 15 ft., one creature. Hit: 10 (3d6) necrotic damage, and the target must make a DC 16 Strength saving throw. On a failed save, the target is pulled to a space within 5 feet of the banderhobb."""
        return 'Melee Weapon Attack: +8 to hit, reach 15 ft., one creature. Hit: 10 (3d6) necrotic damage, and the target must make a DC 16 Strength saving throw. On a failed save, the target is pulled to a space within 5 feet of the banderhobb.'

    def shadow_step_attack(self) -> str:
        """The banderhobb teleports up to 30 feet to an unoccupied space of dim light or darkness that it can see."""
        return 'The banderhobb teleports up to 30 feet to an unoccupied space of dim light or darkness that it can see.'

    def swallow_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one Medium or smaller creature grappled by the banderhobb. Hit: 15 (3d6 + 5) piercing damage. The creature is also swallowed, and the grapple ends. The swallowed creature is blinded and restrained, it has total cover against attacks and other effects outside the banderhobb, and it takes 10 (3d6) necrotic damage at the start of each of the banderhobb's turns. A creature reduced to 0 hit points in this way stops taking the necrotic damage and becomes stable. The banderhobb can have only one creature swallowed at a time. While the banderhobb isn't incapacitated, it can regurgitate the creature at any time (no action required) in a space within 5 feet of it. The creature exits prone. If the banderhobb dies, it likewise regurgitates a swallowed creature."""
        return "Melee Weapon Attack: +8 to hit, reach 5 ft., one Medium or smaller creature grappled by the banderhobb. Hit: 15 (3d6 + 5) piercing damage. The creature is also swallowed, and the grapple ends. The swallowed creature is blinded and restrained, it has total cover against attacks and other effects outside the banderhobb, and it takes 10 (3d6) necrotic damage at the start of each of the banderhobb's turns. A creature reduced to 0 hit points in this way stops taking the necrotic damage and becomes stable. The banderhobb can have only one creature swallowed at a time. While the banderhobb isn't incapacitated, it can regurgitate the creature at any time (no action required) in a space within 5 feet of it. The creature exits prone. If the banderhobb dies, it likewise regurgitates a swallowed creature."

