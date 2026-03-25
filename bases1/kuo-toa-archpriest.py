# bases1/kuo-toa-archpriest.py
"""
KuoToaArchpriest creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kuo-toa-archpriest
"""
from creature_base import GlobalCreatureBaseClass


class KuoToaArchpriest(GlobalCreatureBaseClass):
    """
    Medium humanoid (Kuo-toa) creature - KuoToaArchpriest
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 97, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 16, 'INT': 13, 'WIS': 16, 'CHAR': 14, 'armor_class': 13, 'alignment': 'neutral evil Armor Class  13 (natural armor) Hit Points  97 (13d8 + 39) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Kuo-toa)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'scepter', 'unarmed_strike']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The kuo-toa can breathe air and water.Otherworldly Perception. The kuo-toa can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such """
        return 'The kuo-toa can breathe air and water.Otherworldly Perception. The kuo-toa can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such '

    def multiattack_attack(self) -> str:
        """The kuo-toa makes two melee attacks."""
        return 'The kuo-toa makes two melee attacks.'

    def scepter_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage plus 14 (4d6) lightning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage plus 14 (4d6) lightning damage.'

    def unarmed_strike_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage.'

