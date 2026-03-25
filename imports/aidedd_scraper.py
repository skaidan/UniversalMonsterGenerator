"""
AiDeDd Monster Web Scraper
Scrapes monster data from https://www.aidedd.org/dnd/monstres.php?vo=<monster_name>
"""

import re
import time
import pickle
import os
import logging
from typing import Optional, Dict, Any, List
from urllib.request import urlopen, Request
from html.parser import HTMLParser
from bs4 import BeautifulSoup

# Configuración externa
CONFIG = {
    "base_url": "https://www.aidedd.org/dnd/monstres.php?vo=",
    "timeout": 10,
    "delay": 1,  # Delay entre peticiones en segundos
    "cache_file": "monster_cache.pkl",
    "user_agent": "UniversalMonsterGenerator/1.0 (Ethical Scraper)",
}

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class MonsterHTMLParser(HTMLParser):
    """Custom HTML parser to extract monster stat blocks from AiDeDd pages"""
    
    def __init__(self):
        super().__init__()
        self.monster_data = {
            "name": None,
            "type": None,
            "size": None,
            "armor_class": None,
            "hit_points": None,
            "hit_dice": None,
            "speed": None,
            "STR": None,
            "DEX": None,
            "CON": None,
            "INT": None,
            "WIS": None,
            "CHA": None,
            "saving_throws": None,
            "skills": None,
            "damage_resistances": None,
            "damage_immunities": None,
            "condition_immunities": None,
            "senses": None,
            "languages": None,
            "challenge": None,
            "traits": [],  # Special abilities/traits
            "actions": [],  # Combat actions
            "legendary_actions": [],  # Legendary actions
            "lair_actions": [],  # Lair actions
            "regional_effects": [],  # Regional effects
            "description": None,  # Full description text
        }
        self.in_h1 = False
        
    def handle_starttag(self, tag: str, attrs: list):
        if tag == "h1":
            self.in_h1 = True
    
    def handle_endtag(self, tag: str):
        if tag == "h1":
            self.in_h1 = False
    
    def handle_data(self, data: str):
        if self.in_h1:
            self.monster_data["name"] = data.strip()
            self.in_h1 = False
    
    def parse_sansserif_text(self, text: str):
        """Parse the sansserif div text with regex for accurate extraction"""
        text = text.strip()
        
        # Size and Type: e.g., "Tiny beast, unaligned"
        size_type_match = re.search(r'(Tiny|Small|Medium|Large|Huge|Gargantuan)\s+([^,]+),\s*([^0-9]+)', text)
        if size_type_match:
            self.monster_data["size"] = size_type_match.group(1)
            self.monster_data["type"] = f"{size_type_match.group(2)}, {size_type_match.group(3).strip()}".strip()
        
        # Armor Class: "Armor Class 10"
        ac_match = re.search(r'Armor Class\s+(\d+)', text)
        if ac_match:
            self.monster_data["armor_class"] = int(ac_match.group(1))
        
        # Hit Points: "Hit Points 3 (1d4 + 1)"
        hp_match = re.search(r'Hit Points\s+(\d+)\s*\(([^)]+)\)', text)
        if hp_match:
            self.monster_data["hit_points"] = int(hp_match.group(1))
            self.monster_data["hit_dice"] = hp_match.group(2).replace(" ", "")
        
        # Speed: "Speed 20 ft."
        speed_match = re.search(r'Speed\s+([^<\n]+?)(?=\s*STR|\s*$)', text)
        if speed_match:
            self.monster_data["speed"] = speed_match.group(1).strip()
        
        # Ability Scores: "STR 4 (-3) DEX 11 (+0) CON 12 (+1) INT 2 (-4) WIS 12 (+1) CHA 5 (-3)"
        ability_matches = re.findall(r'(STR|DEX|CON|INT|WIS|CHA|CHAR)\s+(\d+)', text)
        for ability, score in ability_matches:
            if ability == "CHAR":
                ability = "CHA"
            self.monster_data[ability] = int(score)
        
        # Senses: "Senses darkvision 30 ft., passive Perception 11"
        senses_match = re.search(r'Senses\s+([^<\n]+?)(?=\s*Languages|\s*Challenge|\s*$)', text)
        if senses_match:
            self.monster_data["senses"] = senses_match.group(1).strip()
        
        # Saving Throws: "Saving Throws Str +3, Dex +4"
        saving_match = re.search(r'Saving Throws\s+([^<\n]+?)(?=\s*Skills|\s*Damage|\s*Senses|\s*$)', text)
        if saving_match:
            self.monster_data["saving_throws"] = saving_match.group(1).strip()
        
        # Skills: "Skills Perception +3, Stealth +4"
        skills_match = re.search(r'Skills\s+([^<\n]+?)(?=\s*Damage|\s*Senses|\s*Languages|\s*Challenge|\s*$)', text)
        if skills_match:
            self.monster_data["skills"] = skills_match.group(1).strip()
        
        # Damage Resistances: "Damage Resistances fire, cold"
        resistances_match = re.search(r'Damage Resistances\s+([^<\n]+?)(?=\s*Damage|\s*Senses|\s*$)', text)
        if resistances_match:
            self.monster_data["damage_resistances"] = resistances_match.group(1).strip()
        
        # Damage Immunities: "Damage Immunities poison"
        immunities_match = re.search(r'Damage Immunities\s+([^<\n]+?)(?=\s*Condition|\s*Senses|\s*$)', text)
        if immunities_match:
            self.monster_data["damage_immunities"] = immunities_match.group(1).strip()
        
        # Condition Immunities: "Condition Immunities charmed, frightened"
        condition_match = re.search(r'Condition Immunities\s+([^<\n]+?)(?=\s*Senses|\s*$)', text)
        if condition_match:
            self.monster_data["condition_immunities"] = condition_match.group(1).strip()


