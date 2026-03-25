# bases1/neogi.py
"""
Neogi creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=neogi
"""
from creature_base import GlobalCreatureBaseClass


class Neogi(GlobalCreatureBaseClass):
    """
    Small Aberration creature - Neogi
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 16, 'CON': 14, 'INT': 13, 'WIS': 12, 'CHAR': 15, 'armor_class': 15, 'alignment': 'typically Lawful Evil Armor Class  15 (natural armor) Hit Points  33 (6d6 + 12) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['mental_fortitude', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def mental_fortitude(self) -> str:
        """The neogi has advantage on saving throws against being charmed or frightened, and magic can't put the neogi to sleep.Spider Climb. The neogi can climb difficult surfaces, including upside down on ceil"""
        return "The neogi has advantage on saving throws against being charmed or frightened, and magic can't put the neogi to sleep.Spider Climb. The neogi can climb difficult surfaces, including upside down on ceil"

    def multiattack_attack(self) -> str:
        """The neogi makes one Bite attack and two Claw attacks."""
        return 'The neogi makes one Bite attack and two Claw attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 14 (4d6) poison damage, and the target must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 14 (4d6) poison damage, and the target must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) slashing damage.'

