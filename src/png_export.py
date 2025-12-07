"""
PNG Export functionality for the AI ROI Canvas using Selenium and Chrome.
This provides a reliable way to convert HTML to PNG without external dependencies.
"""

import io
import base64
from typing import Optional


def html_to_png(html_content: str) -> Optional[bytes]:
    """
    Convert HTML string to PNG bytes using Selenium and Chrome.
    Captures the full page height dynamically.
    
    Args:
        html_content: HTML string to convert
        
    Returns:
        PNG bytes if successful, None otherwise
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        import tempfile
        import os
        
        # Create Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--window-size=1400,1000")
        
        # Try to create driver
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except:
            # If Chrome driver not available, return None
            return None
        
        try:
            # Write HTML to temp file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
                f.write(html_content)
                temp_path = f.name
            
            # Load HTML in browser
            driver.get(f"file://{temp_path}")
            
            # Get full page dimensions
            total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
            total_width = driver.execute_script("return document.body.parentNode.scrollWidth")
            
            # Set window size to full page dimensions with some padding
            driver.set_window_size(total_width + 50, total_height + 100)
            
            # Wait a moment for rendering
            import time
            time.sleep(1)
            
            # Take screenshot of full page
            png_bytes = driver.get_screenshot_as_png()
            
            # Cleanup
            os.unlink(temp_path)
            
            return png_bytes
            
        finally:
            driver.quit()
            
    except Exception as e:
        # If Selenium not available or any error, return None
        return None


def html_to_png_pyppeteer(html_content: str) -> Optional[bytes]:
    """
    Alternative method using pyppeteer (async-based).
    Works with headless Chromium.
    """
    try:
        import asyncio
        from pyppeteer import launch
        import tempfile
        import os
        
        async def convert():
            browser = await launch(headless=True)
            page = await browser.newPage()
            await page.setViewport({'width': 1400, 'height': 1800})
            
            # Write HTML to temp file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
                f.write(html_content)
                temp_path = f.name
            
            await page.goto(f"file://{temp_path}")
            png_bytes = await page.screenshot()
            await browser.close()
            
            os.unlink(temp_path)
            return png_bytes
        
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(convert())
        return result
        
    except Exception as e:
        return None


def get_png_bytes(html_content: str) -> Optional[bytes]:
    """
    Try multiple methods to convert HTML to PNG.
    Returns PNG bytes or None if all methods fail.
    """
    # Try Selenium first
    result = html_to_png(html_content)
    if result:
        return result
    
    # Try pyppeteer as fallback
    result = html_to_png_pyppeteer(html_content)
    if result:
        return result
    
    return None