def extract_traits_from_html(html: str) -> List[Dict[str, str]]:
    """Extract trait/ability information from monster HTML
    
    Looks for patterns like:
    <strong><em>Trait Name</em></strong>. Description text here.
    Stops before the Actions section.
    """
    traits = []
    
    # Cut off at Actions section to avoid including actions in traits
    traits_html = re.split(r"<div[^>]*class=['\"]rub['\"]>\s*Actions\s*</div>", html, flags=re.IGNORECASE)[0]
    
    # Pattern: <strong><em>Name</em></strong>. Description
    pattern = r'<strong><em>([^<]+)</em></strong>\.\s*([^<]+(?:<[^>]*>[^<]*)*)'
    
    for match in re.finditer(pattern, traits_html):
        trait_name = match.group(1).strip()
        trait_desc = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        
        if trait_name and trait_desc:
            traits.append({
                'name': trait_name,
                'description': trait_desc[:200]  # Limit description length
            })
    
    return traits


def extract_actions_from_html(html: str) -> List[Dict[str, str]]:
    """Extract actions from monster HTML.

    The actions section appears after <div class='rub'>Actions</div>.
    """
    actions = []

    # Find the Actions section block
    parts = re.split(r"<div[^>]*class=['\"]rub['\"]>\s*Actions\s*</div>", html, flags=re.IGNORECASE)
    if len(parts) < 2:
        return actions

    action_html = parts[1]
    # Cut off before the next section (usually <div class='orange'> or another <div class='rub'>)
    action_html = re.split(r"<div[^>]*class=['\"]orange['\"]>|<div[^>]*class=['\"]rub['\"]>", action_html, flags=re.IGNORECASE)[0]

    # Find each action entry in <p><strong><em>ActionName</em></strong>. Description</p>
    action_pattern = r"<p>\s*<strong>(?:<em>)?([^<]+?)(?:</em>)?</strong>\.\s*(.*?)</p>"
    for match in re.finditer(action_pattern, action_html, flags=re.DOTALL | re.IGNORECASE):
        action_name = match.group(1).strip()
        action_desc = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        if action_name and action_desc:
            actions.append({
                'name': action_name,
                'description': action_desc
            })

    return actions


