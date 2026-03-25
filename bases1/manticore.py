# bases1/manticore.py
"""
Manticore creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=manticore
"""
from creature_base import GlobalCreatureBaseClass


class Manticore(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Manticore
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 16, 'CON': 17, 'INT': 7, 'WIS': 12, 'CHAR': 8, 'armor_class': 14, 'alignment': 'lawful evil Armor Class  14 (natural armor) Hit Points  68 (8d10 + 24) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['tail_spike_regrowth', 'multiattack', 'bite', 'claw', 'tail_spike']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def tail_spike_regrowth(self) -> str:
        """The manticore has twenty-four tail spikes. Used spikes regrow when the manticore finishes a long rest."""
        return 'The manticore has twenty-four tail spikes. Used spikes regrow when the manticore finishes a long rest.'

    def multiattack_attack(self) -> str:
        """The manticore makes three attacks: one with its bite and two with its claws or three with its tail spikes."""
        return 'The manticore makes three attacks: one with its bite and two with its claws or three with its tail spikes.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

    def tail_spike_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 100/200 ft., one target. Hit: 7 (1d8 + 3) piercing damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 100/200 ft., one target. Hit: 7 (1d8 + 3) piercing damage.'

