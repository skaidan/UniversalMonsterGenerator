"""
imports package - Web scrapers for creature data sources
"""

from .aidedd_scraper import scrape_monster, MonsterHTMLParser

__all__ = ["scrape_monster", "MonsterHTMLParser"]
