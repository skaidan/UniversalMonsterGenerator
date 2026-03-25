# bases1/doppelganger.py
"""
Doppelganger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=doppelganger
"""
from creature_base import GlobalCreatureBaseClass


class Doppelganger(GlobalCreatureBaseClass):
    """
    Medium monstrosity (Shapechanger) creature - Doppelganger
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 18, 'CON': 14, 'INT': 11, 'WIS': 12, 'CHAR': 14, 'armor_class': 14, 'alignment': 'neutral Armor Class  14 Hit Points  52 (8d8 + 16) Speed  30 ft. STR 11 (+0) DEX 18 (+4) CON 14 (+2) INT 11 (+0) WIS 12 (+1) CHA 14 (+2) Skills  Deception +6', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity (Shapechanger)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack', 'slam', 'read_thoughts']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The doppelganger can use its action to polymorph into a Small or Medium humanoid it has seen, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment """
        return 'The doppelganger can use its action to polymorph into a Small or Medium humanoid it has seen, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment '

    def multiattack_attack(self) -> str:
        """The doppelganger makes two melee attacks."""
        return 'The doppelganger makes two melee attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage.'

    def read_thoughts_attack(self) -> str:
        """The doppelganger magically reads the surface thoughts of one creature within 60 feet of it. The effect can penetrate barriers, but 3 feet of wood or dirt, 2 feet of stone, 2 inches of metal, or a thin sheet of lead blocks it. While the target is in range, the doppelganger can continue reading its thoughts, as long as the doppelganger's concentration isn't broken (as if concentrating on a spell). While reading the target's mind, the doppelganger has advantage on Wisdom (Insight) and Charisma (Deception, Intimidation, and Persuasion) checks against the target."""
        return "The doppelganger magically reads the surface thoughts of one creature within 60 feet of it. The effect can penetrate barriers, but 3 feet of wood or dirt, 2 feet of stone, 2 inches of metal, or a thin sheet of lead blocks it. While the target is in range, the doppelganger can continue reading its thoughts, as long as the doppelganger's concentration isn't broken (as if concentrating on a spell). While reading the target's mind, the doppelganger has advantage on Wisdom (Insight) and Charisma (Deception, Intimidation, and Persuasion) checks against the target."

