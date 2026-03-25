# bases1/shadow.py
"""
Shadow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shadow
"""
from creature_base import GlobalCreatureBaseClass


class Shadow(GlobalCreatureBaseClass):
    """
    Medium undead creature - Shadow
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 16, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 14, 'CON': 13, 'INT': 6, 'WIS': 10, 'CHAR': 8, 'armor_class': 12, 'alignment': 'chaotic evil Armor Class  12 Hit Points  16 (3d8 + 3) Speed  40 ft. STR 6 (-2) DEX 14 (+2) CON 13 (+1) INT 6 (-2) WIS 10 (+0) CHA 8 (-1) Skills  Stealth +4 (+6 in dim light or darkness) Damage Vulnerabilities  radiant Damage Resistances  acid', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amorphous', 'strength_drain']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amorphous(self) -> str:
        """The shadow can move through a space as narrow as 1 inch wide without squeezing.Shadow Stealth. While in dim light or darkness, the shadow can take the Hide action as a bonus action.Sunlight Weakness. """
        return 'The shadow can move through a space as narrow as 1 inch wide without squeezing.Shadow Stealth. While in dim light or darkness, the shadow can take the Hide action as a bonus action.Sunlight Weakness. '

    def strength_drain_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 9 (2d6 + 2) necrotic damage, and the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 9 (2d6 + 2) necrotic damage, and the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later."

