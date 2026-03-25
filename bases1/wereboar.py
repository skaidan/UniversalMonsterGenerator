# bases1/wereboar.py
"""
Wereboar creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wereboar
"""
from creature_base import GlobalCreatureBaseClass


class Wereboar(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human creature - Wereboar
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 78, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 15, 'INT': 10, 'WIS': 11, 'CHAR': 8, 'armor_class': 10, 'alignment': 'Shapechanger)', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack_(humanoid_or_hybrid_form_only)', 'maul_(humanoid_or_hybrid_form_only)', 'tusks_(boar_or_hybrid_form_only)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The wereboar can use its action to polymorph into a boar-humanoid hybrid or into a boar, or back into its true form, which is humanoid. Its statistics, other than its AC, are the same in each form. An"""
        return 'The wereboar can use its action to polymorph into a boar-humanoid hybrid or into a boar, or back into its true form, which is humanoid. Its statistics, other than its AC, are the same in each form. An'

    def multiattack_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """The wereboar makes two attacks, only one of which can be with its tusks."""
        return 'The wereboar makes two attacks, only one of which can be with its tusks.'

    def maul_(humanoid_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage.'

    def tusks_(boar_or_hybrid_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage. If the target is a humanoid, it must succeed on a DC 12 Constitution saving throw or be cursed with wereboar lycanthropy."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage. If the target is a humanoid, it must succeed on a DC 12 Constitution saving throw or be cursed with wereboar lycanthropy.'

