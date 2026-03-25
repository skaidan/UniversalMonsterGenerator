# bases1/ettin.py
"""
Ettin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ettin
"""
from creature_base import GlobalCreatureBaseClass


class Ettin(GlobalCreatureBaseClass):
    """
    Large giant creature - Ettin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 8, 'CON': 17, 'INT': 6, 'WIS': 10, 'CHAR': 8, 'armor_class': 12, 'alignment': 'chaotic evil Armor Class  12 (natural armor) Hit Points  85 (10d10 + 30) Speed  40 ft. STR 21 (+5) DEX 8 (-1) CON 17 (+3) INT 6 (-2) WIS 10 (+0) CHA 8 (-1) Skills  Perception +4 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['two_heads', 'multiattack', 'battleaxe', 'morningstar']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def two_heads(self) -> str:
        """The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned and knocked unconscious.Wakeful. When one of the ettin's heads """
        return "The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned and knocked unconscious.Wakeful. When one of the ettin's heads "

    def multiattack_attack(self) -> str:
        """The ettin makes two attacks: one with its battleaxe and one with its morningstar."""
        return 'The ettin makes two attacks: one with its battleaxe and one with its morningstar.'

    def battleaxe_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage.'

    def morningstar_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) piercing damage.'

