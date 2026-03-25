# bases1/nycaloth.py
"""
Nycaloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nycaloth
"""
from creature_base import GlobalCreatureBaseClass


class Nycaloth(GlobalCreatureBaseClass):
    """
    Large fiend (Yugoloth) creature - Nycaloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 123, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 11, 'CON': 19, 'INT': 12, 'WIS': 10, 'CHAR': 15, 'armor_class': 18, 'alignment': 'neutral evil Armor Class  18 (natural armor) Hit Points  123 (13d10 + 52) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'multiattack', 'claw', 'greataxe', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The nycaloth's innate spellcasting ability is Charisma. The nycaloth can innately cast the following spells, requiring no material components:At will: darkness, detect magic, dispel magic, invisibilit"""
        return "The nycaloth's innate spellcasting ability is Charisma. The nycaloth can innately cast the following spells, requiring no material components:At will: darkness, detect magic, dispel magic, invisibilit"

    def multiattack_attack(self) -> str:
        """The nycaloth makes two melee attacks, or it makes one melee attack and teleports before or after the attack."""
        return 'The nycaloth makes two melee attacks, or it makes one melee attack and teleports before or after the attack.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or take 5 (2d4) slashing damage at the start of each of its turns due to a fiendish wound. Each time the nycaloth hits the wounded target with this attack, the damage dealt by the wound increases by 5 (2d4). Any creature can take an action to stanch the wound with a successful DC 13 Wisdom (Medicine) check. The wound also closes if the target receives magical healing."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or take 5 (2d4) slashing damage at the start of each of its turns due to a fiendish wound. Each time the nycaloth hits the wounded target with this attack, the damage dealt by the wound increases by 5 (2d4). Any creature can take an action to stanch the wound with a successful DC 13 Wisdom (Medicine) check. The wound also closes if the target receives magical healing.'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 18 (2d12 + 5) slashing damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 18 (2d12 + 5) slashing damage.'

    def teleport_attack(self) -> str:
        """The nycaloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."""
        return 'The nycaloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see.'

