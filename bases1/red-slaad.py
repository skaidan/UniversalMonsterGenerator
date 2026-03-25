# bases1/red-slaad.py
"""
RedSlaad creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=red-slaad
"""
from creature_base import GlobalCreatureBaseClass


class RedSlaad(GlobalCreatureBaseClass):
    """
    Large aberration creature - RedSlaad
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 16, 'INT': 6, 'WIS': 6, 'CHAR': 7, 'armor_class': 14, 'alignment': 'chaotic neutral Armor Class  14 (natural armor) Hit Points  93 (11d10 + 33) Speed  30 ft. STR 16 (+3) DEX 12 (+1) CON 16 (+3) INT 6 (-2) WIS 6 (-2) CHA 7 (-2) Skills  Perception + 1 Damage Resistances  acid', 'legendary': False, 'size': 'Large', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The slaad has advantage on saving throws against spells and other magical effects.Regeneration. The slaad regains 10 hit points at the start of its turn if it has at least 1 hit point."""
        return 'The slaad has advantage on saving throws against spells and other magical effects.Regeneration. The slaad regains 10 hit points at the start of its turn if it has at least 1 hit point.'

    def multiattack_attack(self) -> str:
        """The slaad makes three attacks: one with its bite and two with its claws."""
        return 'The slaad makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage. If the target is a humanoid, it must succeed on a DC 14 Constitution saving throw or be infected with a disease-a minuscule slaad egg. A humanoid host can carry only one slaad egg to term at a time. Over three months, the egg moves to the chest cavity, gestates, and forms a slaad tadpole. In the 24-hour period before giving birth, the host starts to feel unwell, its speed is halved, and it has disadvantage on attack rolls, ability checks, and saving throws. At birth, the tadpole chews its way through vital organs and out of the host's chest in 1 round, killing the host in the process. If the disease is cured before the tadpole's emergence, the unborn slaad is disintegrated."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage. If the target is a humanoid, it must succeed on a DC 14 Constitution saving throw or be infected with a disease-a minuscule slaad egg. A humanoid host can carry only one slaad egg to term at a time. Over three months, the egg moves to the chest cavity, gestates, and forms a slaad tadpole. In the 24-hour period before giving birth, the host starts to feel unwell, its speed is halved, and it has disadvantage on attack rolls, ability checks, and saving throws. At birth, the tadpole chews its way through vital organs and out of the host's chest in 1 round, killing the host in the process. If the disease is cured before the tadpole's emergence, the unborn slaad is disintegrated."

