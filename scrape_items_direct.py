#!/usr/bin/env python3
"""
Scraper simplificado que descarga items de https://5e.tools/data/items.json
"""

import argparse
import json
import requests
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional


@dataclass
class Item:
    """Clase para representar un item de D&D 5e"""
    name: str
    type: str  # 'mundane' o 'magic'
    source: str = ""
    rarity: str = ""
    value: str = ""
    weight: str = ""
    description: str = ""
    requires_attunement: bool = False
    properties: List[str] = None
    
    def __post_init__(self):
        if self.properties is None:
            self.properties = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el item a diccionario"""
        return asdict(self)
    
    def to_json(self) -> str:
        """Convierte el item a JSON"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


class ItemsScraper:
    """Scraper para descargar items de 5e.tools"""
    
    def __init__(self, force: bool=False, report: bool=False):
        self.items_data = None
        self.items = []
        self.existing_items = set()
        self.new_items = []
        self.force = force
        self.report = report

    def load_existing_items(self):
        """Carga los items ya guardados para evitar duplicados."""
        items_path = Path("items")

        if items_path.exists() and items_path.is_dir():
            for file_path in items_path.glob("*.json"):
                name = file_path.stem
                self.existing_items.add(name)

        print(f"✓ Items existentes cargados: {len(self.existing_items)}")
        
    def download_items_json(self) -> bool:
        """Descarga el JSON de items desde el mirror de GitHub"""
        print("🔗 Descargando items.json desde GitHub mirror...")
        
        urls = [
            "https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/refs/heads/main/data/foundry-items.json",
            "https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/refs/heads/main/data/fluff-items.json",
            "https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/refs/heads/main/data/items-base.json",
            "https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/refs/heads/main/data/fluff-items.json",
            "https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/refs/heads/main/data/items.json",
            "https://raw.githubusercontent.com/5etools-mirror-3/5etools-src/main/data/items.json",
            "https://raw.githubusercontent.com/Skiviper-AJM/5eTools-Mirror/main/data/items.json",
            "https://raw.githubusercontent.com/OTTOREIKU/5etools-Trevelyan/main/data/items.json"
        ]
        
        for url in urls:
            try:
                print(f"  Intentando: {url}")
                headers = {'User-Agent': 'Mozilla/5.0'}
                
                response = requests.get(url, headers=headers, timeout=30)
                
                if response.status_code == 200:
                    self.items_data = response.json()
                    print(f"✓ JSON descargado exitosamente ({len(response.text)} bytes)")
                    return True
                else:
                    print(f"  ❌ Error {response.status_code}")
            
            except requests.exceptions.RequestException as e:
                print(f"  ❌ Error: {e}")
        
        print("❌ No se pudo descargar desde ninguna URL")
        return False
    
    def extract_items(self):
        """Extrae y clasifica items"""
        if not self.items_data:
            print("❌ No hay datos para procesar")
            return
        
        print("\n" + "="*50)
        print("CLASIFICANDO ITEMS")
        print("="*50)
        
        total_items = 0
        
        # El JSON puede tener estructura item o items
        items_list = self.items_data.get('item', self.items_data.get('items', []))
        
        if not isinstance(items_list, list):
            items_list = [items_list] if items_list else []
        
        print(f"✓ Total de items a procesar: {len(items_list)}")
        
        for item_data in items_list:
            total_items += 1

            name = item_data.get('name', f'Unknown Item {total_items}')
            normalized_name = name.lower().replace(' ', '_').replace('/', '_').replace("'", "")

            if not self.force and normalized_name in self.existing_items:
                continue

            # Extrae información básica
            source = item_data.get('source', '')
            rarity = item_data.get('rarity', '')
            value = item_data.get('value', '')
            weight = item_data.get('weight', '')

            # Extrae descripción
            description = ""
            entries = item_data.get('entries', [])
            if isinstance(entries, list):
                description = "\n".join([
                    e if isinstance(e, str) else json.dumps(e)
                    for e in entries
                ])
            elif isinstance(entries, str):
                description = entries

            # Busca información de sintonización
            requires_attunement = bool(item_data.get('reqAttune'))

            # Extrae propiedades
            properties = item_data.get('property', [])
            if isinstance(properties, str):
                properties = [properties]

            # Crea objeto Item (tipo fijo "item")
            item = Item(
                name=name,
                type='item',
                source=source,
                rarity=rarity,
                value=value,
                weight=weight,
                description=description[:500],
                requires_attunement=requires_attunement,
                properties=properties
            )

            self.items.append(item)
            self.new_items.append(normalized_name)

            if total_items % 100 == 0:
                print(f"  Procesados: {total_items} items")
        
        print(f"✓ Clasificación completada")
        print(f"  └─ Items nuevos: {len(self.items)}")

        # Actualiza el set de existentes para evitar duplicates
        for item in self.items:
            key = item.name.lower().replace(' ', '_').replace('/', '_').replace("'", "")
            self.existing_items.add(key)

        if self.report:
            print("\nNUEVOS ITEMS AGREGADOS:")
            for name in self.new_items:
                print(f"  - {name}")
            print(f"✓ Total nuevos: {len(self.new_items)}")

    
    def save_items(self):
        """Guarda los items en archivos JSON"""
        print("\n" + "="*50)
        print("GUARDANDO ITEMS")
        print("="*50)

        items_path = Path("items")
        items_path.mkdir(parents=True, exist_ok=True)

        for item in self.items:
            filename = items_path / f"{item.name.lower().replace(' ', '_').replace('/', '_').replace("'", '')}.json"
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(item.to_json())
            except Exception as e:
                print(f"⚠️  Error guardando {item.name}: {e}")

        print(f"✓ Items guardados: {len(self.items)}")

        # Guarda resumen
        summary = {
            "total": len(self.items),
            "items": [item.to_dict() for item in self.items[:10]]
        }

        summary_path = Path("items") / "summary.json"
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print(f"✓ Resumen guardado en items/summary.json")
    
    def scrape(self) -> bool:
        """Función principal"""
        if not self.download_items_json():
            return False

        self.load_existing_items()
        self.extract_items()
        self.save_items()
        
        print("\n" + "="*50)
        print("✓ SCRAPING COMPLETADO")
        print("="*50)
        print(f"Total de items extraídos: {len(self.items)}")
        
        return True


def main():
    parser = argparse.ArgumentParser(description='Scraper de items D&D 5e desde mirror de 5e.tools')
    parser.add_argument('--force', action='store_true', help='Reescribir todos los items aunque ya existan')
    parser.add_argument('--report', action='store_true', help='Muestra la lista de nuevos items agregados')

    args = parser.parse_args()

    scraper = ItemsScraper(force=args.force, report=args.report)
    scraper.scrape()


if __name__ == "__main__":
    main()
