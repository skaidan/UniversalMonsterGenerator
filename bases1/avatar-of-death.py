# bases1/avatar-of-death.py
"""
AvatarOfDeath creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=avatar-of-death
"""
from creature_base import GlobalCreatureBaseClass


class AvatarOfDeath(GlobalCreatureBaseClass):
    """
    Medium undead creature - AvatarOfDeath
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 16, 'CON': 16, 'INT': 16, 'WIS': 16, 'CHAR': 16, 'armor_class': 20, 'alignment': 'neutral evil Armor Class  20 Hit Points  half the hit point maximum of its summoner Speed  60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['incorporeal_movement', 'reaping_scythe']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def incorporeal_movement(self) -> str:
        """The avatar can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Turning Immunity. The avatar is immune to"""
        return 'The avatar can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Turning Immunity. The avatar is immune to'

    def reaping_scythe_attack(self) -> str:
        """The avatar sweeps its spectral scythe through a creature within 5 feet of it, dealing 7 (1d8 + 3) slashing damage plus 4 (1d8) necrotic damage."""
        return 'The avatar sweeps its spectral scythe through a creature within 5 feet of it, dealing 7 (1d8 + 3) slashing damage plus 4 (1d8) necrotic damage.'

