# bases1/crocodile.py
"""
Crocodile creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crocodile
"""
from creature_base import GlobalCreatureBaseClass


class Crocodile(GlobalCreatureBaseClass):
    """
    Large beast creature - Crocodile
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 13, 'INT': 2, 'WIS': 10, 'CHAR': 5, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  19 (3d10 + 3) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The crocodile can hold its breath for 15 minutes."""
        return 'The crocodile can hold its breath for 15 minutes.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the crocodile can't bite another target."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the crocodile can't bite another target."

