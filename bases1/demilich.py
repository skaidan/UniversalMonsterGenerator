# bases1/demilich.py
"""
Demilich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=demilich
"""
from creature_base import GlobalCreatureBaseClass


class Demilich(GlobalCreatureBaseClass):
    """
    Tiny undead creature - Demilich
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 80, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 20, 'CON': 10, 'INT': 20, 'WIS': 17, 'CHAR': 20, 'armor_class': 20, 'alignment': 'neutral evil Armor Class  20 (natural armor) Hit Points  80 (32d4) Speed  0 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['avoidance', 'howl_(recharge_5-6)', 'life_drain']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def avoidance(self) -> str:
        """If the demilich is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fail"""
        return 'If the demilich is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fail'

    def howl_(recharge_5-6)_attack(self) -> str:
        """The demilich emits a bloodcurdling howl. Each creature within 30 feet of the demilich that can hear the howl must succeed on a DC 15 Constitution saving throw or drop to 0 hit points. On a successful save, the creature is frightened until the end of its next turn."""
        return 'The demilich emits a bloodcurdling howl. Each creature within 30 feet of the demilich that can hear the howl must succeed on a DC 15 Constitution saving throw or drop to 0 hit points. On a successful save, the creature is frightened until the end of its next turn.'

    def life_drain_attack(self) -> str:
        """The demilich targets up to three creatures that it can see within 10 feet of it. Each target must succeed on a DC 19 Constitution saving throw or take 21 (6d6) necrotic damage, and the demilich regains hit points equal to the total damage dealt to all targets."""
        return 'The demilich targets up to three creatures that it can see within 10 feet of it. Each target must succeed on a DC 19 Constitution saving throw or take 21 (6d6) necrotic damage, and the demilich regains hit points equal to the total damage dealt to all targets.'

