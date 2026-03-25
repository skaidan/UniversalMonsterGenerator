# bases1/neogi-hatchling.py
"""
NeogiHatchling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=neogi-hatchling
"""
from creature_base import GlobalCreatureBaseClass


class NeogiHatchling(GlobalCreatureBaseClass):
    """
    Tiny Aberration creature - NeogiHatchling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 13, 'CON': 10, 'INT': 6, 'WIS': 10, 'CHAR': 9, 'armor_class': 11, 'alignment': 'typically Lawful Evil Armor Class  11 Hit Points  7 (3d4) Speed  20 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['mental_fortitude', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def mental_fortitude(self) -> str:
        """The neogi has advantage on saving throws against being charmed or frightened, and magic can't put the neogi to sleep.Spider Climb. The neogi can climb difficult surfaces, including upside down on ceil"""
        return "The neogi has advantage on saving throws against being charmed or frightened, and magic can't put the neogi to sleep.Spider Climb. The neogi can climb difficult surfaces, including upside down on ceil"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage plus 3 (1d6) poison damage, and the target must succeed on a DC 10 Constitution saving throw or become poisoned for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage plus 3 (1d6) poison damage, and the target must succeed on a DC 10 Constitution saving throw or become poisoned for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

