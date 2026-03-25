# bases1/alustriel-silverhand.py
"""
AlustrielSilverhand creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=alustriel-silverhand
"""
from creature_base import GlobalCreatureBaseClass


class AlustrielSilverhand(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Human creature - AlustrielSilverhand
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 272, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 20, 'CON': 18, 'INT': 24, 'WIS': 23, 'CHAR': 22, 'armor_class': 15, 'alignment': 'Wizard)', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Human', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['ear_of_the_chosen', 'multiattack', 'staff_of_silverymoon', 'reproving_ray', 'argent_blaze_(requires_silver_fire)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def ear_of_the_chosen(self) -> str:
        """Whenever a creature on the same plane of existence as Alustriel speaks Alustriel's name, Alustriel hearsher name and the next nine words the speaker utters.Legendary Resistance (3/Day). If Alustriel f"""
        return "Whenever a creature on the same plane of existence as Alustriel speaks Alustriel's name, Alustriel hearsher name and the next nine words the speaker utters.Legendary Resistance (3/Day). If Alustriel f"

    def multiattack_attack(self) -> str:
        """Alustriel makes three Staff of Silverymoon attacks or two Reproving Ray attacks."""
        return 'Alustriel makes three Staff of Silverymoon attacks or two Reproving Ray attacks.'

    def staff_of_silverymoon_attack(self) -> str:
        """Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage plus 38(7d10) radiant damage."""
        return 'Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage plus 38(7d10) radiant damage.'

    def reproving_ray_attack(self) -> str:
        """Ranged Spell Attack: +14 to hit, range 120 ft., one target. Hit: 65 (9d12 + 7) force damage, and if the target is a creature, it must make a DC 22 Charisma saving throw. On a failed save, the target has the incapacitated condition until the start of Alustriel's next turn. On a successful save, the target's speed is reduced by 10 feet until the start of Alustriel's next turn."""
        return "Ranged Spell Attack: +14 to hit, range 120 ft., one target. Hit: 65 (9d12 + 7) force damage, and if the target is a creature, it must make a DC 22 Charisma saving throw. On a failed save, the target has the incapacitated condition until the start of Alustriel's next turn. On a successful save, the target's speed is reduced by 10 feet until the start of Alustriel's next turn."

    def argent_blaze_(requires_silver_fire)_attack(self) -> str:
        """Alustriel summons a 60-foot cone of silver fire. Each creature in that area must make a DC 22 Dexterity saving throw, taking 77 (14d10) radiant damage on a failed save or half as much damage on a successful one. Additionally, Alustriel or one creature of her choice within 60 feet of her then regains 10 (3d6) hit points."""
        return 'Alustriel summons a 60-foot cone of silver fire. Each creature in that area must make a DC 22 Dexterity saving throw, taking 77 (14d10) radiant damage on a failed save or half as much damage on a successful one. Additionally, Alustriel or one creature of her choice within 60 feet of her then regains 10 (3d6) hit points.'

    def spellcasting_attack(self) -> str:
        """Alustriel casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 22):"""
        return 'Alustriel casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 22):'

