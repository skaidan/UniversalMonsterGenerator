# bases1/quetzalcoatlus.py
"""
Quetzalcoatlus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quetzalcoatlus
"""
from creature_base import GlobalCreatureBaseClass


class Quetzalcoatlus(GlobalCreatureBaseClass):
    """
    Huge Beast (Dinosaur) creature - Quetzalcoatlus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 30, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 13, 'CON': 13, 'INT': 2, 'WIS': 10, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  30 (4d12 + 4) Speed  10 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Beast (Dinosaur)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['flyby', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def flyby(self) -> str:
        """The quetzalcoatlus doesn't provoke an opportunity attack when it flies out of an enemy's reach."""
        return "The quetzalcoatlus doesn't provoke an opportunity attack when it flies out of an enemy's reach."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 10 ft., one creature. Hit: 12 (3d6 + 2) piercing damage. If the quetzalcoatlus flew least 30 feet toward the target immediately before the hit, the target takes an extra 10 (3d6) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 10 ft., one creature. Hit: 12 (3d6 + 2) piercing damage. If the quetzalcoatlus flew least 30 feet toward the target immediately before the hit, the target takes an extra 10 (3d6) piercing damage.'

