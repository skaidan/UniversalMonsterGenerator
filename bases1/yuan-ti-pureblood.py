# bases1/yuan-ti-pureblood.py
"""
YuanTiPureblood creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-pureblood
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiPureblood(GlobalCreatureBaseClass):
    """
    Medium humanoid (Yuan-ti) creature - YuanTiPureblood
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 40, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 12, 'CON': 11, 'INT': 13, 'WIS': 12, 'CHAR': 14, 'armor_class': 11, 'alignment': 'neutral evil Armor Class  11 Hit Points  40 (9d8) Speed  30 ft. STR 11 (+0) DEX 12 (+1) CON 11 (+0) INT 13 (+1) WIS 12 (+1) CHA 14 (+2) Skills  Deception +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Yuan-ti)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'multiattack', 'scimitar', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The yuan-ti's spellcasting ability is Charisma (spell save DC 12). The yuan-ti can innately cast the following spells, requiring no material components:At will: animal friendship (snakes only)3/day ea"""
        return "The yuan-ti's spellcasting ability is Charisma (spell save DC 12). The yuan-ti can innately cast the following spells, requiring no material components:At will: animal friendship (snakes only)3/day ea"

    def multiattack_attack(self) -> str:
        """The yuan-ti makes two melee attacks."""
        return 'The yuan-ti makes two melee attacks.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) slashing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target. Hit: 4 (1d6 + 1) piercing damage plus 7 (2d6) poison damage."""
        return 'Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target. Hit: 4 (1d6 + 1) piercing damage plus 7 (2d6) poison damage.'

