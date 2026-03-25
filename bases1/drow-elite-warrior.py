# bases1/drow-elite-warrior.py
"""
DrowEliteWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=drow-elite-warrior
"""
from creature_base import GlobalCreatureBaseClass


class DrowEliteWarrior(GlobalCreatureBaseClass):
    """
    Medium humanoid (Elf) creature - DrowEliteWarrior
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 71, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 18, 'CON': 14, 'INT': 11, 'WIS': 13, 'CHAR': 12, 'armor_class': 18, 'alignment': 'neutral evil Armor Class  18 (studded leather', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fey_ancestry', 'multiattack', 'shortsword', 'hand_crossbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fey_ancestry(self) -> str:
        """The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's spellcasting ability is Charisma (spell save DC 12). It can innatel"""
        return "The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.Innate Spellcasting. The drow's spellcasting ability is Charisma (spell save DC 12). It can innatel"

    def multiattack_attack(self) -> str:
        """The drow makes two shortsword attacks."""
        return 'The drow makes two shortsword attacks.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage plus 10 (3d6) poison damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage plus 10 (3d6) poison damage.'

    def hand_crossbow_attack(self) -> str:
        """Ranged Weapon Attack: +7 to hit, range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target wakes up if it takes damage or if another creature takes an action to shake it awake."""
        return 'Ranged Weapon Attack: +7 to hit, range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target wakes up if it takes damage or if another creature takes an action to shake it awake.'