def extract_legendary_actions_from_html(html: str) -> List[Dict[str, str]]:
    """Extract legendary actions from monster HTML.

    The legendary actions section appears after <div class='rub'>Legendary Actions</div>.
    """
    legendary_actions = []

    # Find the Legendary Actions section block
    parts = re.split(r"<div[^>]*class=['\"]rub['\"]>\s*Legendary Actions\s*</div>", html, flags=re.IGNORECASE)
    if len(parts) < 2:
        return legendary_actions

    la_html = parts[1]
    # Cut off before the next section
    la_html = re.split(r"<div[^>]*class=['\"]orange['\"]>|<div[^>]*class=['\"]rub['\"]>", la_html, flags=re.IGNORECASE)[0]

    # Find each legendary action entry
    la_pattern = r"<p>\s*<strong>(?:<em>)?([^<]+?)(?:</em>)?</strong>\.\s*(.*?)</p>"
    for match in re.finditer(la_pattern, la_html, flags=re.DOTALL | re.IGNORECASE):
        la_name = match.group(1).strip()
        la_desc = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        if la_name and la_desc:
            legendary_actions.append({
                'name': la_name,
                'description': la_desc
            })

    return legendary_actions


def extract_lair_actions_from_html(html: str) -> List[Dict[str, str]]:
    """Extract lair actions from monster HTML.

    The lair actions section appears after <div class='rub'>Lair Actions</div>.
    """
    lair_actions = []

    # Find the Lair Actions section block
    parts = re.split(r"<div[^>]*class=['\"]rub['\"]>\s*Lair Actions\s*</div>", html, flags=re.IGNORECASE)
    if len(parts) < 2:
        return lair_actions

    lair_html = parts[1]
    # Cut off before the next section
    lair_html = re.split(r"<div[^>]*class=['\"]orange['\"]>|<div[^>]*class=['\"]rub['\"]>", lair_html, flags=re.IGNORECASE)[0]

    # Find each lair action entry
    lair_pattern = r"<p>\s*(.*?)</p>"
    for match in re.finditer(lair_pattern, lair_html, flags=re.DOTALL | re.IGNORECASE):
        lair_desc = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        if lair_desc:
            lair_actions.append({
                'description': lair_desc
            })

    return lair_actions


def extract_regional_effects_from_html(html: str) -> List[Dict[str, str]]:
    """Extract regional effects from monster HTML.

    The regional effects section appears after <div class='rub'>Regional Effects</div>.
    """
    regional_effects = []

    # Find the Regional Effects section block
    parts = re.split(r"<div[^>]*class=['\"]rub['\"]>\s*Regional Effects\s*</div>", html, flags=re.IGNORECASE)
    if len(parts) < 2:
        return regional_effects

    re_html = parts[1]
    # Cut off before the next section
    re_html = re.split(r"<div[^>]*class=['\"]orange['\"]>|<div[^>]*class=['\"]rub['\"]>", re_html, flags=re.IGNORECASE)[0]

    # Find each regional effect entry
    re_pattern = r"<p>\s*(.*?)</p>"
    for match in re.finditer(re_pattern, re_html, flags=re.DOTALL | re.IGNORECASE):
        re_desc = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        if re_desc:
            regional_effects.append({
                'description': re_desc
            })

    return regional_effects
    """
    Scrape a monster from AiDeDd.
    
    Args:
        monster_name: The monster name (e.g., "badger")
        use_cache: Whether to use cached results if available
    
    Returns:
        Dictionary with monster data or None if scraping fails
    """
    start_time = time.time()  # Start timing for metrics
    cache = {}
    if use_cache and os.path.exists(CONFIG["cache_file"]):
        try:
            with open(CONFIG["cache_file"], "rb") as f:
                cache = pickle.load(f)
        except Exception as e:
            logging.warning(f"Could not load cache: {e}")
    
    # Verificar si ya está en caché
    if use_cache and monster_name in cache:
        logging.info(f"Using cached data for '{monster_name}'")
        return cache[monster_name]
    
    url = CONFIG["base_url"] + monster_name.lower()
    
    try:
        # Rate limiting
        time.sleep(CONFIG["delay"])
        
        # User-Agent
        req = Request(url, headers={'User-Agent': CONFIG["user_agent"]})
        with urlopen(req, timeout=CONFIG["timeout"]) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
        
        soup = BeautifulSoup(html_content, 'html.parser')
        parser = MonsterHTMLParser()
        
        # Extraer nombre del h1
        h1 = soup.find('h1')
        if h1:
            parser.monster_data["name"] = h1.get_text().strip()
        
        # Extraer sansSerif div para stats
        sansserif_div = soup.find('div', class_='sansSerif')
        if sansserif_div:
            sansserif_text = sansserif_div.get_text(separator=' ').strip()
            parser.parse_sansserif_text(sansserif_text)
        
        # Extraer descripción completa (ej. párrafos principales)
        description_div = soup.find('div', class_='description')  # Ajustar clase si es necesario
        if description_div:
            parser.monster_data["description"] = description_div.get_text().strip()
        
        # Extraer traits y actions
        traits = extract_traits_from_html(html_content)
        if traits:
            parser.monster_data['traits'] = traits
        
        actions = extract_actions_from_html(html_content)
        if actions:
            parser.monster_data['actions'] = actions

        # Extraer legendary actions, lair actions, regional effects
        legendary_actions = extract_legendary_actions_from_html(html_content)
        if legendary_actions:
            parser.monster_data['legendary_actions'] = legendary_actions

        lair_actions = extract_lair_actions_from_html(html_content)
        if lair_actions:
            parser.monster_data['lair_actions'] = lair_actions

        regional_effects = extract_regional_effects_from_html(html_content)
        if regional_effects:
            parser.monster_data['regional_effects'] = regional_effects

        # Limpiar datos
        result = {k: v for k, v in parser.monster_data.items() if v is not None and v != []}
        
        if result.get("name"):
            # Guardar en caché
            cache[monster_name] = result
            try:
                with open(CONFIG["cache_file"], "wb") as f:
                    pickle.dump(cache, f)
            except Exception as e:
                logging.warning(f"Could not save cache: {e}")
            
            logging.info(f"Successfully scraped '{monster_name}' in {time.time() - start_time:.2f}s")
            return result
        else:
            logging.warning(f"Could not extract monster data for '{monster_name}' (time: {time.time() - start_time:.2f}s)")
            return None

    except Exception as e:
        logging.error(f"Error scraping '{monster_name}' in {time.time() - start_time:.2f}s: {e}")
        return None


