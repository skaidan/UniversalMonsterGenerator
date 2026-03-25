# bases1/nightwalker.py
"""
Nightwalker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nightwalker
"""
from creature_base import GlobalCreatureBaseClass


class Nightwalker(GlobalCreatureBaseClass):
    """
    Huge Undead creature - Nightwalker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 337, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 19, 'CON': 24, 'INT': 6, 'WIS': 9, 'CHAR': 8, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 Hit Points  337 (25d12 + 175) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['annihilating_aura', 'multiattack', 'enervating_focus', 'finger_of_doom_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def annihilating_aura(self) -> str:
        """Any creature that starts its turn within 30 feet of the nightwalker must succeed on a DC 21 Constitution saving throw or take 21 (6d6) necrotic damage. Undead are immune to this aura.Life Eater. A cre"""
        return 'Any creature that starts its turn within 30 feet of the nightwalker must succeed on a DC 21 Constitution saving throw or take 21 (6d6) necrotic damage. Undead are immune to this aura.Life Eater. A cre'

    def multiattack_attack(self) -> str:
        """The nightwalker makes two Enervating Focus attacks, one of which can be replaced by Finger of Doom, if available."""
        return 'The nightwalker makes two Enervating Focus attacks, one of which can be replaced by Finger of Doom, if available.'

    def enervating_focus_attack(self) -> str:
        """Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 28 (5d8 + 6) necrotic damage. The target must succeed on a DC 21 Constitution saving throw or its hit point maximum is reduced by an amount equal to the necrotic damage taken. This reduction lasts until the target finishes a long rest. The target dies if its hit point maximum is reduced to 0."""
        return 'Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 28 (5d8 + 6) necrotic damage. The target must succeed on a DC 21 Constitution saving throw or its hit point maximum is reduced by an amount equal to the necrotic damage taken. This reduction lasts until the target finishes a long rest. The target dies if its hit point maximum is reduced to 0.'

    def finger_of_doom_(recharge_6)_attack(self) -> str:
        """The nightwalker points at one creature it can see within 300 feet of it. The target must succeed on a DC 21 Wisdom saving throw or take 39 (6d12) necrotic damage and become frightened until the end of the nightwalker's next turn. While frightened in this way, the creature is also paralyzed. If a target's saving throw is successful, the target is immune to the nightwalker's Finger of Doom for the next 24 hours."""
        return "The nightwalker points at one creature it can see within 300 feet of it. The target must succeed on a DC 21 Wisdom saving throw or take 39 (6d12) necrotic damage and become frightened until the end of the nightwalker's next turn. While frightened in this way, the creature is also paralyzed. If a target's saving throw is successful, the target is immune to the nightwalker's Finger of Doom for the next 24 hours."

