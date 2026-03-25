# bases1/steam-mephit.py
"""
SteamMephit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=steam-mephit
"""
from creature_base import GlobalCreatureBaseClass


class SteamMephit(GlobalCreatureBaseClass):
    """
    Small elemental creature - SteamMephit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 21, 'min_level': 1, 'level': 1, 'STR': 5, 'DEX': 11, 'CON': 10, 'INT': 11, 'WIS': 10, 'CHAR': 12, 'armor_class': 10, 'alignment': 'neutral evil Armor Class  10 Hit Points  21 (6d6) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_burst', 'claws', 'steam_breath_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_burst(self) -> str:
        """When the mephit dies, it explodes in a cloud of steam. Each creature within 5 feet of the mephit must succeed on a DC 10 Dexterity saving throw or take 4 (1d8) fire damage.Innate Spellcasting (1/Day)."""
        return 'When the mephit dies, it explodes in a cloud of steam. Each creature within 5 feet of the mephit must succeed on a DC 10 Dexterity saving throw or take 4 (1d8) fire damage.Innate Spellcasting (1/Day).'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 2 (1d4) slashing damage plus 2 (1d4) fire damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 2 (1d4) slashing damage plus 2 (1d4) fire damage.'

    def steam_breath_(recharge_6)_attack(self) -> str:
        """The mephit exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a DC 10 Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one."""
        return 'The mephit exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a DC 10 Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one.'

