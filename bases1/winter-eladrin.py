# bases1/winter-eladrin.py
"""
WinterEladrin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=winter-eladrin
"""
from creature_base import GlobalCreatureBaseClass


class WinterEladrin(GlobalCreatureBaseClass):
    """
    Medium Fey (Elf) creature - WinterEladrin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 165, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 16, 'CON': 16, 'INT': 18, 'WIS': 17, 'CHAR': 13, 'armor_class': 19, 'alignment': 'typically Chaotic Neutral Armor Class  19 (natural armor) Hit Points  165 (22d8 + 66) Speed  30 ft. STR 11 (+0) DEX 16 (+3) CON 16 (+3) INT 18 (+4) WIS 17 (+3) CHA 13 (+1) Damage Resistances  cold Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fey (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'longsword', 'longbow', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The eladrin has advantage on saving throws against spells and other magical effects.Sorrowful Presence. Any non-eladrin creature that starts its turn within 60 feet of the eladrin must make a DC 13 Wi"""
        return 'The eladrin has advantage on saving throws against spells and other magical effects.Sorrowful Presence. Any non-eladrin creature that starts its turn within 60 feet of the eladrin must make a DC 13 Wi'

    def multiattack_attack(self) -> str:
        """The eladrin makes two Longsword or Longbow attacks. It can replace one attack with a use of Spellcasting."""
        return 'The eladrin makes two Longsword or Longbow attacks. It can replace one attack with a use of Spellcasting.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d8) slashing damage, or 5 (1d10) slashing damage if used with two hands, plus 13 (3d8) cold damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d8) slashing damage, or 5 (1d10) slashing damage if used with two hands, plus 13 (3d8) cold damage.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 13 (3d8) cold damage."""
        return 'Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 13 (3d8) cold damage.'

    def spellcasting_attack(self) -> str:
        """The eladrin casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 16):"""
        return 'The eladrin casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 16):'

