# bases1/marilith.py
"""
Marilith creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=marilith
"""
from creature_base import GlobalCreatureBaseClass


class Marilith(GlobalCreatureBaseClass):
    """
    Large fiend (Demon) creature - Marilith
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 20, 'CON': 20, 'INT': 18, 'WIS': 16, 'CHAR': 20, 'armor_class': 18, 'alignment': 'chaotic evil Armor Class  18 (natural armor) Hit Points  189 (18d10 + 90) Speed  40 ft. STR 18 (+4) DEX 20 (+5) CON 20 (+5) INT 18 (+4) WIS 16 (+3) CHA 20 (+5) Saving Throws  Str +9', 'legendary': False, 'size': 'Large', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'longsword', 'tail', 'teleport']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The marilith has advantage on saving throws against spells and other magical effects.Magic Weapons. The marilith's weapon attacks are magical.Reactive. The marilith can take one reaction on every turn"""
        return "The marilith has advantage on saving throws against spells and other magical effects.Magic Weapons. The marilith's weapon attacks are magical.Reactive. The marilith can take one reaction on every turn"

    def multiattack_attack(self) -> str:
        """The marilith makes seven attacks: six with its longswords and one with its tail."""
        return 'The marilith makes seven attacks: six with its longswords and one with its tail.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one creature. Hit: 15 (2d10 + 4) bludgeoning damage. If the target is Medium or smaller, it is grappled (escape DC 19). Until this grapple ends, the target is restrained, the marilith can automatically hit the target with its tail, and the marilith can't make tail attacks against other targets."""
        return "Melee Weapon Attack: +9 to hit, reach 10 ft., one creature. Hit: 15 (2d10 + 4) bludgeoning damage. If the target is Medium or smaller, it is grappled (escape DC 19). Until this grapple ends, the target is restrained, the marilith can automatically hit the target with its tail, and the marilith can't make tail attacks against other targets."

    def teleport_attack(self) -> str:
        """The marilith magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see."""
        return 'The marilith magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.'

