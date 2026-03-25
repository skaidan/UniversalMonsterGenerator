# bases1/narzugon.py
"""
Narzugon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=narzugon
"""
from creature_base import GlobalCreatureBaseClass


class Narzugon(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - Narzugon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 112, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 10, 'CON': 17, 'INT': 16, 'WIS': 14, 'CHAR': 19, 'armor_class': 20, 'alignment': 'typically Lawful Evil Armor Class  20 (plate armor', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['infernal_tack', 'multiattack', 'hellfire_lance', 'infernal_command', 'terrifying_command', 'healing_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def infernal_tack(self) -> str:
        """The narzugon wears spurs that are part of infernal tack, which allow it to summon its nightmare companion as an action.Magic Resistance. The narzugon has advantage on saving throws against spells and """
        return 'The narzugon wears spurs that are part of infernal tack, which allow it to summon its nightmare companion as an action.Magic Resistance. The narzugon has advantage on saving throws against spells and '

    def multiattack_attack(self) -> str:
        """The narzugon makes three Hellfire Lance attacks. It also uses Infernal Command or Terrifying Command."""
        return 'The narzugon makes three Hellfire Lance attacks. It also uses Infernal Command or Terrifying Command.'

    def hellfire_lance_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 11 (1d12 + 5) piercing damage plus 16 (3d10) fire damage. If this damage kills a creature with a soul, the soul rises from the River Styx as a lemure in Avernus in 1d4 hours. If the creature isn't revived before then, only a wish spell or killing the lemure and casting true resurrection on the creature's original body can restore it to life. Constructs and devils are immune to this effect."""
        return "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 11 (1d12 + 5) piercing damage plus 16 (3d10) fire damage. If this damage kills a creature with a soul, the soul rises from the River Styx as a lemure in Avernus in 1d4 hours. If the creature isn't revived before then, only a wish spell or killing the lemure and casting true resurrection on the creature's original body can restore it to life. Constructs and devils are immune to this effect."

    def infernal_command_attack(self) -> str:
        """Each ally of the narzugon within 60 feet of it can't be charmed or frightened until the end of the narzugon's next turn."""
        return "Each ally of the narzugon within 60 feet of it can't be charmed or frightened until the end of the narzugon's next turn."

    def terrifying_command_attack(self) -> str:
        """Each creature within 60 feet of the narzugon that isn't a Fiend must succeed on a DC 17 Charisma saving throw or become frightened of the narzugon for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. A creature that makes a successful saving throw is immune to this narzugon's Terrifying Command for 24 hours."""
        return "Each creature within 60 feet of the narzugon that isn't a Fiend must succeed on a DC 17 Charisma saving throw or become frightened of the narzugon for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. A creature that makes a successful saving throw is immune to this narzugon's Terrifying Command for 24 hours."

    def healing_(1/day)_attack(self) -> str:
        """The narzugon, or one creature it touches, regains 100 hit points."""
        return 'The narzugon, or one creature it touches, regains 100 hit points.'

