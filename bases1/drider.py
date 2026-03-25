# bases1/drider.py
"""
Drider creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drider
"""
from creature_base import GlobalCreatureBaseClass


class Drider(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Drider
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 123, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 16, 'CON': 18, 'INT': 13, 'WIS': 14, 'CHAR': 12, 'armor_class': 19, 'alignment': 'chaotic evil Armor Class  19 (natural armor) Hit Points  123 (13d10 + 52) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'multiattack', 'bite', 'longsword', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The drider has advantage on saving throws against being charmed, and magic can't put the drider to sleep.Innate Spellcasting. The drider's innate spellcasting ability is Wisdom (spell save DC 13). The"""
        return "The drider has advantage on saving throws against being charmed, and magic can't put the drider to sleep.Innate Spellcasting. The drider's innate spellcasting ability is Wisdom (spell save DC 13). The"

    def multiattack_attack(self) -> str:
        """The drider makes three attacks, either with its longsword or its longbow. It can replace one of those attacks with a bite attack."""
        return 'The drider makes three attacks, either with its longsword or its longbow. It can replace one of those attacks with a bite attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 2 (1d4) piercing damage plus 9 (2d8) poison damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 2 (1d4) piercing damage plus 9 (2d8) poison damage.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) poison damage."""
        return 'Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) poison damage.'

