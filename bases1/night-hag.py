# bases1/night-hag.py
"""
NightHag creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=night-hag
"""
from creature_base import GlobalCreatureBaseClass


class NightHag(GlobalCreatureBaseClass):
    """
    Medium fiend creature - NightHag
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 112, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 16, 'WIS': 14, 'CHAR': 16, 'armor_class': 17, 'alignment': 'neutral evil Armor Class  17 (natural armor) Hit Points  112 (15d8 + 45) Speed  30 ft. STR 18 (+4) DEX 15 (+2) CON 16 (+3) INT 16 (+3) WIS 14 (+2) CHA 16 (+3) Skills  Deception +7', 'legendary': False, 'size': 'Medium', 'type': 'fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['innate_spellcasting', 'claws_(hag_form_only)', 'change_shape', 'etherealness', 'nightmare_haunting_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def innate_spellcasting(self) -> str:
        """The hag's innate spellcasting ability is Charisma (spell save DC 14, +6 to hit with spell attacks). She can innately cast the following spells, requiring no material components:At will: detect magic, """
        return "The hag's innate spellcasting ability is Charisma (spell save DC 14, +6 to hit with spell attacks). She can innately cast the following spells, requiring no material components:At will: detect magic, "

    def claws_(hag_form_only)_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage.'

    def change_shape_attack(self) -> str:
        """The hag magically polymorphs into a Small or Medium female humanoid, or back into her true form. Her statistics are the same in each form. Any equipment she is wearing or carrying isn't transformed. She reverts to her true form if she dies."""
        return "The hag magically polymorphs into a Small or Medium female humanoid, or back into her true form. Her statistics are the same in each form. Any equipment she is wearing or carrying isn't transformed. She reverts to her true form if she dies."

    def etherealness_attack(self) -> str:
        """The hag magically enters the Ethereal Plane from the Material Plane, or vice versa. To do so, the hag must have a heartstone in her possession."""
        return 'The hag magically enters the Ethereal Plane from the Material Plane, or vice versa. To do so, the hag must have a heartstone in her possession.'

    def nightmare_haunting_(1/day)_attack(self) -> str:
        """While on the Ethereal Plane, the hag magically touches a sleeping humanoid on the Material Plane. A protection from evil and good spell cast on the target prevents this contact, as does a magic circle. As long as the contact persists, the target has dreadful visions. If these visions last for at least 1 hour, the target gains no benefit from its rest, and its hit point maximum is reduced by 5 (1d10). If this effect reduces the target's hit point maximum to 0, the target dies, and if the target was evil, its soul is trapped in the hag's soul bag. The reduction to the target's hit point maximum lasts until removed by the greater restoration spell or similar magic."""
        return "While on the Ethereal Plane, the hag magically touches a sleeping humanoid on the Material Plane. A protection from evil and good spell cast on the target prevents this contact, as does a magic circle. As long as the contact persists, the target has dreadful visions. If these visions last for at least 1 hour, the target gains no benefit from its rest, and its hit point maximum is reduced by 5 (1d10). If this effect reduces the target's hit point maximum to 0, the target dies, and if the target was evil, its soul is trapped in the hag's soul bag. The reduction to the target's hit point maximum lasts until removed by the greater restoration spell or similar magic."

