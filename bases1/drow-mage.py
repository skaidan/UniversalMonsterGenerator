# bases1/drow-mage.py
"""
DrowMage creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-mage
"""
from creature_base import GlobalCreatureBaseClass


class DrowMage(GlobalCreatureBaseClass):
    """
    Medium humanoid (Elf) creature - DrowMage
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 10, 'INT': 17, 'WIS': 13, 'CHAR': 12, 'armor_class': 12, 'alignment': 'neutral evil Armor Class  12 (15 with  mage armor ) Hit Points  45 (10d8) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 10 (+0) INT 17 (+3) WIS 13 (+1) CHA 12 (+1) Skills  Arcana +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'staff', 'summon_demon_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's innate spellcasting ability is Charisma (spell save DC 12). It can """
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's innate spellcasting ability is Charisma (spell save DC 12). It can "

    def staff_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) bludgeoning damage, or 3 (1d8 - 1) bludgeoning damage if used with two hands, plus 3 (1d 6) poison damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) bludgeoning damage, or 3 (1d8 - 1) bludgeoning damage if used with two hands, plus 3 (1d 6) poison damage.'

    def summon_demon_(1/day)_attack(self) -> str:
        """The drow magically summons a quasit, or attempts to summon a shadow demon with a 50 percent chance of success. The summoned demon appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other demons. It remains for 10 minutes, until it or its summoner dies, or until its summoner dismisses it as an action."""
        return "The drow magically summons a quasit, or attempts to summon a shadow demon with a 50 percent chance of success. The summoned demon appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other demons. It remains for 10 minutes, until it or its summoner dies, or until its summoner dismisses it as an action."