def clear_cache():
    """Clear the monster cache file"""
    if os.path.exists(CONFIG["cache_file"]):
        os.remove(CONFIG["cache_file"])
        logging.info("Cache cleared")


def get_cache_stats():
    """Get statistics about the cache"""
    if os.path.exists(CONFIG["cache_file"]):
        try:
            with open(CONFIG["cache_file"], "rb") as f:
                cache = pickle.load(f)
            total = len(cache)
            # Calcular métricas básicas (puedes expandir con más datos si guardas tiempos)
            return {
                "total_monsters": total,
                "cache_file": CONFIG["cache_file"],
                "cache_size_mb": os.path.getsize(CONFIG["cache_file"]) / (1024 * 1024)
            }
        except Exception as e:
            logging.error(f"Could not read cache stats: {e}")
            return None
    return {"total_monsters": 0, "cache_file": CONFIG["cache_file"], "cache_size_mb": 0}


# Ejemplo de test simple
if __name__ == "__main__":
    # Test con badger
    data = scrape_monster("badger")
    if data:
        print("Scraped data keys:", list(data.keys()))
        print("Challenge:", data.get("challenge"))
        print("Saving Throws:", data.get("saving_throws"))
        print("Skills:", data.get("skills"))
    else:
        print("Failed to scrape badger")


def extract_ability_scores(data: str) -> Dict[str, int]:
    """Extract ability scores from raw text"""
    scores = {}
    pattern = r"(STR|DEX|CON|INT|WIS|CHA|CHAR)\s+(\d+)"
    
    for match in re.finditer(pattern, data):
        ability = match.group(1)
        if ability == "CHAR":
            ability = "CHA"
        scores[ability] = int(match.group(2))
    
    return scores


if __name__ == "__main__":
    # Test the scraper
    data = scrape_monster("badger")
    if data:
        print("✓ Successfully scraped badger data:")
        for key, value in data.items():
            print(f"  {key}: {value}")
    else:
        print("✗ Failed to scrape badger data")
