# bases1/diviner-wizard.py
"""
DivinerWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=diviner-wizard
"""
from creature_base import GlobalCreatureBaseClass


class DivinerWizard(GlobalCreatureBaseClass):
    """
    DivinerWizard creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 90,
        "min_level": 9,
        "level": 9,
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
        "hit_points_up": [9, 9, 9],
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
        """Multiattack: The diviner makes three Arcane Burst attacks.Arcane Burst. Melee or Ranged Spell Attack: +7 to hit, ..."""
        return "The diviner makes three Arcane Burst attacks.Arcane Burst. Melee or Ranged Spell Attack: +7 to hit, reach 5 ft. or range 120 ft., one target. Hit: 20 (3d10 + 4) radiant damage.Overwhelming Revelation "

