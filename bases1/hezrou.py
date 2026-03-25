# bases1/hezrou.py
"""
Hezrou creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hezrou
"""
from creature_base import GlobalCreatureBaseClass


class Hezrou(GlobalCreatureBaseClass):
    """
    Large fiend (Demon) creature - Hezrou
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 17, 'CON': 20, 'INT': 5, 'WIS': 12, 'CHAR': 13, 'armor_class': 16, 'alignment': 'chaotic evil Armor Class  16 (natural armor) Hit Points  136 (13d10 + 65) Speed  30 ft. STR 19 (+4) DEX 17 (+3) CON 20 (+5) INT 5 (-3) WIS 12 (+1) CHA 13 (+1) Saving Throws  Str +7', 'legendary': False, 'size': 'Large', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The hezrou has advantage on saving throws against spells and other magical effects.Stench. Any creature that starts its turn within 10 feet of the hezrou must succeed on a DC 14 Constitution saving th"""
        return 'The hezrou has advantage on saving throws against spells and other magical effects.Stench. Any creature that starts its turn within 10 feet of the hezrou must succeed on a DC 14 Constitution saving th'

    def multiattack_attack(self) -> str:
        """The hezrou makes three attacks: one with its bite and two with its claws."""
        return 'The hezrou makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 15 (2d10 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 15 (2d10 + 4) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.'

