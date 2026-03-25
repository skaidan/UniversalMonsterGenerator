# bases1/grung.py
"""
Grung creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grung
"""
from creature_base import GlobalCreatureBaseClass


class Grung(GlobalCreatureBaseClass):
    """
    Small Humanoid creature - Grung
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 14, 'CON': 15, 'INT': 10, 'WIS': 11, 'CHAR': 10, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 Hit Points  11 (2d6 + 4) Speed  25 ft.', 'legendary': False, 'size': 'Small', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'dagger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The grung can breathe air and water.Poisonous Skin. Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw """
        return "The grung can breathe air and water.Poisonous Skin. Any creature that grapples the grung or otherwise comes into direct contact with the grung's skin must succeed on a DC 12 Constitution saving throw "

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage plus 5 (2d4) poison damage."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage plus 5 (2d4) poison damage.'

