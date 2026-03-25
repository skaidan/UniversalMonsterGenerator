# bases1/neogi-master.py
"""
NeogiMaster creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=neogi-master
"""
from creature_base import GlobalCreatureBaseClass


class NeogiMaster(GlobalCreatureBaseClass):
    """
    Medium Aberration (Warlock) creature - NeogiMaster
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 71, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 16, 'CON': 14, 'INT': 16, 'WIS': 12, 'CHAR': 18, 'armor_class': 15, 'alignment': 'typically Lawful Evil Armor Class  15 (natural armor) Hit Points  71 (11d8 + 22) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Aberration (Warlock)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'bite', 'claw', 'tentacle_of_hadar', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the neogi's darkvision.Mental Fortitude. The neogi has advantage on saving throws against being charmed or frightened, and magic can't put the neogi to sleep.Spider Cli"""
        return "Magical darkness doesn't impede the neogi's darkvision.Mental Fortitude. The neogi has advantage on saving throws against being charmed or frightened, and magic can't put the neogi to sleep.Spider Cli"

    def multiattack_attack(self) -> str:
        """The neogi makes one Bite attack and one Claw attack, or it makes two Tentacle of Hadar attacks."""
        return 'The neogi makes one Bite attack and one Claw attack, or it makes two Tentacle of Hadar attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 14 (4d6) poison damage, and the target must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage plus 14 (4d6) poison damage, and the target must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) piercing damage.'

    def tentacle_of_hadar_attack(self) -> str:
        """Ranged Spell Attack: +6 to hit, range 120 ft., one target. Hit: 14 (3d6 + 4) necrotic damage, and the target can't take reactions until the end of the neogi's next turn, as a spectral tentacle clings to the target."""
        return "Ranged Spell Attack: +6 to hit, range 120 ft., one target. Hit: 14 (3d6 + 4) necrotic damage, and the target can't take reactions until the end of the neogi's next turn, as a spectral tentacle clings to the target."

    def spellcasting_attack(self) -> str:
        """The neogi casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 14):"""
        return 'The neogi casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 14):'

