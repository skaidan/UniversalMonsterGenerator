# bases1/green-slaad.py
"""
GreenSlaad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=green-slaad
"""
from creature_base import GlobalCreatureBaseClass


class GreenSlaad(GlobalCreatureBaseClass):
    """
    Large aberration (Shapechanger) creature - GreenSlaad
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 11, 'WIS': 8, 'CHAR': 12, 'armor_class': 16, 'alignment': 'chaotic neutral Armor Class  16 (natural armor) Hit Points  127 (15d10 + 45) Speed  30 ft. STR 18 (+4) DEX 15 (+2) CON 16 (+3) INT 11 (+0) WIS 8 (-1) CHA 12 (+1) Skills  Arcana +3', 'legendary': False, 'size': 'Large', 'type': 'aberration (Shapechanger)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['shapechanger', 'multiattack', 'bite_(slaad_form_only)', 'claw_(slaad_form_only)', 'staff', 'hurl_flame']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def shapechanger(self) -> str:
        """The slaad can use its action to polymorph into a Small or Medium humanoid, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or ca"""
        return 'The slaad can use its action to polymorph into a Small or Medium humanoid, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or ca'

    def multiattack_attack(self) -> str:
        """The slaad makes three attacks: one with its bite and two with its claws or staff. Alternatively, it uses its Hurl Flame twice."""
        return 'The slaad makes three attacks: one with its bite and two with its claws or staff. Alternatively, it uses its Hurl Flame twice.'

    def bite_(slaad_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) piercing damage.'

    def claw_(slaad_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage.'

    def staff_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

    def hurl_flame_attack(self) -> str:
        """Ranged Spell Attack: +4 to hit, range 60 ft., one target. Hit: 10 (3d6) fire damage. The fire ignites flammable objects that aren't being worn or carried."""
        return "Ranged Spell Attack: +4 to hit, range 60 ft., one target. Hit: 10 (3d6) fire damage. The fire ignites flammable objects that aren't being worn or carried."

