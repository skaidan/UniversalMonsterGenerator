# bases1/shield-guardian.py
"""
ShieldGuardian creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shield-guardian
"""
from creature_base import GlobalCreatureBaseClass


class ShieldGuardian(GlobalCreatureBaseClass):
    """
    Large construct creature - ShieldGuardian
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 142, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 8, 'CON': 18, 'INT': 7, 'WIS': 10, 'CHAR': 3, 'armor_class': 17, 'alignment': 'unaligned Armor Class  17 (natural armor) Hit Points  142 (15d10 + 60) Speed  30 ft. STR 18 (+4) DEX 8 (-1) CON 18 (+4) INT 7 (-2) WIS 10 (+0) CHA 3 (-4) Senses  blindsight 10 ft.', 'legendary': False, 'size': 'Large', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bound', 'multiattack', 'fist']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bound(self) -> str:
        """The shield guardian is magically bound to an amulet. As long as the guardian and its amulet are on the same plane of existence, the amulet's wearer can telepathically call the guardian to travel to it"""
        return "The shield guardian is magically bound to an amulet. As long as the guardian and its amulet are on the same plane of existence, the amulet's wearer can telepathically call the guardian to travel to it"

    def multiattack_attack(self) -> str:
        """The guardian makes two fist attacks."""
        return 'The guardian makes two fist attacks.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

