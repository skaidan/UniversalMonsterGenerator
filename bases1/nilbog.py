# bases1/nilbog.py
"""
Nilbog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nilbog
"""
from creature_base import GlobalCreatureBaseClass


class Nilbog(GlobalCreatureBaseClass):
    """
    Small Fey (Goblinoid) creature - Nilbog
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 14, 'CON': 10, 'INT': 10, 'WIS': 8, 'CHAR': 15, 'armor_class': 13, 'alignment': 'typically Chaotic Neutral Armor Class  13 (leather armor) Hit Points  7 (2d6) Speed  30 ft. STR 8 (-1) DEX 14 (+2) CON 10 (+0) INT 10 (+0) WIS 8 (-1) CHA 15 (+2) Skills  Stealth +6 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Small', 'type': 'Fey (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['nilbogism', 'fools_scepter', 'mocking_word', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def nilbogism(self) -> str:
        """Any creature that attempts to damage the nilbog must first succeed on a DC 12 Charisma saving throw or be charmed until the end of the creature's next turn. A creature charmed in this way must use its"""
        return "Any creature that attempts to damage the nilbog must first succeed on a DC 12 Charisma saving throw or be charmed until the end of the creature's next turn. A creature charmed in this way must use its"

    def fools_scepter_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage.'

    def mocking_word_attack(self) -> str:
        """The nilbog targets one creature it can see within 60 feet of it. The target must succeed on a DC 12 Wisdom saving throw or take 5 (2d4) psychic damage and have disadvantage on its next attack roll before the end of its next turn."""
        return 'The nilbog targets one creature it can see within 60 feet of it. The target must succeed on a DC 12 Wisdom saving throw or take 5 (2d4) psychic damage and have disadvantage on its next attack roll before the end of its next turn.'

    def spellcasting_attack(self) -> str:
        """The nilbog casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 12):"""
        return 'The nilbog casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 12):'

