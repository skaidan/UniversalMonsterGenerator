# bases1/gynosphinx.py
"""
Gynosphinx creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gynosphinx
"""
from creature_base import GlobalCreatureBaseClass


class Gynosphinx(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Gynosphinx
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 18, 'WIS': 18, 'CHAR': 18, 'armor_class': 17, 'alignment': 'lawful neutral Armor Class  17 (natural armor) Hit Points  136 (16d10 + 48) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['inscrutable', 'multiattack', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def inscrutable(self) -> str:
        """The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intention"""
        return "The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intention"

    def multiattack_attack(self) -> str:
        """The sphinx makes two claw attacks."""
        return 'The sphinx makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.'

