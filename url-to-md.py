import asyncio
import os
from crawl4ai import AsyncWebCrawler
from crawl4ai import BrowserConfig, CrawlerRunConfig

async def main():
    # 1. Set up configuration objects (optional if you want defaults)
    browser_config = BrowserConfig(
        browser_type="chromium",
        headless=True,
        verbose=True
    )
    crawler_config = CrawlerRunConfig(
        page_timeout=30000,     # 30 seconds
        wait_for_images=True,
        verbose=True
    )

    # 2. Initialize AsyncWebCrawler with your chosen browser config
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # 3. Run a single crawl
        url_to_crawl = "https://langchain-ai.github.io/langgraph/how-tos/"
        result = await crawler.arun(url=url_to_crawl, config=crawler_config)
        
        # 4. Process and save the result
        if result.success:
            print(f"Successfully crawled: {result.url}")
            
            # Create output path in current directory
            output_path = os.path.join(os.getcwd(), "output.md")
            
            # Write markdown content to output.md
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result.markdown)
                
            print(f"Markdown content saved to: {output_path}")
        else:
            print(f"Failed to crawl {result.url}. Error: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(main())