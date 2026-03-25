# bases1/catoblepas.py
"""
Catoblepas creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=catoblepas
"""
from creature_base import GlobalCreatureBaseClass


class Catoblepas(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - Catoblepas
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 84, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 12, 'CON': 21, 'INT': 3, 'WIS': 14, 'CHAR': 8, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  84 (8d10 + 40) Speed  30 ft. STR 19 (+4) DEX 12 (+1) CON 21 (+5) INT 3 (-4) WIS 14 (+2) CHA 8 (-1) Skills  Perception +5 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['stench', 'tail', 'death_ray_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def stench(self) -> str:
        """Any creature other than a catoblepas that starts its turn within 10 feet of the catoblepas must succeed on a DC 16 Constitution saving throw or be poisoned until the start of the creature's next turn."""
        return "Any creature other than a catoblepas that starts its turn within 10 feet of the catoblepas must succeed on a DC 16 Constitution saving throw or be poisoned until the start of the creature's next turn."

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 21 (5d6 + 4) bludgeoning damage, and the target must succeed on a DC 16 Constitution saving throw or be stunned until the start of the catoblepas's next turn."""
        return "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 21 (5d6 + 4) bludgeoning damage, and the target must succeed on a DC 16 Constitution saving throw or be stunned until the start of the catoblepas's next turn."

    def death_ray_(recharge_5–6)_attack(self) -> str:
        """The catoblepas targets one creature it can see within 30 feet of it. The target must make a DC 16 Constitution saving throw, taking 36 (8d8) necrotic damage on a failed save, or half as much damage on a successful one. If the saving throw fails by 5 or more, the target instead takes 64 necrotic damage. The target dies if reduced to 0 hit points by this ray."""
        return 'The catoblepas targets one creature it can see within 30 feet of it. The target must make a DC 16 Constitution saving throw, taking 36 (8d8) necrotic damage on a failed save, or half as much damage on a successful one. If the saving throw fails by 5 or more, the target instead takes 64 necrotic damage. The target dies if reduced to 0 hit points by this ray.'

