# bases1/conjurer-wizard.py
"""
ConjurerWizard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=conjurer-wizard
"""
from creature_base import GlobalCreatureBaseClass


class ConjurerWizard(GlobalCreatureBaseClass):
    """
    ConjurerWizard creature
    Size: Small, Type: or Medium creature, they both teleport, swapping places.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 58,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "or Medium creature, they both teleport, swapping places.",
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
        # Add creature-specific abilities
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The conjurer makes three Arcane Burst attacks.Arcane Burst. Melee or Ranged Spell Attack: +8 to hit,..."""
        return "The conjurer makes three Arcane Burst attacks.Arcane Burst. Melee or Ranged Spell Attack: +8 to hit, reach 5 ft. or range 120 ft., one target. Hit: 19 (3d10 + 3) force damage.Spellcasting. The conjure"

