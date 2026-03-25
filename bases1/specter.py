# bases1/specter.py
"""
Specter creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=specter
"""
from creature_base import GlobalCreatureBaseClass


class Specter(GlobalCreatureBaseClass):
    """
    Medium undead creature - Specter
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 14, 'CON': 11, 'INT': 10, 'WIS': 10, 'CHAR': 11, 'armor_class': 12, 'alignment': 'chaotic evil Armor Class  12 Hit Points  22 (5d8) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['incorporeal_movement', 'life_drain']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def incorporeal_movement(self) -> str:
        """The specter can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Sunlight Sensitivity. While in sunlight,"""
        return 'The specter can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Sunlight Sensitivity. While in sunlight,'

    def life_drain_attack(self) -> str:
        """Melee Spell Attack: +4 to hit, reach 5 ft., one creature. Hit: 10 (3d6) necrotic damage. The target must succeed on a DC 10 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the creature finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."""
        return 'Melee Spell Attack: +4 to hit, reach 5 ft., one creature. Hit: 10 (3d6) necrotic damage. The target must succeed on a DC 10 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the creature finishes a long rest. The target dies if this effect reduces its hit point maximum to 0.'

