# bases1/lizardfolk-shaman.py
"""
LizardfolkShaman creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lizardfolk-shaman
"""
from creature_base import GlobalCreatureBaseClass


class LizardfolkShaman(GlobalCreatureBaseClass):
    """
    Medium humanoid (Lizardfolk) creature - LizardfolkShaman
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 13, 'INT': 10, 'WIS': 15, 'CHAR': 8, 'armor_class': 13, 'alignment': 'neutral Armor Class  13 (natural armor) Hit Points  27 (5d8 + 5) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Lizardfolk)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'multiattack_(lizardfolk_form_only)', 'bite', 'claws_(lizardfolk_form_only)', 'change_shape_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The lizardfolk can hold its breath for 15 minutes.Spellcasting (Lizardfolk Form Only). The lizardfolk is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with s"""
        return 'The lizardfolk can hold its breath for 15 minutes.Spellcasting (Lizardfolk Form Only). The lizardfolk is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with s'

    def multiattack_(lizardfolk_form_only)_attack(self) -> str:
        """The lizardfolk makes two attacks: one with its bite and one with its claws."""
        return 'The lizardfolk makes two attacks: one with its bite and one with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 7 (1d10 + 2) piercing damage in crocodile form. If the lizardfolk is in crocodile form and the target is a Large or smaller creature, the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the lizardfolk can't bite another target. If the lizardfolk reverts to its true form, the grapple ends."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 7 (1d10 + 2) piercing damage in crocodile form. If the lizardfolk is in crocodile form and the target is a Large or smaller creature, the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the lizardfolk can't bite another target. If the lizardfolk reverts to its true form, the grapple ends."

    def claws_(lizardfolk_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.'

    def change_shape_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """The lizardfolk magically polymorphs into a crocodile, remaining in that form for up to 1 hour. It can revert to its true form as a bonus action. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."""
        return "The lizardfolk magically polymorphs into a crocodile, remaining in that form for up to 1 hour. It can revert to its true form as a bonus action. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."

