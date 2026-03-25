# bases1/wraith.py
"""
Wraith creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wraith
"""
from creature_base import GlobalCreatureBaseClass


class Wraith(GlobalCreatureBaseClass):
    """
    Medium undead creature - Wraith
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 16, 'CON': 16, 'INT': 12, 'WIS': 14, 'CHAR': 15, 'armor_class': 13, 'alignment': 'neutral evil Armor Class  13 Hit Points  67 (9d8 + 27) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['incorporeal_movement', 'life_drain', 'create_specter']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def incorporeal_movement(self) -> str:
        """The wraith can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Sunlight Sensitivity. While in sunlight, """
        return 'The wraith can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Sunlight Sensitivity. While in sunlight, '

    def life_drain_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 21 (4d8 + 3) necrotic damage. The target must succeed on a DC 14 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 21 (4d8 + 3) necrotic damage. The target must succeed on a DC 14 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0.'

    def create_specter_attack(self) -> str:
        """The wraith targets a humanoid within 10 feet of it that has been dead for no longer than 1 minute and died violently. The target's spirit rises as a specter in the space of its corpse or in the nearest unoccupied space. The specter is under the wraith's control. The wraith can have no more than seven specters under its control at one time."""
        return "The wraith targets a humanoid within 10 feet of it that has been dead for no longer than 1 minute and died violently. The target's spirit rises as a specter in the space of its corpse or in the nearest unoccupied space. The specter is under the wraith's control. The wraith can have no more than seven specters under its control at one time."

