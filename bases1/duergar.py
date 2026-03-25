# bases1/duergar.py
"""
Duergar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar
"""
from creature_base import GlobalCreatureBaseClass


class Duergar(GlobalCreatureBaseClass):
    """
    Medium humanoid (Dwarf) creature - Duergar
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 11, 'CON': 14, 'INT': 11, 'WIS': 10, 'CHAR': 9, 'armor_class': 16, 'alignment': 'lawful evil Armor Class  16 (scale mail', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Dwarf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['duergar_resilience', 'enlarge_(recharges_after_a_short_or_long_rest)', 'war_pick', 'javelin', 'invisibility_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def duergar_resilience(self) -> str:
        """The duergar has advantage on saving throws against poison, spells, and illusions, as well as to resist being charmed or paralyzed.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage """
        return 'The duergar has advantage on saving throws against poison, spells, and illusions, as well as to resist being charmed or paralyzed.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage '

    def enlarge_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """For 1 minute, the duergar magically increases in size, along with anything it is wearing or carrying. While enlarged, the duergar is Large, doubles its damage dice on Strength-based weapon attacks (included in the attacks), and makes Strength checks and Strength saving throws with advantage. If the duergar lacks the room to become Large, it attains the maximum size possible in the space available."""
        return 'For 1 minute, the duergar magically increases in size, along with anything it is wearing or carrying. While enlarged, the duergar is Large, doubles its damage dice on Strength-based weapon attacks (included in the attacks), and makes Strength checks and Strength saving throws with advantage. If the duergar lacks the room to become Large, it attains the maximum size possible in the space available.'

    def war_pick_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage, or 11 (2d8 + 2) piercing damage while enlarged."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage, or 11 (2d8 + 2) piercing damage while enlarged.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 9 (2d6 + 2) piercing damage while enlarged."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 9 (2d6 + 2) piercing damage while enlarged.'

    def invisibility_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """The duergar magically turns invisible until it attacks, casts a spell, or uses its Enlarge, or until its concentration is broken, up to 1 hour (as if concentrating on a spell). Any equipment the duergar wears or carries is invisible with it."""
        return 'The duergar magically turns invisible until it attacks, casts a spell, or uses its Enlarge, or until its concentration is broken, up to 1 hour (as if concentrating on a spell). Any equipment the duergar wears or carries is invisible with it.'

