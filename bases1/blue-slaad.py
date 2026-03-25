# bases1/blue-slaad.py
"""
BlueSlaad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=blue-slaad
"""
from creature_base import GlobalCreatureBaseClass


class BlueSlaad(GlobalCreatureBaseClass):
    """
    Large aberration creature - BlueSlaad
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 123, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 15, 'CON': 18, 'INT': 7, 'WIS': 7, 'CHAR': 9, 'armor_class': 15, 'alignment': 'chaotic neutral Armor Class  15 (natural armor) Hit Points  123 (13d10 + 52) Speed  30 ft. STR 20 (+5) DEX 15 (+2) CON 18 (+4) INT 7 (-2) WIS 7 (-2) CHA 9 (-1) Skills  Perception + 1 Damage Resistances  acid', 'legendary': False, 'size': 'Large', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The slaad has advantage on saving throws against spells and other magical effects.Regeneration. The slaad regains 10 hit points at the start of its turn if it has at least 1 hit point."""
        return 'The slaad has advantage on saving throws against spells and other magical effects.Regeneration. The slaad regains 10 hit points at the start of its turn if it has at least 1 hit point.'

    def multiattack_attack(self) -> str:
        """The slaad makes three attacks: one with its bite and two with its claws."""
        return 'The slaad makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) piercing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage. If the target is a humanoid, it must succeed on a DC 15 Constitution saving throw or be infected with a disease called chaos phage. While infected, the target can't regain hit points, and its hit point maximum is reduced by 10 (3d6) every 24 hours. If the disease reduces the target's hit point maximum to 0, the target instantly transforms into a red slaad or, if it has the ability to cast spells of 3rd level or higher, a green slaad. Only a wish spell can reverse the transformation."""
        return "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage. If the target is a humanoid, it must succeed on a DC 15 Constitution saving throw or be infected with a disease called chaos phage. While infected, the target can't regain hit points, and its hit point maximum is reduced by 10 (3d6) every 24 hours. If the disease reduces the target's hit point maximum to 0, the target instantly transforms into a red slaad or, if it has the ability to cast spells of 3rd level or higher, a green slaad. Only a wish spell can reverse the transformation."

