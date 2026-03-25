# bases1/crawling-claw.py
"""
CrawlingClaw creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crawling-claw
"""
from creature_base import GlobalCreatureBaseClass


class CrawlingClaw(GlobalCreatureBaseClass):
    """
    Tiny undead creature - CrawlingClaw
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 2, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 14, 'CON': 11, 'INT': 5, 'WIS': 10, 'CHAR': 4, 'armor_class': 12, 'alignment': 'neutral evil Armor Class  12 Hit Points  2 (1d4) Speed  20 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['turn_immunity', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def turn_immunity(self) -> str:
        """The claw is immune to effects that turn undead."""
        return 'The claw is immune to effects that turn undead.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning or slashing damage (claw's choice)."""
        return "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning or slashing damage (claw's choice)."

