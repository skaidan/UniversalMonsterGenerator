# bases1/spy.py
"""
Spy creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spy
"""
from creature_base import GlobalCreatureBaseClass


class Spy(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Spy
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 15, 'CON': 10, 'INT': 12, 'WIS': 14, 'CHAR': 16, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 Hit Points  27 (6d8) Speed  30 ft. STR 10 (+0) DEX 15 (+2) CON 10 (+0) INT 12 (+1) WIS 14 (+2) CHA 16 (+3) Skills  Deception +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['cunning_action', 'multiattack', 'shortsword', 'hand_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def cunning_action(self) -> str:
        """On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action.Sneak Attack (1/Turn). The spy deals an extra 7 (2d6) damage when it hits a target with a weapon attack"""
        return 'On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action.Sneak Attack (1/Turn). The spy deals an extra 7 (2d6) damage when it hits a target with a weapon attack'

    def multiattack_attack(self) -> str:
        """The spy makes two melee attacks."""
        return 'The spy makes two melee attacks.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def hand_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

