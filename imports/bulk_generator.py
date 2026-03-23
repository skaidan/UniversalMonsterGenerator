#!/usr/bin/env python3
"""
Bulk Monster Generator
Scrapes all monsters from AiDeDd and creates creature classes in bases1/
"""

import os
import sys
import re
import time
from urllib.request import urlopen
from html.parser import HTMLParser
from typing import List, Dict, Set
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from imports.aidedd_scraper import scrape_monster


def get_all_monster_names() -> Set[str]:
    """Extract all monster names from the monsters filter page"""
    url = "https://www.aidedd.org/dnd-filters/monsters.php"
    
    print("[1/3] Fetching monster list from AiDeDd...")
    try:
        with urlopen(url, timeout=30) as response:
            html = response.read().decode('utf-8', errors='ignore')
        
        # Extract all monster links: monstres.php?vo=monster-name
        pattern = r'monstres\.php\?vo=([^"&\s]+)'
        matches = re.findall(pattern, html)
        
        # Remove duplicates and sort
        monsters = sorted(set(matches))
        print(f"✓ Found {len(monsters)} unique monsters")
        return monsters
    
    except Exception as e:
        print(f"✗ Error fetching monster list: {e}")
        return set()


def normalize_class_name(monster_name: str) -> str:
    """Convert monster name to valid Python class name
    
    Examples:
        'badger' -> 'Badger'
        'adult-blue-dragon' -> 'AdultBlueDragon'
        'air-elemental' -> 'AirElemental'
    """
    parts = monster_name.split('-')
    return ''.join(word.capitalize() for word in parts)


def generate_creature_class(monster_name: str, monster_data: Dict) -> str:
    """Generate Python code for a creature class"""
    
    class_name = normalize_class_name(monster_name)
    
    # Extract data with safe defaults
    hit_points = monster_data.get('hit_points', 10)
    armor_class = monster_data.get('armor_class', 10)
    size = monster_data.get('size', 'Medium')
    creature_type = monster_data.get('type', 'Beast')
    alignment = monster_data.get('alignment', 'Unaligned')
    
    str_score = monster_data.get('STR', 10)
    dex_score = monster_data.get('DEX', 10)
    con_score = monster_data.get('CON', 10)
    int_score = monster_data.get('INT', 10)
    wis_score = monster_data.get('WIS', 10)
    cha_score = monster_data.get('CHA', 10)
    
    # Calculate min_level based on challenge rating
    challenge = monster_data.get('challenge', {}).get('rating', '0')
    challenge_num = float(challenge.split('/')[0]) if isinstance(challenge, str) else challenge
    min_level = max(1, int(challenge_num) + 1)
    
    # Calculate hit_points_up (max of 1, or 10% of HP)
    hp_up_max = max(1, int(hit_points * 0.1))
    
    # Create _up arrays that guarantee column sums = 2
    # Using a simple pattern that works for any creature
    hit_points_up = [hp_up_max] * 3
    
    # Distribute ability increases in a round-robin pattern
    # Pattern: STR, DEX, CON, INT, WIS (cycle through them)
    ability_scores = {
        'STR': str_score,
        'DEX': dex_score,
        'CON': con_score,
        'INT': int_score,
        'WIS': wis_score,
        'CHA': cha_score
    }
    
    # Sort by score (highest first) to prioritize high abilities
    sorted_abilities = sorted(ability_scores.items(), key=lambda x: -x[1])
    
    # Create base arrays (all zeros)
    str_up = [0, 0, 0]
    dex_up = [0, 0, 0]
    con_up = [0, 0, 0]
    int_up = [0, 0, 0]
    wis_up = [0, 0, 0]
    cha_up = [0, 0, 0]
    
    ability_arrays = {
        'STR': str_up,
        'DEX': dex_up,
        'CON': con_up,
        'INT': int_up,
        'WIS': wis_up,
        'CHA': cha_up
    }
    
    # Fill columns to sum = 2
    # Col 0: top 2 abilities get +1
    # Col 1: middle 2 abilities get +1  
    # Col 2: bottom 2 abilities get +1
    col_0_abilities = sorted_abilities[0:2]
    col_1_abilities = sorted_abilities[2:4]
    col_2_abilities = sorted_abilities[4:6]
    
    for ability_name, _ in col_0_abilities:
        ability_arrays[ability_name][0] += 1
    
    for ability_name, _ in col_1_abilities:
        ability_arrays[ability_name][1] += 1
    
    for ability_name, _ in col_2_abilities:
        ability_arrays[ability_name][2] += 1
    
    code = f'''# bases1/{monster_name}.py
"""
{class_name} creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo={monster_name}
"""
from creature_base import GlobalCreatureBaseClass


class {class_name}(GlobalCreatureBaseClass):
    """
    {class_name} creature
    Size: {size}, Type: {creature_type}
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {{
        "hit_points": {hit_points},
        "min_level": {min_level},
        "level": {min_level},
        "STR": {str_score},
        "DEX": {dex_score},
        "CON": {con_score},
        "INT": {int_score},
        "WIS": {wis_score},
        "CHAR": {cha_score},
        "armor_class": {armor_class},
        "alignment": "{alignment}",
        "legendary": False,
        "size": "{size}",
        "type": "{creature_type}",
        "hit_points_up": {hit_points_up},
        "STR_up": {str_up},
        "DEX_up": {dex_up},
        "CON_up": {con_up},
        "INT_up": {int_up},
        "WIS_up": {wis_up},
        "CHAR_up": {cha_up},
        "abilities": [],
    }}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Add creature-specific abilities here if needed
        pass
'''
    
    return code


