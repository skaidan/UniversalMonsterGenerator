# bases1/tortle.py
"""
Tortle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tortle
"""
from creature_base import GlobalCreatureBaseClass


class Tortle(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - Tortle
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 12, 'INT': 11, 'WIS': 13, 'CHAR': 12, 'armor_class': 17, 'alignment': 'any alignment Armor Class', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'challenge': '0', 'saving_throws': None, 'skills': 'Athletics +4, Survival +3', 'damage_resistances': None, 'damage_immunities': None, 'condition_immunities': None, 'senses': 'passive Perception 11', 'languages': None, 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'claw', 'spear', 'light_crossbow', 'shell_defense']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The tortle can hold its breath for 1 hour."""
        return 'The tortle can hold its breath for 1 hour.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands in melee."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands in melee.'

    def light_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +2 to hit, range 80/320 ft., one target. Hit: 4 (1d8) piercing damage."""
        return 'Ranged Weapon Attack: +2 to hit, range 80/320 ft., one target. Hit: 4 (1d8) piercing damage.'

    def shell_defense_attack(self) -> str:
        """The tortle withdraws into its shell. Until it emerges, it gains a +4 bonus to AC and has advantage on Strength and Constitution saving throws. While in its shell, the tortle is prone, its speed is 0 and can't increase, it has disadvantage on Dexterity saving throws, it can't take reactions, and the only action it can take is a bonus action to emerge."""
        return "The tortle withdraws into its shell. Until it emerges, it gains a +4 bonus to AC and has advantage on Strength and Constitution saving throws. While in its shell, the tortle is prone, its speed is 0 and can't increase, it has disadvantage on Dexterity saving throws, it can't take reactions, and the only action it can take is a bonus action to emerge."

