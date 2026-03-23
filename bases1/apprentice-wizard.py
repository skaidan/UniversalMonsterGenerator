# bases1/apprentice-wizard.py
"""
ApprenticeWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=apprentice-wizard
"""
from creature_base import GlobalCreatureBaseClass


class ApprenticeWizard(GlobalCreatureBaseClass):
    """
    ApprenticeWizard creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid, any alignment",
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
        self.abilities.extend(['arcane_burst'])

    def arcane_burst(self) -> str:
        """Arcane Burst: Melee or Ranged Spell Attack: +4 to hit, reach 5 ft. or range 120 ft., one target. Hit: 7 (1d10 + 2)..."""
        return "Melee or Ranged Spell Attack: +4 to hit, reach 5 ft. or range 120 ft., one target. Hit: 7 (1d10 + 2) force damage.Spellcasting. The apprentice casts one of the following spells, using Intelligence as "

