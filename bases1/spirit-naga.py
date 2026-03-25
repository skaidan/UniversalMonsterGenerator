# bases1/spirit-naga.py
"""
SpiritNaga creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spirit-naga
"""
from creature_base import GlobalCreatureBaseClass


class SpiritNaga(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - SpiritNaga
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 17, 'CON': 14, 'INT': 16, 'WIS': 15, 'CHAR': 16, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (natural armor) Hit Points  75 (10d10 + 20) Speed  40 ft. STR 18 (+4) DEX 17 (+3) CON 14 (+2) INT 16 (+3) WIS 15 (+2) CHA 16 (+3) Saving Throws  Dex +6', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['rejuvenation', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def rejuvenation(self) -> str:
        """If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.Spellcasting. The naga is a 10th-level spellcaster. Its spell"""
        return 'If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.Spellcasting. The naga is a 10th-level spellcaster. Its spell'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 7 (1d6 + 4) piercing damage, and the target must make a DC 13 Constitution saving throw, taking 31 (7d8) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 7 (1d6 + 4) piercing damage, and the target must make a DC 13 Constitution saving throw, taking 31 (7d8) poison damage on a failed save, or half as much damage on a successful one.'

