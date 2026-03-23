# bases1/yuan-ti-pit-master.py
"""
YuanTiPitMaster creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-pit-master
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiPitMaster(GlobalCreatureBaseClass):
    """
    YuanTiPitMaster creature
    Size: Medium, Type: snake or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 88,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "snake or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies.",
        "hit_points_up": [8, 8, 8],
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
        # Add creature-specific abilities
        self.abilities.extend(['devils_sight'])

    def devils_sight(self) -> str:
        """Devil's Sight: Magical darkness doesn't impede the yuan-ti's darkvision.Magic Resistance. The yuan-ti has advantage..."""
        return "Magical darkness doesn't impede the yuan-ti's darkvision.Magic Resistance. The yuan-ti has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The yuan-ti makes thr"

