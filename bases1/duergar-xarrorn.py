# bases1/duergar-xarrorn.py
"""
DuergarXarrorn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar-xarrorn
"""
from creature_base import GlobalCreatureBaseClass


class DuergarXarrorn(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Dwarf) creature - DuergarXarrorn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 11, 'CON': 14, 'INT': 11, 'WIS': 10, 'CHAR': 9, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate armor) Hit Points  26 (4d8 + 8) Speed  25 ft. STR 16 (+3) DEX 11 (+0) CON 14 (+2) INT 11 (+0) WIS 10 (+0) CHA 9 (-1) Damage Resistances  poison Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Dwarf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['duergar_resilience', 'fire_lance', 'fire_spray_(recharge_5–6)', 'invisibility_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def duergar_resilience(self) -> str:
        """The duergar has advantage on saving throws against spells and the charmed, paralyzed, and poisoned conditions.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage on attack rolls, as """
        return 'The duergar has advantage on saving throws against spells and the charmed, paralyzed, and poisoned conditions.Sunlight Sensitivity. While in sunlight, the duergar has disadvantage on attack rolls, as '

    def fire_lance_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 9 (1d12 + 3) piercing damage, or 16 (2d12 + 3) piercing damage while under the effect of Enlarge, plus 3 (1d6) fire damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 9 (1d12 + 3) piercing damage, or 16 (2d12 + 3) piercing damage while under the effect of Enlarge, plus 3 (1d6) fire damage.'

    def fire_spray_(recharge_5–6)_attack(self) -> str:
        """From its fire lance, the duergar shoots a 15-foot cone of fire or a line of fire 30 feet long and 5 feet wide. Each creature in that area must make a DC 12 Dexterity saving throw, taking 10 (3d6) fire damage on a failed save, or half as much damage on a successful one."""
        return 'From its fire lance, the duergar shoots a 15-foot cone of fire or a line of fire 30 feet long and 5 feet wide. Each creature in that area must make a DC 12 Dexterity saving throw, taking 10 (3d6) fire damage on a failed save, or half as much damage on a successful one.'

    def invisibility_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """The duergar magically turns invisible for up to 1 hour or until it attacks, it forces a creature to make a saving throw, or its concentration is broken (as if concentrating on a spell). Any equipment the duergar wears or carries is invisible with it."""
        return 'The duergar magically turns invisible for up to 1 hour or until it attacks, it forces a creature to make a saving throw, or its concentration is broken (as if concentrating on a spell). Any equipment the duergar wears or carries is invisible with it.'

