# bases1/vampire-spawn.py
"""
VampireSpawn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vampire-spawn
"""
from creature_base import GlobalCreatureBaseClass


class VampireSpawn(GlobalCreatureBaseClass):
    """
    Medium undead creature - VampireSpawn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 82, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 16, 'CON': 16, 'INT': 11, 'WIS': 10, 'CHAR': 12, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (natural armor) Hit Points  82 (11d8 + 33) Speed  30 ft. STR 16 (+3) DEX 16 (+3) CON 16 (+3) INT 11 (+0) WIS 10 (+0) CHA 12 (+1) Saving Throws  Dex +6', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['regeneration', 'multiattack', 'claws', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def regeneration(self) -> str:
        """The vampire regains 10 hit points at the start of its turn if it has at least 1 hit point and isn't in sunlight or running water. If the vampire takes radiant damage or damage from holy water, this tr"""
        return "The vampire regains 10 hit points at the start of its turn if it has at least 1 hit point and isn't in sunlight or running water. If the vampire takes radiant damage or damage from holy water, this tr"

    def multiattack_attack(self) -> str:
        """The vampire makes two attacks, only one of which can be a bite attack."""
        return 'The vampire makes two attacks, only one of which can be a bite attack.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 8 (2d4 + 3) slashing damage. Instead of dealing damage, the vampire can grapple the target (escape DC 13)."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 8 (2d4 + 3) slashing damage. Instead of dealing damage, the vampire can grapple the target (escape DC 13).'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one willing creature, or a creature that is grappled by the vampire, incapacitated, or restrained. Hit: 6 (1d6 + 3) piercing damage plus 7 (2d6) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken, and the vampire regains hit points equal to that amount. The reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one willing creature, or a creature that is grappled by the vampire, incapacitated, or restrained. Hit: 6 (1d6 + 3) piercing damage plus 7 (2d6) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken, and the vampire regains hit points equal to that amount. The reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."

