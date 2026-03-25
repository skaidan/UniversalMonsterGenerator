# bases1/spined-devil.py
"""
SpinedDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spined-devil
"""
from creature_base import GlobalCreatureBaseClass


class SpinedDevil(GlobalCreatureBaseClass):
    """
    Small fiend (Devil) creature - SpinedDevil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 15, 'CON': 12, 'INT': 11, 'WIS': 14, 'CHAR': 8, 'armor_class': 13, 'alignment': 'lawful evil Armor Class  13 (natural armor) Hit Points  22 (5d6 + 5) Speed  20 ft.', 'legendary': False, 'size': 'Small', 'type': 'fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'bite', 'fork', 'tail_spine']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the devil's darkvision.Flyby. The devil doesn't provoke an opportunity attack when it flies out of an enemy's reach.Limited Spines. The devil has twelve tail spines. Us"""
        return "Magical darkness doesn't impede the devil's darkvision.Flyby. The devil doesn't provoke an opportunity attack when it flies out of an enemy's reach.Limited Spines. The devil has twelve tail spines. Us"

    def multiattack_attack(self) -> str:
        """The devil makes two attacks: one with its bite and one with its fork or two with its tail spines."""
        return 'The devil makes two attacks: one with its bite and one with its fork or two with its tail spines.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.'

    def fork_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage.'

    def tail_spine_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 20/80 ft., one target. Hit: 4 (1d4 + 2) piercing damage plus 3 (1d6) fire damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 20/80 ft., one target. Hit: 4 (1d4 + 2) piercing damage plus 3 (1d6) fire damage.'

