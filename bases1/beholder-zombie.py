# bases1/beholder-zombie.py
"""
BeholderZombie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=beholder-zombie
"""
from creature_base import GlobalCreatureBaseClass


class BeholderZombie(GlobalCreatureBaseClass):
    """
    Large undead creature - BeholderZombie
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 8, 'CON': 16, 'INT': 3, 'WIS': 8, 'CHAR': 5, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (natural armor) Hit Points  93 (11d10 + 33) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['undead_fortitude', 'bite', 'eye_ray', '&nbsp;_1-_paralyzing_ray', '&nbsp;_2-_fear_ray', '&nbsp;_3-_enervation_ray', '&nbsp;_4-_disintegration_ray']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def undead_fortitude(self) -> str:
        """If damage reduces the zombie to 0 Hit Points, it makes a Constitution saving throw (DC 5 plus the damage taken) unless the damage is Radiant or from a Critical Hit. On a successful save, the zombie dr"""
        return 'If damage reduces the zombie to 0 Hit Points, it makes a Constitution saving throw (DC 5 plus the damage taken) unless the damage is Radiant or from a Critical Hit. On a successful save, the zombie dr'

    def bite_attack(self) -> str:
        """Bite. Melee Attack Roll: +5, reach 5 ft. Hit: 16 (4d6 + 2) Piercing damage."""
        return 'Bite. Melee Attack Roll: +5, reach 5 ft. Hit: 16 (4d6 + 2) Piercing damage.'

    def eye_ray_attack(self) -> str:
        """The zombie randomly shoots one of the following magical rays at a target it can see within 120 feet of itself (roll 1d4; reroll if the zombie has already used that ray during this turn):"""
        return 'The zombie randomly shoots one of the following magical rays at a target it can see within 120 feet of itself (roll 1d4; reroll if the zombie has already used that ray during this turn):'

    def &nbsp;_1-_paralyzing_ray_attack(self) -> str:
        """Constitution Saving Throw: DC 14. Failure: The target has the Paralyzed condition and repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically."""
        return 'Constitution Saving Throw: DC 14. Failure: The target has the Paralyzed condition and repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.'

    def &nbsp;_2-_fear_ray_attack(self) -> str:
        """Wisdom Saving Throw: DC 14. Failure: 13 (3d8) Psychic damage, and the target has the Frightened condition until the end of its next turn."""
        return 'Wisdom Saving Throw: DC 14. Failure: 13 (3d8) Psychic damage, and the target has the Frightened condition until the end of its next turn.'

    def &nbsp;_3-_enervation_ray_attack(self) -> str:
        """Constitution Saving Throw: DC 14. Failure: 10 (3d6) Necrotic damage, and the target has the Poisoned condition until the end of its next turn. While Poisoned, the target can't regain Hit Points. Success: Half damage only."""
        return "Constitution Saving Throw: DC 14. Failure: 10 (3d6) Necrotic damage, and the target has the Poisoned condition until the end of its next turn. While Poisoned, the target can't regain Hit Points. Success: Half damage only."

    def &nbsp;_4-_disintegration_ray_attack(self) -> str:
        """Dexterity Saving Throw: DC 14. Failure: 27 (5d10) Force damage. If the target is a nonmagical object or a creation of magical force, a 10-foot Cube of it disintegrates into dust. Success: Half damage. Failure or Success: If the target is a creature and this damage reduces it to 0 Hit Points, it disintegrates into dust."""
        return 'Dexterity Saving Throw: DC 14. Failure: 27 (5d10) Force damage. If the target is a nonmagical object or a creation of magical force, a 10-foot Cube of it disintegrates into dust. Success: Half damage. Failure or Success: If the target is a creature and this damage reduces it to 0 Hit Points, it disintegrates into dust.'

