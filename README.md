# Webpage Print Bot

A Python bot to scrape links from a website, open them in Chrome, and automate printing (as PDF or to a printer).

## Features
- Scrapes webpage links with `BeautifulSoup`.
- Automates printing using `Selenium` and Chrome.
- Batch processing for multiple links.

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/softdev629/langchain-docsite2pdf.git
   cd langchain-docsite2pdf
   ```
2. Install dependencies:
3. Install Google Chrome & ChromeDriver.

## Usage
1. Update the `url` in `print-bot.py` with your target website.
2. Run the bot:
   ```bash
   python print-bot.py
   ```
3. PDFs will be saved in the specified directory.

## Dependencies
- `PyAutoGui` for automation.
- `BeautifulSoup` for scraping.
- `requests` for HTTP requests.

## Contributing
Feel free to fork, modify, and submit pull requests!

## License
MIT License
