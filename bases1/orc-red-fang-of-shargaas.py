# bases1/orc-red-fang-of-shargaas.py
"""
OrcRedFangOfShargaas creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-red-fang-of-shargaas
"""
from creature_base import GlobalCreatureBaseClass


class OrcRedFangOfShargaas(GlobalCreatureBaseClass):
    """
    Medium humanoid (Orc) creature - OrcRedFangOfShargaas
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 16, 'CON': 15, 'INT': 9, 'WIS': 11, 'CHAR': 9, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (studded leather) Hit Points  52 (8d8 + 16) Speed  30 ft. STR 11 (+0) DEX 16 (+3) CON 15 (+2) INT 9 (-1) WIS 11 (+0) CHA 9 (-1) Skills  Intimidation +1', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Orc)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['cunning_action', 'multiattack', 'scimitar', 'dart', 'veil_of_shargaas_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def cunning_action(self) -> str:
        """On each of its turns, the orc can use a bonus action to take the Dash, Disengage, or Hide action.Hand of Shargaas. The orc deals 2 extra dice of damage when it hits a target with a weapon attack (incl"""
        return 'On each of its turns, the orc can use a bonus action to take the Dash, Disengage, or Hide action.Hand of Shargaas. The orc deals 2 extra dice of damage when it hits a target with a weapon attack (incl'

    def multiattack_attack(self) -> str:
        """The orc makes two scimitar or dart attacks."""
        return 'The orc makes two scimitar or dart attacks.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 13 (3d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 13 (3d6 + 3) slashing damage.'

    def dart_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit: 10 (3d4 + 3) piercing damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit: 10 (3d4 + 3) piercing damage.'

    def veil_of_shargaas_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """The orc casts darkness without any components. Wisdom is its spellcasting ability."""
        return 'The orc casts darkness without any components. Wisdom is its spellcasting ability.'

