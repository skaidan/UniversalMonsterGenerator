# bases1/rust-monster.py
"""
RustMonster creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rust-monster
"""
from creature_base import GlobalCreatureBaseClass


class RustMonster(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - RustMonster
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 12, 'CON': 13, 'INT': 2, 'WIS': 13, 'CHAR': 6, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  27 (5d8 + 5) Speed  40 ft STR 13 (+1) DEX 12 (+1) CON 13 (+1) INT 2 (-4) WIS 13 (+1) CHA 6 (-2) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['iron_scent', 'bite', 'antennae']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def iron_scent(self) -> str:
        """The rust monster can pinpoint, by scent, the location of ferrous metal within 30 feet of it.Rust Metal. Any nonmagical weapon made of metal that hits the rust monster corrodes. After dealing damage, t"""
        return 'The rust monster can pinpoint, by scent, the location of ferrous metal within 30 feet of it.Rust Metal. Any nonmagical weapon made of metal that hits the rust monster corrodes. After dealing damage, t'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d8 + 1) piercing damage.'

    def antennae_attack(self) -> str:
        """The rust monster corrodes a nonmagical ferrous metal object it can see within 5 feet of it. If the object isn't being worn or carried, the touch destroys a 1-foot cube of it. If the object is being worn or carried by a creature, the creature can make a DC 11 Dexterity saving throw to avoid the rust monster's touch. If the object touched is either metal armor or a metal shield being worn or carried, its takes a permanent and cumulative -1 penalty to the AC it offers. Armor reduced to an AC of 10 or a shield that drops to a +0 bonus is destroyed. If the object touched is a held metal weapon, it rusts as described in the Rust Metal trait."""
        return "The rust monster corrodes a nonmagical ferrous metal object it can see within 5 feet of it. If the object isn't being worn or carried, the touch destroys a 1-foot cube of it. If the object is being worn or carried by a creature, the creature can make a DC 11 Dexterity saving throw to avoid the rust monster's touch. If the object touched is either metal armor or a metal shield being worn or carried, its takes a permanent and cumulative -1 penalty to the AC it offers. Armor reduced to an AC of 10 or a shield that drops to a +0 bonus is destroyed. If the object touched is a held metal weapon, it rusts as described in the Rust Metal trait."

