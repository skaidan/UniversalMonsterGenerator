# bases1/venerable-shadow.py
"""
VenerableShadow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=venerable-shadow
"""
from creature_base import GlobalCreatureBaseClass


class VenerableShadow(GlobalCreatureBaseClass):
    """
    Medium undead creature - VenerableShadow
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 16, 'CON': 13, 'INT': 6, 'WIS': 12, 'CHAR': 10, 'armor_class': 13, 'alignment': 'chaotic evil Armor Class  13 (natural armor) Hit Points  27 (5d8 + 5) Speed  40 ft. STR 6 (-2) DEX 16 (+3) CON 13 (+1) INT 6 (-2) WIS 12 (+1) CHA 10 (+0) Skills  Stealth +5 (+7 in dim light or darkness) Damage Vulnerabilities  radiant Damage Resistances  acid', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amorphous', 'strength_drain']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amorphous(self) -> str:
        """The shadow can move through a space as narrow as 1 inch wide without squeezing.Shadow Stealth. While in dim light or darkness, the shadow can take the Hide action as a bonus action.Sunlight Weakness. """
        return 'The shadow can move through a space as narrow as 1 inch wide without squeezing.Shadow Stealth. While in dim light or darkness, the shadow can take the Hide action as a bonus action.Sunlight Weakness. '

    def strength_drain_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 12 (2d8 + 3) necrotic damage, and the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. If a non-evil humanoid dies from this attack, a new shadow (CR 1/2) rises from the corpse 1d2 hours later."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 12 (2d8 + 3) necrotic damage, and the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. If a non-evil humanoid dies from this attack, a new shadow (CR 1/2) rises from the corpse 1d2 hours later."

