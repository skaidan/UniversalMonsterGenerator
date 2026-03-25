# bases1/juiblex.py
"""
Juiblex creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=juiblex
"""
from creature_base import GlobalCreatureBaseClass


class Juiblex(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - Juiblex
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 350, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 10, 'CON': 23, 'INT': 20, 'WIS': 20, 'CHAR': 16, 'armor_class': 18, 'alignment': 'Chaotic Evil Armor Class  18 (natural armor) Hit Points  350 (28d12 + 168) Speed  30 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['foul', 'multiattack', 'acid_lash', 'eject_slime_(recharge_5–6)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def foul(self) -> str:
        """Any creature other than an Ooze that starts its turn within 10 feet of Juiblex must succeed on a DC 21 Constitution saving throw or be poisoned until the start of the creature's next turn.Legendary Re"""
        return "Any creature other than an Ooze that starts its turn within 10 feet of Juiblex must succeed on a DC 21 Constitution saving throw or be poisoned until the start of the creature's next turn.Legendary Re"

    def multiattack_attack(self) -> str:
        """Juiblex makes three Acid Lash attacks."""
        return 'Juiblex makes three Acid Lash attacks.'

    def acid_lash_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +14 to hit, reach 10 ft. or range 60/120 ft., one target. Hit: 21 (4d6 + 7) acid damage. Any creature killed by this attack is drawn into Juiblex's body, where the corpse is dissolved after 1 minute."""
        return "Melee or Ranged Weapon Attack: +14 to hit, reach 10 ft. or range 60/120 ft., one target. Hit: 21 (4d6 + 7) acid damage. Any creature killed by this attack is drawn into Juiblex's body, where the corpse is dissolved after 1 minute."

    def eject_slime_(recharge_5–6)_attack(self) -> str:
        """Juiblex spews out a corrosive slime, targeting one creature that it can see within 60 feet of it. The target must succeed on a DC 21 Dexterity saving throw or take 55 (10d10) acid damage. Unless the target avoids taking all of this damage, any metal armor worn by the target takes a permanent −1 penalty to the AC it offers, and any metal weapon the target is carrying or wearing takes a permanent −1 penalty to damage rolls. The penalty worsens each time a target is subjected to this effect. If the penalty on an object drops to −5, the object is destroyed. The penalty on an object can be removed by the mending spell."""
        return 'Juiblex spews out a corrosive slime, targeting one creature that it can see within 60 feet of it. The target must succeed on a DC 21 Dexterity saving throw or take 55 (10d10) acid damage. Unless the target avoids taking all of this damage, any metal armor worn by the target takes a permanent −1 penalty to the AC it offers, and any metal weapon the target is carrying or wearing takes a permanent −1 penalty to damage rolls. The penalty worsens each time a target is subjected to this effect. If the penalty on an object drops to −5, the object is destroyed. The penalty on an object can be removed by the mending spell.'

    def spellcasting_attack(self) -> str:
        """Juiblex casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 20):"""
        return 'Juiblex casts one of the following spells, requiring no material components and using Wisdom as the spellcasting ability (spell save DC 20):'

