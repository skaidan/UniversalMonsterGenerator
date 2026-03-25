# bases1/guardian-naga.py
"""
GuardianNaga creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=guardian-naga
"""
from creature_base import GlobalCreatureBaseClass


class GuardianNaga(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - GuardianNaga
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 18, 'CON': 16, 'INT': 16, 'WIS': 19, 'CHAR': 18, 'armor_class': 18, 'alignment': 'lawful good Armor Class  18 (natural armor) Hit Points  127 (15d10 + 45) Speed  40 ft. STR 19 (+4) DEX 18 (+4) CON 16 (+3) INT 16 (+3) WIS 19 (+4) CHA 18 (+4) Saving Throws  Dex +8', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['rejuvenation', 'bite', 'spit_poison']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def rejuvenation(self) -> str:
        """If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.Spellcasting. The naga is an 11th-level spellcaster. Its spel"""
        return 'If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.Spellcasting. The naga is an 11th-level spellcaster. Its spel'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one creature. Hit: 8 (1d8 + 4) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one creature. Hit: 8 (1d8 + 4) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one.'

    def spit_poison_attack(self) -> str:
        """Ranged Weapon Attack: +8 to hit, range 15/30 ft., one creature. Hit: The target must make a DC 15 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Ranged Weapon Attack: +8 to hit, range 15/30 ft., one creature. Hit: The target must make a DC 15 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one.'

