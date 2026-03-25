import pytest
import os
import tempfile
from unittest.mock import patch, mock_open, MagicMock
from imports.aidedd_scraper import (
    scrape_monster, clear_cache, get_cache_stats, CONFIG,
    extract_traits_from_html, extract_actions_from_html,
    extract_legendary_actions_from_html, extract_lair_actions_from_html,
    extract_regional_effects_from_html
)


class TestAideddScraper:
    """Test suite for aidedd_scraper.py"""

    def test_scrape_monster_success(self):
        """Test successful scraping of a monster"""
        # Mock the urlopen and response
        mock_response = MagicMock()
        mock_response.read.return_value = b'<html><head><title>Test</title></head><body><h1>Badger</h1><div class="sansSerif">Armor Class 10 Hit Points 3 (1d4 + 1) Speed 20 ft. STR 4 DEX 11 CON 12 INT 2 WIS 12 CHA 5 Challenge 0</div></body></html>'
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None

        with patch('imports.aidedd_scraper.urlopen', return_value=mock_response):
            with patch('imports.aidedd_scraper.time.sleep'):  # Skip delay
                result = scrape_monster('badger', use_cache=False)

        assert result is not None
        assert result['name'] == 'Badger'
        assert result['armor_class'] == 10
        assert result['hit_points'] == 3
        assert result['challenge'] == '0'

    def test_scrape_monster_cache_hit(self):
        """Test using cached data"""
        # Create a temporary cache file
        cache_data = {'badger': {'name': 'Badger', 'armor_class': 10}}
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            import pickle
            pickle.dump(cache_data, temp_file)
            temp_file_path = temp_file.name

        # Mock CONFIG to use temp file
        with patch('imports.aidedd_scraper.CONFIG', {**CONFIG, 'cache_file': temp_file_path}):
            result = scrape_monster('badger', use_cache=True)

        assert result == cache_data['badger']

        # Clean up
        os.unlink(temp_file_path)

    def test_scrape_monster_failure(self):
        """Test scraping failure"""
        with patch('imports.aidedd_scraper.urlopen', side_effect=Exception('Network error')):
            with patch('imports.aidedd_scraper.time.sleep'):
                result = scrape_monster('nonexistent', use_cache=False)

        assert result is None

    def test_clear_cache(self):
        """Test clearing the cache"""
        # Create a temporary cache file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b'test')
            temp_file_path = temp_file.name

        with patch('imports.aidedd_scraper.CONFIG', {**CONFIG, 'cache_file': temp_file_path}):
            clear_cache()

        assert not os.path.exists(temp_file_path)

    def test_get_cache_stats(self):
        """Test getting cache statistics"""
        # Create a temporary cache file
        cache_data = {'monster1': {}, 'monster2': {}}
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            import pickle
            pickle.dump(cache_data, temp_file)
            temp_file_path = temp_file.name

        with patch('imports.aidedd_scraper.CONFIG', {**CONFIG, 'cache_file': temp_file_path}):
            stats = get_cache_stats()

        assert stats['total_monsters'] == 2
        assert 'cache_size_mb' in stats

        # Clean up
        os.unlink(temp_file_path)

    def test_extract_traits_from_html(self):
        """Test extracting traits from HTML"""
        html = '''
        <div class="rub">Actions</div>
        <strong><em>Pack Tactics</em></strong>. Description here.
        <strong><em>Keen Smell</em></strong>. Another description.
        '''
        traits = extract_traits_from_html(html)
        assert len(traits) == 2
        assert traits[0]['name'] == 'Pack Tactics'
        assert traits[1]['name'] == 'Keen Smell'

    def test_extract_actions_from_html(self):
        """Test extracting actions from HTML"""
        html = '''
        <div class="rub">Actions</div>
        <p><strong>Bite</strong>. Bite attack description.</p>
        <p><strong>Claw</strong>. Claw attack description.</p>
        <div class="orange">
        '''
        actions = extract_actions_from_html(html)
        assert len(actions) == 2
        assert actions[0]['name'] == 'Bite'
        assert actions[1]['name'] == 'Claw'

    def test_extract_legendary_actions_from_html(self):
        """Test extracting legendary actions from HTML"""
        html = '''
        <div class="rub">Legendary Actions</div>
        <p><strong>Cast Spell</strong>. Cast spell description.</p>
        <p><strong>Move</strong>. Move description.</p>
        '''
        la = extract_legendary_actions_from_html(html)
        assert len(la) == 2
        assert la[0]['name'] == 'Cast Spell'

    def test_extract_lair_actions_from_html(self):
        """Test extracting lair actions from HTML"""
        html = '''
        <div class="rub">Lair Actions</div>
        <p>When fighting inside its lair, the dragon can take lair actions.</p>
        <p>Description of lair action.</p>
        '''
        lair = extract_lair_actions_from_html(html)
        assert len(lair) == 2
        assert 'lair actions' in lair[0]['description'].lower()

    def test_extract_regional_effects_from_html(self):
        """Test extracting regional effects from HTML"""
        html = '''
        <div class="rub">Regional Effects</div>
        <p>The region is affected by the dragon's presence.</p>
        <p>Description of regional effect.</p>
        '''
        re = extract_regional_effects_from_html(html)
        assert len(re) == 2
        assert 'region' in re[0]['description'].lower()


if __name__ == "__main__":
    pytest.main([__file__])