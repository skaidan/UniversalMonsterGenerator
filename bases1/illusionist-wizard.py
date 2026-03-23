# bases1/illusionist-wizard.py
"""
IllusionistWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=illusionist-wizard
"""
from creature_base import GlobalCreatureBaseClass


class IllusionistWizard(GlobalCreatureBaseClass):
    """
    IllusionistWizard creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 44,
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
        "type": "Humanoid, any alignment",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The illusionist makes two Arcane Burst attacks.Arcane Burst. Melee or Ranged Spell Attack: +5 to hit..."""
        return "The illusionist makes two Arcane Burst attacks.Arcane Burst. Melee or Ranged Spell Attack: +5 to hit, reach 5 ft. or range 120 ft., one target. Hit: 14 (2d10 + 3) psychic damage.Spellcasting. The illu"

