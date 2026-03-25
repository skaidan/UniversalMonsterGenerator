# bases1/annis-hag.py
"""
AnnisHag creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=annis-hag
"""
from creature_base import GlobalCreatureBaseClass


class AnnisHag(GlobalCreatureBaseClass):
    """
    Large Fey creature - AnnisHag
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 90, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 12, 'CON': 14, 'INT': 13, 'WIS': 14, 'CHAR': 15, 'armor_class': 17, 'alignment': 'typically Chaotic Evil Armor Class  17 (natural armor) Hit Points  90 (12d10 + 24) Speed  40 ft. STR 21 (+5) DEX 12 (+1) CON 14 (+2) INT 13 (+1) WIS 14 (+2) CHA 15 (+2) Saving Throws  Con +5 Skills  Deception +5', 'legendary': False, 'size': 'Large', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'claw', 'crushing_hug', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The annis makes one Bite attack and two Claw attacks."""
        return 'The annis makes one Bite attack and two Claw attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (3d6 + 5) piercing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (3d6 + 5) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (3d6 + 5) slashing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (3d6 + 5) slashing damage.'

    def crushing_hug_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 36 (9d6 + 5) bludgeoning damage, and the target is grappled (escape DC 15) if it is a Large or smaller creature. Until the grapple ends, the target takes 36 (9d6 + 5) bludgeoning damage at the start of each of the hag's turns. The hag can't make attacks while grappling a creature in this way."""
        return "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 36 (9d6 + 5) bludgeoning damage, and the target is grappled (escape DC 15) if it is a Large or smaller creature. Until the grapple ends, the target takes 36 (9d6 + 5) bludgeoning damage at the start of each of the hag's turns. The hag can't make attacks while grappling a creature in this way."

    def spellcasting_attack(self) -> str:
        """The hag casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 13):"""
        return 'The hag casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 13):'

