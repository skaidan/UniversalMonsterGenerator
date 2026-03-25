# bases1/spellcaster-lvl-1.py
"""
SpellcasterLvl1 creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spellcaster-lvl-1
"""
from creature_base import GlobalCreatureBaseClass


class SpellcasterLvl1(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - SpellcasterLvl1
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 9, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 12, 'CON': 10, 'INT': 15, 'WIS': 14, 'CHAR': 13, 'armor_class': 12, 'alignment': '- Armor Class  12 (leather armor) Hit Points  9 (2d8) Speed  30 ft. STR 10 (+0) DEX 12 (+1) CON 10 (+0) INT 15 (+2) WIS 14 (+2) CHA 13 (+1) Saving Throws  Wis +4 Skills  Arcana +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magical_role', 'quatersatff']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magical_role(self) -> str:
        """Choose a role for the spellcaster: healer or mage. Your choice determines which Spellcasting trait to use below.Spellcasting (Healer). The spellcaster's spellcasting ability is Wisdom (spell save DC 1"""
        return "Choose a role for the spellcaster: healer or mage. Your choice determines which Spellcasting trait to use below.Spellcasting (Healer). The spellcaster's spellcasting ability is Wisdom (spell save DC 1"

    def quatersatff_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage, or 4 (1d8) bludgeoning damage if used with two hands."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage, or 4 (1d8) bludgeoning damage if used with two hands.'

