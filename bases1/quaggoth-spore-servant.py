# bases1/quaggoth-spore-servant.py
"""
QuaggothSporeServant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quaggoth-spore-servant
"""
from creature_base import GlobalCreatureBaseClass


class QuaggothSporeServant(GlobalCreatureBaseClass):
    """
    Medium plant creature - QuaggothSporeServant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 16, 'INT': 2, 'WIS': 6, 'CHAR': 1, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  45 (6d8 + 18) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The spore servant makes two claw attacks."""
        return 'The spore servant makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

