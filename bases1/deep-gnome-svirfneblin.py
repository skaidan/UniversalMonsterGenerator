# bases1/deep-gnome-svirfneblin.py
"""
DeepGnomeSvirfneblin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deep-gnome-svirfneblin
"""
from creature_base import GlobalCreatureBaseClass


class DeepGnomeSvirfneblin(GlobalCreatureBaseClass):
    """
    Small humanoid (Gnome) creature - DeepGnomeSvirfneblin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 16, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 14, 'INT': 12, 'WIS': 10, 'CHAR': 9, 'armor_class': 15, 'alignment': 'neutral good Armor Class  15 (chain shirt) Hit Points  16 (3d6 + 6) Speed  20 ft. STR 15 (+2) DEX 14 (+2) CON 14 (+2) INT 12 (+1) WIS 10 (+0) CHA 9 (-1) Skills  Investigation +3', 'legendary': False, 'size': 'Small', 'type': 'humanoid (Gnome)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['stone_camouflage', 'war_pick', 'poisoned_dart']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def stone_camouflage(self) -> str:
        """The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.Gnome Cunning. The gnome has advantage on Intelligence, Wisdom, and Charisma saving throws against magic.Innate Spel"""
        return 'The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.Gnome Cunning. The gnome has advantage on Intelligence, Wisdom, and Charisma saving throws against magic.Innate Spel'

    def war_pick_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

    def poisoned_dart_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/120 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 12 Constitution saving throw or be poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/120 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 12 Constitution saving throw or be poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

