# bases1/death-dog.py
"""
DeathDog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-dog
"""
from creature_base import GlobalCreatureBaseClass


class DeathDog(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - DeathDog
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 14, 'INT': 3, 'WIS': 13, 'CHAR': 6, 'armor_class': 12, 'alignment': 'neutral evil Armor Class  12 Hit Points  39 (6d8 + 12) Speed  40 ft. STR 15 (+2) DEX 14 (+2) CON 14 (+2) INT 3 (-4) WIS 13 (+1) CHA 6 (-2) Skills  Perception +5', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['two-headed', 'multiattack', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def two-headed(self) -> str:
        """The dog has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious."""
        return 'The dog has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious.'

    def multiattack_attack(self) -> str:
        """The dog makes two bite attacks."""
        return 'The dog makes two bite attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage. If the target is a creature, it must succeed on a DC 12 Constitution saving throw against disease or become poisoned until the disease is cured. Every 24 hours that elapse, the creature must repeat the saving throw, reducing its hit point maximum by 5 (1d10) on a failure. This reduction lasts until the disease is cured. The creature dies if the disease reduces its hit point maximum to 0."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage. If the target is a creature, it must succeed on a DC 12 Constitution saving throw against disease or become poisoned until the disease is cured. Every 24 hours that elapse, the creature must repeat the saving throw, reducing its hit point maximum by 5 (1d10) on a failure. This reduction lasts until the disease is cured. The creature dies if the disease reduces its hit point maximum to 0.'

