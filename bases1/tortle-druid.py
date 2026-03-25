# bases1/tortle-druid.py
"""
TortleDruid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tortle-druid
"""
from creature_base import GlobalCreatureBaseClass


class TortleDruid(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - TortleDruid
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 10, 'CON': 12, 'INT': 11, 'WIS': 15, 'CHAR': 12, 'armor_class': 17, 'alignment': 'any alignment Armor Class  17 (natural armor) Hit Points  33 (6d8 + 6) Speed  30 ft. STR 14 (+2) DEX 10 (+0) CON 12 (+1) INT 11 (+0) WIS 15 (+2) CHA 12 (+1) Skills  Animal Handling +4', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'multiattack', 'claw', 'natures_wrath', 'shell_defense', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The tortle can hold its breath for 1 hour."""
        return 'The tortle can hold its breath for 1 hour.'

    def multiattack_attack(self) -> str:
        """The tortle makes four Claw attacks or two Nature's Wrath attacks."""
        return "The tortle makes four Claw attacks or two Nature's Wrath attacks."

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.'

    def natures_wrath_attack(self) -> str:
        """Ranged Spell Attack: +4 to hit, range 90 ft., one target. Hit: 9 (2d6 + 2) damage of a type chosen by the tortle: cold, fire, lightning, or thunder."""
        return 'Ranged Spell Attack: +4 to hit, range 90 ft., one target. Hit: 9 (2d6 + 2) damage of a type chosen by the tortle: cold, fire, lightning, or thunder.'

    def shell_defense_attack(self) -> str:
        """The tortle withdraws into its shell. Until it emerges, it gains a +4 bonus to AC and has advantage on Strength and Constitution saving throws. While in its shell, the tortle is prone, its speed is 0 and can't increase, it has disadvantage on Dexterity saving throws, it can't take reactions, and the only action it can take is a bonus action to emerge."""
        return "The tortle withdraws into its shell. Until it emerges, it gains a +4 bonus to AC and has advantage on Strength and Constitution saving throws. While in its shell, the tortle is prone, its speed is 0 and can't increase, it has disadvantage on Dexterity saving throws, it can't take reactions, and the only action it can take is a bonus action to emerge."

    def spellcasting_attack(self) -> str:
        """The tortle casts one of the following spells, using Wisdom as the spellcasting ability (spell save DC 12):"""
        return 'The tortle casts one of the following spells, using Wisdom as the spellcasting ability (spell save DC 12):'

