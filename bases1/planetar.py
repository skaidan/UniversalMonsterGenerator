# bases1/planetar.py
"""
Planetar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=planetar
"""
from creature_base import GlobalCreatureBaseClass


class Planetar(GlobalCreatureBaseClass):
    """
    Large celestial creature - Planetar
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 200, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 20, 'CON': 24, 'INT': 19, 'WIS': 22, 'CHAR': 25, 'armor_class': 19, 'alignment': 'lawful good Armor Class  19 (natural armor) Hit Points  200 (16d10 + 112) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'celestial', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['angelic_weapons', 'multiattack', 'greatsword', 'healing_touch_(4/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def angelic_weapons(self) -> str:
        """The planetar's weapon attacks are magical. When the planetar hits with any weapon, the weapon deals an extra 5d8 radiant damage (included in the attack).Divine Awareness. The planetar knows if it hear"""
        return "The planetar's weapon attacks are magical. When the planetar hits with any weapon, the weapon deals an extra 5d8 radiant damage (included in the attack).Divine Awareness. The planetar knows if it hear"

    def multiattack_attack(self) -> str:
        """The planetar makes two melee attacks."""
        return 'The planetar makes two melee attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 21 (4d6 + 7) slashing damage plus 22 (5d8) radiant damage."""
        return 'Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 21 (4d6 + 7) slashing damage plus 22 (5d8) radiant damage.'

    def healing_touch_(4/day)_attack(self) -> str:
        """The planetar touches another creature. The target magically regains 30 (6d8 + 3) hit points and is freed from any curse, disease, poison, blindness, or deafness."""
        return 'The planetar touches another creature. The target magically regains 30 (6d8 + 3) hit points and is freed from any curse, disease, poison, blindness, or deafness.'

