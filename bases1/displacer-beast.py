# bases1/displacer-beast.py
"""
DisplacerBeast creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=displacer-beast
"""
from creature_base import GlobalCreatureBaseClass


class DisplacerBeast(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - DisplacerBeast
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 6, 'WIS': 12, 'CHAR': 8, 'armor_class': 13, 'alignment': 'lawful evil Armor Class  13 (natural armor) Hit Points  85 (10d10 + 30) Speed  40 ft. STR 18 (+4) DEX 15 (+2) CON 16 (+3) INT 6 (-2) WIS 12 (+1) CHA 8 (-1) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['avoidance', 'multiattack', 'tentacle']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def avoidance(self) -> str:
        """If the displacer beast is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if """
        return 'If the displacer beast is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if '

    def multiattack_attack(self) -> str:
        """The displacer beast makes two attacks with its tentacles."""
        return 'The displacer beast makes two attacks with its tentacles.'

    def tentacle_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage plus 3 (1d6) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage plus 3 (1d6) piercing damage.'

