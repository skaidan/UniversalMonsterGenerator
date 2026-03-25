# bases1/grung-wildling.py
"""
GrungWildling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grung-wildling
"""
from creature_base import GlobalCreatureBaseClass


class GrungWildling(GlobalCreatureBaseClass):
    """
    Small Humanoid creature - GrungWildling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 16, 'CON': 15, 'INT': 10, 'WIS': 15, 'CHAR': 11, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (natural armor) Hit Points  27 (5d6 + 10) Speed  25 ft.', 'legendary': False, 'size': 'Small', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'dagger', 'shortbow', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The grung can breathe air and water.Poisonous Skin. Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw """
        return "The grung can breathe air and water.Poisonous Skin. Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw "

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 5 (2d4) poison damage."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 5 (2d4) poison damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 5 (2d4) poison damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 5 (2d4) poison damage.'

    def spellcasting_attack(self) -> str:
        """The grung casts one of the following spells, using Wisdom as the spellcasting ability (spell save DC 12):"""
        return 'The grung casts one of the following spells, using Wisdom as the spellcasting ability (spell save DC 12):'

