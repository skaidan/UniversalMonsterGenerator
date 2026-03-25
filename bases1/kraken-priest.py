# bases1/kraken-priest.py
"""
KrakenPriest creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kraken-priest
"""
from creature_base import GlobalCreatureBaseClass


class KrakenPriest(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - KrakenPriest
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 10, 'CON': 16, 'INT': 10, 'WIS': 15, 'CHAR': 14, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  75 (10d8 + 30) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'thunderous_touch', 'thunderbolt', 'spellcasting', 'voice_of_the_kraken_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The priest can breathe air and water."""
        return 'The priest can breathe air and water.'

    def multiattack_attack(self) -> str:
        """The priest makes two Thunderous Touch or Thunderbolt attacks."""
        return 'The priest makes two Thunderous Touch or Thunderbolt attacks.'

    def thunderous_touch_attack(self) -> str:
        """Melee Spell Attack: +5 to hit, reach 5 ft., one target. Hit: 27 (5d10) thunder damage."""
        return 'Melee Spell Attack: +5 to hit, reach 5 ft., one target. Hit: 27 (5d10) thunder damage.'

    def thunderbolt_attack(self) -> str:
        """Ranged Spell Attack: +5 to hit, range 60 ft., one target. Hit: 11 (2d10) lightning damage plus 11 (2d10) thunder damage, and the target is knocked prone."""
        return 'Ranged Spell Attack: +5 to hit, range 60 ft., one target. Hit: 11 (2d10) lightning damage plus 11 (2d10) thunder damage, and the target is knocked prone.'

    def spellcasting_attack(self) -> str:
        """The priest casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 13):"""
        return 'The priest casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 13):'

    def voice_of_the_kraken_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """A kraken speaks through the priest with a thunderous voice audible within 300 feet. Creatures of the priest's choice that can hear the kraken's words (which are spoken in Abyssal, Infernal, or Primordial) must succeed on a DC 14 Wisdom saving throw or be frightened of the priest for 1 minute. A frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return "A kraken speaks through the priest with a thunderous voice audible within 300 feet. Creatures of the priest's choice that can hear the kraken's words (which are spoken in Abyssal, Infernal, or Primordial) must succeed on a DC 14 Wisdom saving throw or be frightened of the priest for 1 minute. A frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."

