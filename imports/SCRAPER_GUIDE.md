# AiDeDd Web Scraper - Scrapy Guide

## Overview

The `/imports` folder contains tools to scrape monster data from the AiDeDd D&D 5e database and automatically create new creature classes in the project.

**Data Source**: https://www.aidedd.org/dnd-filters/monsters.php

## Files

### `aidedd_scraper.py`
Web scraper that extracts monster stats from AiDeDd monster pages.

#### Main Functions:
- **`scrape_monster(monster_name: str)`** - Scrapes a single monster from the database
  - Returns dictionary with extracted stats
  - Example: `scrape_monster("badger")`

- **`extract_ability_scores(data: str)`** - Parses ability scores from raw text

#### Classes:
- **`MonsterHTMLParser`** - Custom HTML parser for extracting stat blocks
  - Handles extraction of name, type, size, AC, HP, abilities, etc.

## Usage Examples

### Scraping a New Monster

```python
from imports import scrape_monster

# Get monster data
data = scrape_monster("badger")
print(data)
# Output:
# {
#     'name': 'Badger',
#     'size': 'Tiny',
#     'type': 'Beast',
#     'armor_class': 10,
#     'hit_points': 3,
#     'hit_dice': '1d4+1',
#     'STR': 4,
#     'DEX': 11,
#     'CON': 12,
#     'INT': 2,
#     'WIS': 12,
#     'CHA': 5,
#     'challenge': {'rating': '0', 'xp': 10}
# }
```

### Creating a New Creature Class

1. Scrape the monster data:
```bash
python3 -c "from imports import scrape_monster; print(scrape_monster('badger'))"
```

2. Create a new Python file in `/bases1/` (e.g., `badger.py`):
```python
from creature_base import GlobalCreatureBaseClass

class Badger(GlobalCreatureBaseClass):
    """Creature scraped from AiDeDd"""
    
    DEFAULT_STATS = {
        "hit_points": 3,
        "min_level": 1,
        "level": 1,
        "STR": 4,
        "DEX": 11,
        "CON": 12,
        "INT": 2,
        "WIS": 12,
        "CHAR": 5,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Tiny",
        "type": "Beast",
        # See creature_base.py for validation rules
        "hit_points_up": [1, 1, 1],
        "min_level_up": [1, 0, 1],
        "STR_up": [0, 1, 0],
        "DEX_up": [0, 0, 1],
        "CON_up": [0, 1, 0],
        "INT_up": [1, 0, 0],
        "WIS_up": [0, 0, 0],
        "CHAR_up": [0, 0, 0],
        "abilities": [],
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add creature-specific abilities
        self.abilities.append("KeenSmell")
        self.abilities.append("Bite")
```

## Validation Rules

When creating DEFAULT_STATS, follow these rules:

### hit_points_up
- Each value must be between 1 and (10% of initial hit_points)
- For a creature with 3 HP: `10% of 3 = 0.3 → max 1`
- Each value must be 1

### Other _up fields (min_level_up, STR_up, etc.)
- Each value must be 0-2
- **Column sums must equal exactly 2**
  - Sum of min_level_up[0] + STR_up[0] + ... + CHAR_up[0] = 2
  - Sum of min_level_up[1] + STR_up[1] + ... + CHAR_up[1] = 2
  - And so on...

### Example (Badger with 3 HP):
```
hit_points_up: [1, 1, 1]
min_level_up: [1, 0, 1]   Sums: Col0=1+0+0+0+1+0+0=2 ✓
STR_up:       [0, 1, 0]           Col1=0+1+0+1+0+0+0=2 ✓
DEX_up:       [0, 0, 1]           Col2=1+0+1+0+0+0+0=2 ✓
CON_up:       [0, 1, 0]
INT_up:       [1, 0, 0]
WIS_up:       [0, 0, 0]
CHAR_up:      [0, 0, 0]
```

## Example: Badger

The example creature included in this release is the **Badger**:
- File: `/bases1/badger.py`
- Source: https://www.aidedd.org/dnd/monstres.php?vo=badger
- Stats extracted automatically from the webpage

Test it:
```python
from bases1.badger import Badger

badger = Badger(**Badger.DEFAULT_STATS)
print(f"Badger HP: {badger.hit_points}")
print(f"Badger Abilities: {badger.abilities}")
```

## Known Limitations

The current scraper focuses on:
- Basic stats (AC, HP, ability scores)
- Challenge rating
- Type and size
- Speed, senses, languages (partially working)

Future improvements could include:
- Better parsing of special abilities
- Skill proficiencies
- Damage resistances/immunities
- Action descriptions
- Legendary actions
- Multiattack handling

## Contributing

To add more creatures:
1. Scrape the monster from AiDeDd
2. Create a new class in `/bases1/`
3. Follow the DEFAULT_STATS template
4. Test with: `python3 -c "from bases1.creature_name import CreatureName; c = CreatureName(**CreatureName.DEFAULT_STATS); print(c)"`
