# bases1/efreeti.py
"""
Efreeti creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=efreeti
"""
from creature_base import GlobalCreatureBaseClass


class Efreeti(GlobalCreatureBaseClass):
    """
    Large elemental creature - Efreeti
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 200, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 12, 'CON': 24, 'INT': 16, 'WIS': 15, 'CHAR': 16, 'armor_class': 17, 'alignment': 'lawful evil Armor Class  17 (natural armor) Hit Points  200 (16d10 + 112) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['elemental_demise', 'multiattack', 'scimitar', 'hurl_flame']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def elemental_demise(self) -> str:
        """If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind only equipment the efreeti was wearing or carrying.Innate Spellcasting. The efreeti's innate spellcasti"""
        return "If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind only equipment the efreeti was wearing or carrying.Innate Spellcasting. The efreeti's innate spellcasti"

    def multiattack_attack(self) -> str:
        """The efreeti makes two scimitar attacks or uses its Hurl Flame twice."""
        return 'The efreeti makes two scimitar attacks or uses its Hurl Flame twice.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage plus 7 (2d6) fire damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage plus 7 (2d6) fire damage.'

    def hurl_flame_attack(self) -> str:
        """Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 17 (5d6) fire damage."""
        return 'Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 17 (5d6) fire damage.'

