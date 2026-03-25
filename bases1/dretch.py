# bases1/dretch.py
"""
Dretch creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dretch
"""
from creature_base import GlobalCreatureBaseClass


class Dretch(GlobalCreatureBaseClass):
    """
    Small fiend (Demon) creature - Dretch
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 11, 'CON': 12, 'INT': 5, 'WIS': 8, 'CHAR': 3, 'armor_class': 11, 'alignment': 'chaotic evil Armor Class  11 (natural armor) Hit Points  18 (4d6 + 4) Speed  20 ft. STR 11 (+0) DEX 11 (+0) CON 12 (+1) INT 5 (-3) WIS 8 (-1) CHA 3 (-4) Damage Resistances  cold', 'legendary': False, 'size': 'Small', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'claws', 'fetid_cloud_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The dretch makes two attacks: one with its bite and one with its claws."""
        return 'The dretch makes two attacks: one with its bite and one with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.'

    def fetid_cloud_(1/day)_attack(self) -> str:
        """A 10-foot radius of disgusting green gas extends out from the dretch. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."""
        return "A 10-foot radius of disgusting green gas extends out from the dretch. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."

