# bases1/firenewt-warlock-of-imix.py
"""
FirenewtWarlockOfImix creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=firenewt-warlock-of-imix
"""
from creature_base import GlobalCreatureBaseClass


class FirenewtWarlockOfImix(GlobalCreatureBaseClass):
    """
    Medium Elemental creature - FirenewtWarlockOfImix
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 11, 'CON': 12, 'INT': 9, 'WIS': 11, 'CHAR': 14, 'armor_class': 10, 'alignment': 'typically Neutral Evil Armor Class  10 Hit Points  33 (6d8 + 6) Speed  30 ft. STR 13 (+1) DEX 11 (+0) CON 12 (+1) INT 9 (-1) WIS 11 (+0) CHA 14 (+2) Damage Immunities  fire Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'morningstar', 'fire_ray', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The firenewt can breathe air and water.Devil's Sight. Magical darkness doesn't impede the firenewt's darkvision.Imix's Blessing. When the firenewt reduces an enemy to 0 hit points, the firenewt gains """
        return "The firenewt can breathe air and water.Devil's Sight. Magical darkness doesn't impede the firenewt's darkvision.Imix's Blessing. When the firenewt reduces an enemy to 0 hit points, the firenewt gains "

    def multiattack_attack(self) -> str:
        """The firenewt makes three Morningstar or Fire Ray attacks."""
        return 'The firenewt makes three Morningstar or Fire Ray attacks.'

    def morningstar_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage.'

    def fire_ray_attack(self) -> str:
        """Ranged Spell Attack: +4 to hit, range 120 ft., one target. Hit: 5 (1d6 + 2) fire damage."""
        return 'Ranged Spell Attack: +4 to hit, range 120 ft., one target. Hit: 5 (1d6 + 2) fire damage.'

    def spellcasting_attack(self) -> str:
        """The firenewt casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 12):"""
        return 'The firenewt casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 12):'

