# bases1/lamia.py
"""
Lamia creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lamia
"""
from creature_base import GlobalCreatureBaseClass


class Lamia(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Lamia
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 97, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 13, 'CON': 15, 'INT': 14, 'WIS': 15, 'CHAR': 16, 'armor_class': 13, 'alignment': 'chaotic evil Armor Class  13 (natural armor) Hit Points  97 (13d10 + 26) Speed  30 ft. STR 16 (+3) DEX 13 (+1) CON 15 (+2) INT 14 (+2) WIS 15 (+2) CHA 16 (+3) Skills  Deception +7', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'multiattack', 'claws', 'dagger', 'intoxicating_touch']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The lamia's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast the following spells, requiring no material components.At will: disguise self (any humanoid form), major im"""
        return "The lamia's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast the following spells, requiring no material components.At will: disguise self (any humanoid form), major im"

    def multiattack_attack(self) -> str:
        """The lamia makes two attacks: one with its claws and one with its dagger or Intoxicating Touch."""
        return 'The lamia makes two attacks: one with its claws and one with its dagger or Intoxicating Touch.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 14 (2d10 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 14 (2d10 + 3) slashing damage.'

    def dagger_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage.'

    def intoxicating_touch_attack(self) -> str:
        """Melee Spell Attack: +5 to hit, reach 5 ft., one creature. Hit: The target is magically cursed for 1 hour. Until the curse ends, the target has disadvantage on Wisdom saving throws and all ability checks."""
        return 'Melee Spell Attack: +5 to hit, reach 5 ft., one creature. Hit: The target is magically cursed for 1 hour. Until the curse ends, the target has disadvantage on Wisdom saving throws and all ability checks.'

