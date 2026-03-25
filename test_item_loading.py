#!/usr/bin/env python3
"""
Script para investigar cómo cargar los items dinámicamente
"""

import asyncio
from playwright.async_api import async_playwright


async def test_item_loading():
    """Prueba loading dinámico de items"""
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
            ]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
        )
        page = await context.new_page()
        
        print("🔗 Navegando a 5e.tools/items.html...")
        await page.goto("https://5e.tools/items.html", wait_until="domcontentloaded", timeout=60000)
        
        await page.wait_for_timeout(3000)
        
        print("\n" + "="*50)
        print("INTENTANDO CARGAR ITEMS MUNDANOS")
        print("="*50)
        
        # Busca y click en el label mundano
        mundane_label = await page.query_selector(".side-label.side-label--mundane")
        
        if mundane_label:
            print("✓ Label mundano encontrado")
            text = await mundane_label.text_content()
            print(f"  Texto: {text.strip()}")
            
            # Haz click
            await mundane_label.click()
            print("✓ Click en mundano")
            
            # Espera a que se carguen
            await page.wait_for_timeout(2000)
            
            # Busca items ahora
            mundane_list = await page.query_selector(".list.list--stats.mundane.ele-mundane")
            if mundane_list:
                html = await mundane_list.inner_html()
                print(f"✓ HTML en lista mundana: {len(html)} caracteres")
                
                # Intenta encontrar links
                links = await mundane_list.query_selector_all("a")
                print(f"✓ Links encontrados: {len(links)}")
                
                # Muestra los primeros
                for i, link in enumerate(links[:5], 1):
                    href = await link.get_attribute("href")
                    text = await link.text_content()
                    print(f"  {i}. {text.strip()} -> {href}")
        else:
            print("❌ Label mundano no encontrado")
        
        await page.wait_for_timeout(1000)
        
        print("\n" + "="*50)
        print("INTENTANDO CARGAR ITEMS MÁGICOS")
        print("="*50)
        
        # Busca y click en el label mágico
        magic_label = await page.query_selector(".side-label.side-label--magic")
        
        if magic_label:
            print("✓ Label mágico encontrado")
            text = await magic_label.text_content()
            print(f"  Texto: {text.strip()}")
            
            # Haz click
            await magic_label.click()
            print("✓ Click en mágico")
            
            # Espera a que se carguen
            await page.wait_for_timeout(2000)
            
            # Busca items ahora
            magic_list = await page.query_selector(".list.list--stats.magic.ele-magic")
            if magic_list:
                html = await magic_list.inner_html()
                print(f"✓ HTML en lista mágica: {len(html)} caracteres")
                
                # Intenta encontrar links
                links = await magic_list.query_selector_all("a")
                print(f"✓ Links encontrados: {len(links)}")
                
                # Muestra los primeros
                for i, link in enumerate(links[:5], 1):
                    href = await link.get_attribute("href")
                    text = await link.text_content()
                    print(f"  {i}. {text.strip()} -> {href}")
        else:
            print("❌ Label mágico no encontrado")
        
        # Guarda el HTML final
        html_final = await page.content()
        with open("items_page_after_clicks.html", "w", encoding="utf-8") as f:
            f.write(html_final)
        
        print("\n✓ HTML guardado en items_page_after_clicks.html")
        
        await browser.close()


if __name__ == "__main__":
    asyncio.run(test_item_loading())
