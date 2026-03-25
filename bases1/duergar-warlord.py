# bases1/duergar-warlord.py
"""
DuergarWarlord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar-warlord
"""
from creature_base import GlobalCreatureBaseClass


class DuergarWarlord(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Dwarf) creature - DuergarWarlord
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 11, 'CON': 17, 'INT': 12, 'WIS': 12, 'CHAR': 14, 'armor_class': 20, 'alignment': 'any alignment Armor Class  20 (plate armor', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Dwarf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['duergar_resilience', 'multiattack', 'psychic-attuned_hammer', 'javelin', 'call_to_attack', 'invisibility_(recharge_4–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def duergar_resilience(self) -> str:
        """The duergar has advantage on saving throws against spells and the charmed, paralyzed, and poisoned conditions.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage on attack rolls, as """
        return 'The duergar has advantage on saving throws against spells and the charmed, paralyzed, and poisoned conditions.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage on attack rolls, as '

    def multiattack_attack(self) -> str:
        """The duergar makes three Psychic-Attuned Hammer or Javelin attacks and uses Call to Attack."""
        return 'The duergar makes three Psychic-Attuned Hammer or Javelin attacks and uses Call to Attack.'

    def psychic-attuned_hammer_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) bludgeoning damage, or 15 (2d10 + 4) bludgeoning damage while under the effect of Enlarge, plus 5 (1d10) psychic damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d10 + 4) bludgeoning damage, or 15 (2d10 + 4) bludgeoning damage while under the effect of Enlarge, plus 5 (1d10) psychic damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage, or 11 (2d6 + 4) piercing damage while under the effect of Enlarge."""
        return 'Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage, or 11 (2d6 + 4) piercing damage while under the effect of Enlarge.'

    def call_to_attack_attack(self) -> str:
        """Up to three allies within 120 feet of this duergar that can hear it can each use their reaction to make one weapon attack."""
        return 'Up to three allies within 120 feet of this duergar that can hear it can each use their reaction to make one weapon attack.'

    def invisibility_(recharge_4–6)_attack(self) -> str:
        """The duergar magically turns invisible for up to 1 hour or until it attacks, it forces a creature to make a saving throw, or its concentration is broken (as if concentrating on a spell). Any equipment the duergar wears or carries is invisible with it."""
        return 'The duergar magically turns invisible for up to 1 hour or until it attacks, it forces a creature to make a saving throw, or its concentration is broken (as if concentrating on a spell). Any equipment the duergar wears or carries is invisible with it.'

