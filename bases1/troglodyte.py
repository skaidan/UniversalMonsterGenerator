# bases1/troglodyte.py
"""
Troglodyte creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=troglodyte
"""
from creature_base import GlobalCreatureBaseClass


class Troglodyte(GlobalCreatureBaseClass):
    """
    Medium humanoid (Troglodyte) creature - Troglodyte
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 10, 'CON': 14, 'INT': 6, 'WIS': 10, 'CHAR': 6, 'armor_class': 11, 'alignment': 'chaotic evil Armor Class  11 (natural armor) Hit Points  13 (2d8 + 4) Speed  30 ft. STR 14 (+2) DEX 10 (+0) CON 14 (+2) INT 6 (-2) WIS 10 (+0) CHA 6 (-2) Skills  Stealth +2 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Troglodyte)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['chameleon_skin', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def chameleon_skin(self) -> str:
        """The troglodyte has advantage on Dexterity (Stealth) checks made to hide.Stench. Any creature other than a troglodyte that starts its turn within 5 feet of the troglodyte must succeed on a DC 12 Consti"""
        return 'The troglodyte has advantage on Dexterity (Stealth) checks made to hide.Stench. Any creature other than a troglodyte that starts its turn within 5 feet of the troglodyte must succeed on a DC 12 Consti'

    def multiattack_attack(self) -> str:
        """The troglodyte makes three attacks: one with its bite and two with its claws."""
        return 'The troglodyte makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.'

