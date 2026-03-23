# bases1/grell.py
"""
Grell creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grell
"""
from creature_base import GlobalCreatureBaseClass


class Grell(GlobalCreatureBaseClass):
    """
    Grell creature
    Size: Medium, Type: or smaller, it is also restrained until this grapple ends. While grappling the target, the grell has advantage on attack rolls against it and can't use this attack against other targets. When the grell moves, any Medium or smaller target it is grappling moves with it.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 55,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, it is also restrained until this grapple ends. While grappling the target, the grell has advantage on attack rolls against it and can't use this attack against other targets. When the grell moves, any Medium or smaller target it is grappling moves with it.",
        "hit_points_up": [5, 5, 5],
        "STR_up": [1, 0, 0],
        "DEX_up": [1, 0, 0],
        "CON_up": [0, 1, 0],
        "INT_up": [0, 1, 0],
        "WIS_up": [0, 0, 1],
        "CHAR_up": [0, 0, 1],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The grell makes two attacks: one with its tentacles and one with its beak.Tentacles. Melee Weapon At..."""
        return "The grell makes two attacks: one with its tentacles and one with its beak.Tentacles. Melee Weapon Attack: +4 to hit, reach 10 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must "
    def multiattack(self) -> str:
        """Multiattack: The grell makes two attacks: one with its tentacles and one with its beak.Tentacles. Melee Weapon At..."""
        return "The grell makes two attacks: one with its tentacles and one with its beak.Tentacles. Melee Weapon Attack: +4 to hit, reach 10 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must "

