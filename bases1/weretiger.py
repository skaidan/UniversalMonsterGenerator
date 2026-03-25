# bases1/weretiger.py
"""
Weretiger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=weretiger
"""
from creature_base import GlobalCreatureBaseClass


class Weretiger(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human creature - Weretiger
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 120, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 15, 'CON': 16, 'INT': 10, 'WIS': 13, 'CHAR': 11, 'armor_class': 12, 'alignment': 'Shapechanger)', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack_(humanoid_or_hybrid_form_only)', 'bite_(tiger_or_hybrid_form_only)', 'claw_(tiger_or_hybrid_form_only)', 'scimitar_(humanoid_or_hybrid_form_only)', 'longbow_(humanoid_or_hybrid_form_only)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The weretiger can use its action to polymorph into a tiger-humanoid hybrid or into a tiger, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each for"""
        return 'The weretiger can use its action to polymorph into a tiger-humanoid hybrid or into a tiger, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each for'

    def multiattack_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """In humanoid form, the weretiger makes two scimitar attacks or two longbow attacks. In hybrid form, it can attack like a humanoid or make two claw attacks."""
        return 'In humanoid form, the weretiger makes two scimitar attacks or two longbow attacks. In hybrid form, it can attack like a humanoid or make two claw attacks.'

    def bite_(tiger_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage. If the target is a humanoid, it must succeed on a DC 13 Constitution saving throw or be cursed with weretiger lycanthropy."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage. If the target is a humanoid, it must succeed on a DC 13 Constitution saving throw or be cursed with weretiger lycanthropy.'

    def claw_(tiger_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage.'

    def scimitar_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

    def longbow_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

