# bases1/chitine.py
"""
Chitine creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=chitine
"""
from creature_base import GlobalCreatureBaseClass


class Chitine(GlobalCreatureBaseClass):
    """
    Small Monstrosity creature - Chitine
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 12, 'INT': 10, 'WIS': 10, 'CHAR': 7, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (hide armor) Hit Points  18 (4d6 + 4) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'multiattack', 'dagger']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The chitine has advantage on saving throws against being charmed, and magic can't put the chitine to sleep.Sunlight Sensitivity. While in sunlight, the chitine has disadvantage on attack rolls, as wel"""
        return "The chitine has advantage on saving throws against being charmed, and magic can't put the chitine to sleep.Sunlight Sensitivity. While in sunlight, the chitine has disadvantage on attack rolls, as wel"

    def multiattack_attack(self) -> str:
        """The chitine makes three Dagger attacks."""
        return 'The chitine makes three Dagger attacks.'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

