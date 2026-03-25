# bases1/djinni.py
"""
Djinni creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=djinni
"""
from creature_base import GlobalCreatureBaseClass


class Djinni(GlobalCreatureBaseClass):
    """
    Large elemental creature - Djinni
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 161, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 15, 'CON': 22, 'INT': 15, 'WIS': 16, 'CHAR': 20, 'armor_class': 17, 'alignment': 'chaotic good Armor Class  17 (natural armor) Hit Points  161 (14d10 + 84) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['elemental_demise', 'multiattack', 'scimitar', 'create_whirlwind']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def elemental_demise(self) -> str:
        """If the djinni dies, its body disintegrates into a warm breeze, leaving behind only equipment the djinni was wearing or carrying.Innate Spellcasting. The djinni's innate spellcasting ability is Charism"""
        return "If the djinni dies, its body disintegrates into a warm breeze, leaving behind only equipment the djinni was wearing or carrying.Innate Spellcasting. The djinni's innate spellcasting ability is Charism"

    def multiattack_attack(self) -> str:
        """The djinni makes three scimitar attacks."""
        return 'The djinni makes three scimitar attacks.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage plus 3 (1d6) lightning or thunder damage (djinni's choice)."""
        return "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage plus 3 (1d6) lightning or thunder damage (djinni's choice)."

    def create_whirlwind_attack(self) -> str:
        """A 5-foot-radius, 30-foot-tall cylinder of swirling air magically forms on a point the djinni can see within 120 feet of it. The whirlwind lasts as long as the djinni maintains concentration (as if concentrating on a spell). Any creature but the djinni that enters the whirlwind must succeed on a DC 18 Strength saving throw or be restrained by it. The djinni can move the whirlwind up to 60 feet as an action, and creatures restrained by the whirlwind move with it. The whirlwind ends if the djinni loses sight of it. A creature can use its action to free a creature restrained by the whirlwind, including itself, by succeeding on a DC 18 Strength check. If the check succeeds, the creature is no longer restrained and moves to the nearest space outside the whirlwind."""
        return 'A 5-foot-radius, 30-foot-tall cylinder of swirling air magically forms on a point the djinni can see within 120 feet of it. The whirlwind lasts as long as the djinni maintains concentration (as if concentrating on a spell). Any creature but the djinni that enters the whirlwind must succeed on a DC 18 Strength saving throw or be restrained by it. The djinni can move the whirlwind up to 60 feet as an action, and creatures restrained by the whirlwind move with it. The whirlwind ends if the djinni loses sight of it. A creature can use its action to free a creature restrained by the whirlwind, including itself, by succeeding on a DC 18 Strength check. If the check succeeds, the creature is no longer restrained and moves to the nearest space outside the whirlwind.'

