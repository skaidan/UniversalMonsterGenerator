# bases1/ki-rin.py
"""
KiRin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ki-rin
"""
from creature_base import GlobalCreatureBaseClass


class KiRin(GlobalCreatureBaseClass):
    """
    Large Celestial creature - KiRin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 153, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 16, 'CON': 16, 'INT': 19, 'WIS': 20, 'CHAR': 20, 'armor_class': 20, 'alignment': 'typically Lawful Good Armor Class  20 (natural armor) Hit Points  153 (18d10 + 54) Speed  60 ft.', 'legendary': False, 'size': 'Large', 'type': 'Celestial', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(3/day)', 'multiattack', 'hoof', 'horn', 'sacred_fire', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(3/day)(self) -> str:
        """If the ki-rin fails a saving throw, it can choose to succeed instead.Magic Resistance. The ki-rin has advantage on saving throws against spells and other magical effects."""
        return 'If the ki-rin fails a saving throw, it can choose to succeed instead.Magic Resistance. The ki-rin has advantage on saving throws against spells and other magical effects.'

    def multiattack_attack(self) -> str:
        """The ki-rin makes two Hoof attacks and one Horn attack, or it makes two Sacred Fire attacks."""
        return 'The ki-rin makes two Hoof attacks and one Horn attack, or it makes two Sacred Fire attacks.'

    def hoof_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 10 (2d4 + 5) force damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 15 ft., one target. Hit: 10 (2d4 + 5) force damage.'

    def horn_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) radiant damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) radiant damage.'

    def sacred_fire_attack(self) -> str:
        """Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 18 (3d8 + 5) radiant damage."""
        return 'Ranged Spell Attack: +9 to hit, range 120 ft., one target. Hit: 18 (3d8 + 5) radiant damage.'

    def spellcasting_attack(self) -> str:
        """The ki-rin casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 17):"""
        return 'The ki-rin casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 17):'

