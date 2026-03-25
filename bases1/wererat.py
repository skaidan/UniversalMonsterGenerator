# bases1/wererat.py
"""
Wererat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wererat
"""
from creature_base import GlobalCreatureBaseClass


class Wererat(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human creature - Wererat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 15, 'CON': 12, 'INT': 11, 'WIS': 10, 'CHAR': 8, 'armor_class': 12, 'alignment': 'Shapechanger)', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack_(humanoid_or_hybrid_form_only)', 'bite_(rat_or_hybrid_form_only)', 'shortsword_(humanoid_or_hybrid_form_only)', 'hand_crossbow_(humanoid_or_hybrid_form_only)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The wererat can use its action to polymorph into a rat-humanoid hybrid or into a giant rat, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each for"""
        return 'The wererat can use its action to polymorph into a rat-humanoid hybrid or into a giant rat, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each for'

    def multiattack_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """The wererat makes two attacks, only one of which can be a bite."""
        return 'The wererat makes two attacks, only one of which can be a bite.'

    def bite_(rat_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage. If the target is a humanoid, it must succeed on a DC 11 Constitution saving throw or be cursed with wererat lycanthropy."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage. If the target is a humanoid, it must succeed on a DC 11 Constitution saving throw or be cursed with wererat lycanthropy.'

    def shortsword_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def hand_crossbow_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

