# bases1/spellcaster-lvl-2.py
"""
SpellcasterLvl2 creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spellcaster-lvl-2
"""
from creature_base import GlobalCreatureBaseClass


class SpellcasterLvl2(GlobalCreatureBaseClass):
    """
    SpellcasterLvl2 creature
    Size: Medium, Type: humanoid (any race), -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 1,
        "level": 1,
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
        "type": "humanoid (any race), -",
        "hit_points_up": [1, 1, 1],
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
        self.abilities.extend(['magical_role'])

    def magical_role(self) -> str:
        """Magical Role: Choose a role for the spellcaster: healer or mage. Your choice determines which Spellcasting trait t..."""
        return "Choose a role for the spellcaster: healer or mage. Your choice determines which Spellcasting trait to use below.Spellcasting (Healer). The spellcaster's spellcasting ability is Wisdom (spell save DC 1"