def main():
    print("="*70)
    print("BULK MONSTER GENERATOR - AiDeDd to Python Classes")
    print("="*70)
    
    # Get all monster names
    monsters = get_all_monster_names()
    if not monsters:
        print("✗ Could not retrieve monster list")
        return
    
    # Create output directory
    bases1_dir = Path(__file__).parent.parent / "bases1"
    bases1_dir.mkdir(exist_ok=True)
    
    print(f"\n[2/3] Scraping and generating classes...")
    
    successful = 0
    failed = 0
    skipped = 0
    
    # Skip badger as it already exists
    existing_monsters = {p.stem for p in bases1_dir.glob("*.py") if p.name not in ["__init__.py"]}
    
    for i, monster_name in enumerate(monsters, 1):
        class_name = normalize_class_name(monster_name)
        class_file = bases1_dir / f"{monster_name}.py"
        
        # Skip if already exists
        if monster_name in existing_monsters:
            print(f"  [{i:3d}/{len(monsters)}] SKIPPED: {class_name} (already exists)")
            skipped += 1
            continue
        
        try:
            # Scrape monster data
            monster_data = scrape_monster(monster_name)
            
            if monster_data:
                # Generate code
                code = generate_creature_class(monster_name, monster_data)
                
                # Write file
                with open(class_file, 'w') as f:
                    f.write(code)
                
                print(f"  [{i:3d}/{len(monsters)}] ✓ {class_name} ({monster_data.get('hit_points', '?')} HP)")
                successful += 1
                
                # Rate limiting
                time.sleep(0.5)
            else:
                print(f"  [{i:3d}/{len(monsters)}] ✗ {class_name} (scrape failed)")
                failed += 1
        
        except Exception as e:
            print(f"  [{i:3d}/{len(monsters)}] ✗ {class_name} ({str(e)[:40]})")
            failed += 1
            time.sleep(0.5)
    
    print(f"\n[3/3] Summary")
    print("-"*70)
    print(f"  ✓ Created:  {successful}")
    print(f"  ✗ Failed:   {failed}")
    print(f"  ⊘ Skipped:  {skipped}")
    print(f"  Total:      {len(monsters)}")
    print("\nClasses generated in: bases1/")


if __name__ == "__main__":
    main()
