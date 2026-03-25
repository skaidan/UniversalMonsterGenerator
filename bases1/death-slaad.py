# bases1/death-slaad.py
"""
DeathSlaad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-slaad
"""
from creature_base import GlobalCreatureBaseClass


class DeathSlaad(GlobalCreatureBaseClass):
    """
    Medium aberration (Shapechanger) creature - DeathSlaad
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 170, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 15, 'CON': 19, 'INT': 15, 'WIS': 10, 'CHAR': 16, 'armor_class': 18, 'alignment': 'chaotic evil Armor Class  18 (natural armor) Hit Points  170 (20d8 + 80) Speed  30 ft. STR 20 (+5) DEX 15 (+2) CON 19 (+4) INT 15 (+2) WIS 10 (+0) CHA 16 (+3) Skills  Arcana +6', 'legendary': False, 'size': 'Medium', 'type': 'aberration (Shapechanger)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack', 'bite_(slaad_form_only)', 'claws_(slaad_form_only)', 'greatsword']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The slaad can use its action to polymorph into a Small or Medium humanoid, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or ca"""
        return 'The slaad can use its action to polymorph into a Small or Medium humanoid, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or ca'

    def multiattack_attack(self) -> str:
        """The slaad makes three attacks: one with its bite and two with its claws or greatsword."""
        return 'The slaad makes three attacks: one with its bite and two with its claws or greatsword.'

    def bite_(slaad_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) piercing damage plus 7 (2d6) necrotic damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) piercing damage plus 7 (2d6) necrotic damage.'

    def claws_(slaad_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 10 (1d10 + 5) slashing damage plus 7 (2d6) necrotic damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 10 (1d10 + 5) slashing damage plus 7 (2d6) necrotic damage.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage plus 7 (2d6) necrotic damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage plus 7 (2d6) necrotic damage.'

