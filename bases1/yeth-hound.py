# bases1/yeth-hound.py
"""
YethHound creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yeth-hound
"""
from creature_base import GlobalCreatureBaseClass


class YethHound(GlobalCreatureBaseClass):
    """
    Large Fey creature - YethHound
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 51, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 17, 'CON': 16, 'INT': 5, 'WIS': 12, 'CHAR': 7, 'armor_class': 14, 'alignment': 'typically Neutral Evil Armor Class  14 (natural armor) Hit Points  51 (6d10 + 18) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['sunlight_banishment', 'bite', 'baleful_baying']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sunlight_banishment(self) -> str:
        """If the yeth hound starts its turn in sunlight, it is transported to the Ethereal Plane. While sunlight shines on the spot from which it vanished, the hound must remain in the Deep Ethereal. After suns"""
        return 'If the yeth hound starts its turn in sunlight, it is transported to the Ethereal Plane. While sunlight shines on the spot from which it vanished, the hound must remain in the Deep Ethereal. After suns'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage, plus 14 (4d6) psychic damage if the target is frightened."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage, plus 14 (4d6) psychic damage if the target is frightened.'

    def baleful_baying_attack(self) -> str:
        """The yeth hound bays magically. Every enemy within 300 feet of the hound that can hear it must succeed on a DC 13 Wisdom saving throw or be frightened of the hound until the end of the hound's next turn or until the hound is incapacitated. A frightened target that starts its turn within 30 feet of the hound must use all its movement on that turn to get as far from the hound as possible, must finish the move before taking an action, and must take the most direct route, even if hazards lie that way. A target that successfully saves is immune to the baying of all yeth hounds for the next 24 hours."""
        return "The yeth hound bays magically. Every enemy within 300 feet of the hound that can hear it must succeed on a DC 13 Wisdom saving throw or be frightened of the hound until the end of the hound's next turn or until the hound is incapacitated. A frightened target that starts its turn within 30 feet of the hound must use all its movement on that turn to get as far from the hound as possible, must finish the move before taking an action, and must take the most direct route, even if hazards lie that way. A target that successfully saves is immune to the baying of all yeth hounds for the next 24 hours."

