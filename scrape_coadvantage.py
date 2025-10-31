import asyncio
import os
from dotenv import load_dotenv
from playwright.async_api import async_playwright

DOWNLOAD_PATH = "/app/downloads"
ENV_PATH = "/app/.env"

# Load environment variables
load_dotenv(ENV_PATH)
USERNAME = os.getenv("COADVANTAGE_USERNAME")
PASSWORD = os.getenv("COADVANTAGE_PASSWORD")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()
        
        print("Navigating to CoAdvantage portal...")
        await page.goto("https://portal.coadvantage.com")
        #TODO: check URL
        await page.fill("input[name='username']", USERNAME)
        #TODO: check input fields
        await page.click("text=Sign In")
        await page.screenshot(path=f"{DOWNLOAD_PATH}/coadvantage_home.png")
        print("Screenshot saved to:", f"{DOWNLOAD_PATH}/coadvantage_home.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())