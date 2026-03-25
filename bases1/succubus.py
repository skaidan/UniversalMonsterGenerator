# bases1/succubus.py
"""
Succubus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=succubus
"""
from creature_base import GlobalCreatureBaseClass


class Succubus(GlobalCreatureBaseClass):
    """
    Medium fiend (Shapechanger) creature - Succubus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 66, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 17, 'CON': 13, 'INT': 15, 'WIS': 12, 'CHAR': 20, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (natural armor) Hit Points  66 (12d8 + 12) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'fiend (Shapechanger)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['telepathic_bond', 'claw_(fiend_form_only)', 'charm', 'draining_kiss', 'etherealness']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def telepathic_bond(self) -> str:
        """The fiend ignores the range restriction on its telepathy when communicating with a creature it has charmed. The two don't even need to be on the same plane of existence.Shapechanger. The fiend can use"""
        return "The fiend ignores the range restriction on its telepathy when communicating with a creature it has charmed. The two don't even need to be on the same plane of existence.Shapechanger. The fiend can use"

    def claw_(fiend_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

    def charm_attack(self) -> str:
        """One humanoid the fiend can see within 30 feet of it must succeed on a DC 15 Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's verbal or telepathic commands. If the target suffers any harm or receives a suicidal command, it can repeat the saving throw, ending the effect on a success. If the target successfully saves against the effect, or if the effect on it ends, the target is immune to this fiend's Charm for the next 24 hours. The fiend can have only one target charmed at a time. If it charms another, the effect on the previous target ends."""
        return "One humanoid the fiend can see within 30 feet of it must succeed on a DC 15 Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's verbal or telepathic commands. If the target suffers any harm or receives a suicidal command, it can repeat the saving throw, ending the effect on a success. If the target successfully saves against the effect, or if the effect on it ends, the target is immune to this fiend's Charm for the next 24 hours. The fiend can have only one target charmed at a time. If it charms another, the effect on the previous target ends."

    def draining_kiss_attack(self) -> str:
        """The fiend kisses a creature charmed by it or a willing creature. The target must make a DC 15 Constitution saving throw against this magic, taking 32 (5d10 + 5) psychic damage on a failed save, or half as much damage on a successful one. The target's hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."""
        return "The fiend kisses a creature charmed by it or a willing creature. The target must make a DC 15 Constitution saving throw against this magic, taking 32 (5d10 + 5) psychic damage on a failed save, or half as much damage on a successful one. The target's hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."

    def etherealness_attack(self) -> str:
        """The fiend magically enters the Ethereal Plane from the Material Plane, or vice versa."""
        return 'The fiend magically enters the Ethereal Plane from the Material Plane, or vice versa.'

