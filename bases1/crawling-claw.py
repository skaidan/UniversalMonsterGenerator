# bases1/crawling-claw.py
"""
CrawlingClaw creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crawling-claw
"""
from creature_base import GlobalCreatureBaseClass


class CrawlingClaw(GlobalCreatureBaseClass):
    """
    CrawlingClaw creature
    Size: Tiny, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 2,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "undead, neutral evil",
        "hit_points_up": [1, 1, 1],
        "STR_up": [1, 0, 0],
        "DEX_up": [1, 0, 0],
        "CON_up": [0, 1, 0],
        "INT_up": [0, 1, 0],
        "WIS_up": [0, 0, 1],
        "CHAR_up": [0, 0, 1],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.extend(['turn_immunity'])

    def turn_immunity(self) -> str:
        """Turn Immunity: The claw is immune to effects that turn undead.ActionsClaw. Melee Weapon Attack: +3 to hit, reach 5 ..."""
        return "The claw is immune to effects that turn undead.ActionsClaw. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning or slashing damage (claw's choice).Monster Manual (BR+"
    def turn_immunity(self) -> str:
        """Turn Immunity: The claw is immune to effects that turn undead.ActionsClaw. Melee Weapon Attack: +3 to hit, reach 5 ..."""
        return "The claw is immune to effects that turn undead.ActionsClaw. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning or slashing damage (claw's choice).Monster Manual (BR+"

