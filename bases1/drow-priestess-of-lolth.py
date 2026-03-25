# bases1/drow-priestess-of-lolth.py
"""
DrowPriestessOfLolth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-priestess-of-lolth
"""
from creature_base import GlobalCreatureBaseClass


class DrowPriestessOfLolth(GlobalCreatureBaseClass):
    """
    Medium humanoid (Elf) creature - DrowPriestessOfLolth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 71, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 12, 'INT': 13, 'WIS': 17, 'CHAR': 18, 'armor_class': 16, 'alignment': 'neutral evil Armor Class  16 (scale mail) Hit Points  71 (13d8 + 13) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 12 (+1) INT 13 (+1) WIS 17 (+3) CHA 18 (+4) Saving Throws  Con +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'multiattack', 'scourge', 'summon_demon_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's innate spellcasting ability is Charisma (spell save DC 15). She can"""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's innate spellcasting ability is Charisma (spell save DC 15). She can"

    def multiattack_attack(self) -> str:
        """The drow makes two scourge attacks."""
        return 'The drow makes two scourge attacks.'

    def scourge_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage plus 17 (5d6) poison damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage plus 17 (5d6) poison damage.'

    def summon_demon_(1/day)_attack(self) -> str:
        """The drow attempts to magically summon a yochlol with a 30 percent chance of success. If the attempt fails, the drow takes 5 (1d10) psychic damage. Otherwise, the summoned demon appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other demons. It remains for 10 minutes, until it or its summoner dies, or until its summoner dismisses it as an action."""
        return "The drow attempts to magically summon a yochlol with a 30 percent chance of success. If the attempt fails, the drow takes 5 (1d10) psychic damage. Otherwise, the summoned demon appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other demons. It remains for 10 minutes, until it or its summoner dies, or until its summoner dismisses it as an action."

