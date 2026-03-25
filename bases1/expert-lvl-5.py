# bases1/expert-lvl-5.py
"""
ExpertLvl5 creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=expert-lvl-5
"""
from creature_base import GlobalCreatureBaseClass


class ExpertLvl5(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - ExpertLvl5
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 17, 'CON': 12, 'INT': 13, 'WIS': 10, 'CHAR': 14, 'armor_class': 14, 'alignment': '- Armor Class  14 (studded leather) Hit Points  33 (6d8 + 6) Speed  30 ft. STR 10 (+0) DEX 17 (+3) CON 12 (+1) INT 13 (+1) WIS 10 (+0) CHA 14 (+2) Saving Throws  Dex +6 Skills  Acrobatics +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['helpful', 'shortsword', 'dagger', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def helpful(self) -> str:
        """The expert can take the Help action as a bonus action.Tools. The expert has thieves' tools and a musical instrument.Cunning Action. On the expert's turn in combat, it can take the Dash, Disengage, or """
        return "The expert can take the Help action as a bonus action.Tools. The expert has thieves' tools and a musical instrument.Cunning Action. On the expert's turn in combat, it can take the Dash, Disengage, or "

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def dagger_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +6 to hit, range 80/320 ft., one target. Hit: 7 (1d8 + 3) piercing damage."""
        return 'Ranged Weapon Attack: +6 to hit, range 80/320 ft., one target. Hit: 7 (1d8 + 3) piercing damage.'

