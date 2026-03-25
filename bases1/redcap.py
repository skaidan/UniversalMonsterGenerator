# bases1/redcap.py
"""
Redcap creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=redcap
"""
from creature_base import GlobalCreatureBaseClass


class Redcap(GlobalCreatureBaseClass):
    """
    Small Fey creature - Redcap
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 18, 'INT': 10, 'WIS': 12, 'CHAR': 9, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (natural armor) Hit Points  45 (6d6 + 24) Speed  25 ft. STR 18 (+4) DEX 13 (+1) CON 18 (+4) INT 10 (+0) WIS 12 (+1) CHA 9 (-1) Skills  Athletics +6', 'legendary': False, 'size': 'Small', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['iron_boots', 'multiattack', 'wicked_sickle', 'ironbound_pursuit']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def iron_boots(self) -> str:
        """The redcap has disadvantage on Dexterity (Stealth) checks.Outsize Strength. While grappling, the redcap is considered to be Medium. Also, wielding a heavy weapon doesn't impose disadvantage on its att"""
        return "The redcap has disadvantage on Dexterity (Stealth) checks.Outsize Strength. While grappling, the redcap is considered to be Medium. Also, wielding a heavy weapon doesn't impose disadvantage on its att"

    def multiattack_attack(self) -> str:
        """The redcap makes three Wicked Sickle attacks."""
        return 'The redcap makes three Wicked Sickle attacks.'

    def wicked_sickle_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) slashing damage.'

    def ironbound_pursuit_attack(self) -> str:
        """The redcap moves up to its speed to a creature it can see and kicks with its iron boots. The target must succeed on a DC 14 Dexterity saving throw or take 20 (3d10 + 4) bludgeoning damage and be knocked prone."""
        return 'The redcap moves up to its speed to a creature it can see and kicks with its iron boots. The target must succeed on a DC 14 Dexterity saving throw or take 20 (3d10 + 4) bludgeoning damage and be knocked prone.'

