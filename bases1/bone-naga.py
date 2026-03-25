# bases1/bone-naga.py
"""
BoneNaga creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bone-naga
"""
from creature_base import GlobalCreatureBaseClass


class BoneNaga(GlobalCreatureBaseClass):
    """
    Large undead creature - BoneNaga
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 16, 'CON': 12, 'INT': 15, 'WIS': 15, 'CHAR': 16, 'armor_class': 15, 'alignment': 'lawful evil Armor Class  15 (natural armor) Hit Points  58 (9d10 + 9) Speed  30 ft. STR 15 (+2) DEX 16 (+3) CON 12 (+1) INT 15 (+2) WIS 15 (+2) CHA 16 (+3) Damage Immunities  poison Condition Immunities  charmed', 'legendary': False, 'size': 'Large', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['spellcasting', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def spellcasting(self) -> str:
        """The naga is a 5th-level spellcaster (spell save DC 12, +4 to hit with spell attacks) that needs only verbal components to cast its spells.If the naga was a guardian naga in life, its spellcasting abil"""
        return 'The naga is a 5th-level spellcaster (spell save DC 12, +4 to hit with spell attacks) that needs only verbal components to cast its spells.If the naga was a guardian naga in life, its spellcasting abil'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 10 ft., one creature. Hit: 10 (2d6 + 3) piercing damage plus 10 (3d6) poison damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 10 ft., one creature. Hit: 10 (2d6 + 3) piercing damage plus 10 (3d6) poison damage.'

