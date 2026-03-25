# bases1/chasme.py
"""
Chasme creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=chasme
"""
from creature_base import GlobalCreatureBaseClass


class Chasme(GlobalCreatureBaseClass):
    """
    Large fiend (Demon) creature - Chasme
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 84, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 15, 'CON': 12, 'INT': 11, 'WIS': 14, 'CHAR': 10, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (natural armor) Hit Points  84 (13d10 + 13) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['drone', 'proboscis']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def drone(self) -> str:
        """The chasme produces a horrid droning sound to which demons are immune. Any other creature that starts its turn with in 30 feet of the chasme must succeed on a DC 12 Constitution saving throw or fall u"""
        return 'The chasme produces a horrid droning sound to which demons are immune. Any other creature that starts its turn with in 30 feet of the chasme must succeed on a DC 12 Constitution saving throw or fall u'

    def proboscis_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 16 (4d6 + 2) piercing damage plus 24 (7d6) necrotic damage, and the target's hit point maximum is reduced by an amount equal to the necrotic damage taken. If this effect reduces a creature's hit point maximum to 0, the creature dies. This reduction to a creature's hit point maximum lasts until the creature finishes a long rest or until it is affected by a spell like greater restoration."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 16 (4d6 + 2) piercing damage plus 24 (7d6) necrotic damage, and the target's hit point maximum is reduced by an amount equal to the necrotic damage taken. If this effect reduces a creature's hit point maximum to 0, the creature dies. This reduction to a creature's hit point maximum lasts until the creature finishes a long rest or until it is affected by a spell like greater restoration."

