# bases1/glabrezu.py
"""
Glabrezu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=glabrezu
"""
from creature_base import GlobalCreatureBaseClass


class Glabrezu(GlobalCreatureBaseClass):
    """
    Large fiend (Demon) creature - Glabrezu
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 157, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 15, 'CON': 21, 'INT': 19, 'WIS': 17, 'CHAR': 16, 'armor_class': 17, 'alignment': 'chaotic evil Armor Class  17 (natural armor) Hit Points  157 (15d10 + 75) Speed  40 ft. STR 20 (+5) DEX 15 (+2) CON 21 (+5) INT 19 (+4) WIS 17 (+3) CHA 16 (+3) Saving Throws  Str +9', 'legendary': False, 'size': 'Large', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'multiattack', 'pincer', 'fist']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The glabrezu's spellcasting ability is Intelligence (spell save DC 16). The glabrezu can innately cast the following spells, requiring no material components:At will: darkness, detect magic, dispel ma"""
        return "The glabrezu's spellcasting ability is Intelligence (spell save DC 16). The glabrezu can innately cast the following spells, requiring no material components:At will: darkness, detect magic, dispel ma"

    def multiattack_attack(self) -> str:
        """The glabrezu makes four attacks: two with its pincers and two with its fists. Alternatively, it makes two attacks with its pincers and casts one spell."""
        return 'The glabrezu makes four attacks: two with its pincers and two with its fists. Alternatively, it makes two attacks with its pincers and casts one spell.'

    def pincer_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage. If the target is a Medium or smaller creature, it is grappled (escape DC 15). The glabrezu has two pincers, each of which can grapple only one target."""
        return 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage. If the target is a Medium or smaller creature, it is grappled (escape DC 15). The glabrezu has two pincers, each of which can grapple only one target.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) bludgeoning damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) bludgeoning damage.'

