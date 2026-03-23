# bases1/astral-dreadnought.py
"""
AstralDreadnought creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=astral-dreadnought
"""
from creature_base import GlobalCreatureBaseClass


class AstralDreadnought(GlobalCreatureBaseClass):
    """
    AstralDreadnought creature
    Size: Huge, Type: or smaller creature that the dreadnought can see within 60 feet of it must succeed on a DC 19 Charisma saving throw or be teleported to an unoccupied space on the floor of the Demiplanar Donjon. At the end of the target's next turn, it reappears in the space it left or in the nearest unoccupied space if that space is occupied.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 297,
        "min_level": 22,
        "level": 22,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "or smaller creature that the dreadnought can see within 60 feet of it must succeed on a DC 19 Charisma saving throw or be teleported to an unoccupied space on the floor of the Demiplanar Donjon. At the end of the target's next turn, it reappears in the space it left or in the nearest unoccupied space if that space is occupied.",
        "hit_points_up": [29, 29, 29],
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
        self.abilities.extend(['antimagic_cone'])

    def antimagic_cone(self) -> str:
        """Antimagic Cone: The dreadnought's eye creates an area of antimagic, as in the antimagic field spell, in a 150-foot c..."""
        return "The dreadnought's eye creates an area of antimagic, as in the antimagic field spell, in a 150-foot cone. At the start of each of its turns, it decides which way the cone faces. The cone doesn't functi"

