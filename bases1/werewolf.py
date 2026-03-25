# bases1/werewolf.py
"""
Werewolf creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=werewolf
"""
from creature_base import GlobalCreatureBaseClass


class Werewolf(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human creature - Werewolf
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 13, 'CON': 14, 'INT': 10, 'WIS': 11, 'CHAR': 10, 'armor_class': 11, 'alignment': 'Shapechanger)', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack_(humanoid_or_hybrid_form_only)', 'bite_(wolf_or_hybrid_form_only)', 'claws_(hybrid_form_only)', 'spear_(humanoid_form_only)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The werewolf can use its action to polymorph into a wolf-humanoid hybrid or into a wolf, or back into its true form, which is humanoid. Its statistics, other than its AC, are the same in each form. An"""
        return 'The werewolf can use its action to polymorph into a wolf-humanoid hybrid or into a wolf, or back into its true form, which is humanoid. Its statistics, other than its AC, are the same in each form. An'

    def multiattack_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """The werewolf makes two attacks: two with its spear (humanoid form) or one with its bite and one with its claws (hybrid form)."""
        return 'The werewolf makes two attacks: two with its spear (humanoid form) or one with its bite and one with its claws (hybrid form).'

    def bite_(wolf_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage. If the target is a humanoid, it must succeed on a DC 12 Constitution saving throw or be cursed with werewolf lycanthropy."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage. If the target is a humanoid, it must succeed on a DC 12 Constitution saving throw or be cursed with werewolf lycanthropy.'

    def claws_(hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (2d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (2d4 + 2) slashing damage.'

    def spear_(humanoid_form_only)_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one creature. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one creature. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack.'

