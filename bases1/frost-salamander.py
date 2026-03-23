# bases1/frost-salamander.py
"""
FrostSalamander creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frost-salamander
"""
from creature_base import GlobalCreatureBaseClass


class FrostSalamander(GlobalCreatureBaseClass):
    """
    FrostSalamander creature
    Size: Huge, Type: Elemental, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 168,
        "min_level": 10,
        "level": 10,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Elemental, unaligned",
        "hit_points_up": [16, 16, 16],
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
        self.abilities.extend(['burning_fury'])

    def burning_fury(self) -> str:
        """Burning Fury: When the salamander takes fire damage, its Freezing Breath automatically recharges.ActionsMultiattac..."""
        return "When the salamander takes fire damage, its Freezing Breath automatically recharges.ActionsMultiattack. The salamander makes one Bite attack and four Claw attacks.Bite. Melee Weapon Attack: +9 to hit, "

