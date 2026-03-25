# bases1/frost-salamander.py
"""
FrostSalamander creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frost-salamander
"""
from creature_base import GlobalCreatureBaseClass


class FrostSalamander(GlobalCreatureBaseClass):
    """
    Huge Elemental creature - FrostSalamander
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 168, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 12, 'CON': 18, 'INT': 7, 'WIS': 11, 'CHAR': 7, 'armor_class': 17, 'alignment': 'unaligned Armor Class  17 (natural armor) Hit Points  168 (16d12 + 64) Speed  60 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['burning_fury', 'multiattack', 'bite', 'claw', 'freezing_breath_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def burning_fury(self) -> str:
        """When the salamander takes fire damage, its Freezing Breath automatically recharges."""
        return 'When the salamander takes fire damage, its Freezing Breath automatically recharges.'

    def multiattack_attack(self) -> str:
        """The salamander makes one Bite attack and four Claw attacks."""
        return 'The salamander makes one Bite attack and four Claw attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 9 (1d8 + 5) piercing damage plus 5 (1d10) cold damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 9 (1d8 + 5) piercing damage plus 5 (1d10) cold damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 8 (1d6 + 5) piercing damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 8 (1d6 + 5) piercing damage.'

    def freezing_breath_(recharge_6)_attack(self) -> str:
        """The salamander exhales chill wind in a 60-foot cone. Each creature in that area must make a DC 17 Constitution saving throw, taking 44 (8d10) cold damage on a failed save, or half as much damage on a successful one."""
        return 'The salamander exhales chill wind in a 60-foot cone. Each creature in that area must make a DC 17 Constitution saving throw, taking 44 (8d10) cold damage on a failed save, or half as much damage on a successful one.'

