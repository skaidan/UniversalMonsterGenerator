# bases1/drow.py
"""
Drow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow
"""
from creature_base import GlobalCreatureBaseClass


class Drow(GlobalCreatureBaseClass):
    """
    Medium humanoid (Elf) creature - Drow
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 10, 'INT': 11, 'WIS': 11, 'CHAR': 12, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (chain shirt) Hit Points  13 (3d8) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 10 (+0) INT 11 (+0) WIS 11 (+0) CHA 12 (+1) Skills  Perception +2', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'shortsword', 'hand_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's spellcasting ability is Charisma (spell save DC 11). It can innatel"""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's spellcasting ability is Charisma (spell save DC 11). It can innatel"

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def hand_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target wakes up if it takes damage or if another creature takes an action to shake it awake."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target wakes up if it takes damage or if another creature takes an action to shake it awake.'

