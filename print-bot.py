import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import pyautogui
import pyperclip
import os


def python_langchain():
    url = 'https://js.langchain.com/docs/'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    urls = []
    cnt = 0
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is None:
            continue
        if href.startswith("/") and href != "/":
            if not href in urls:
                print(href)
                urls.append(href)
                pyperclip.copy(f"{cnt}.pdf")
                webbrowser.get(chrome_path).open(f"{url}{href}")
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'p')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'w')
                cnt += 1


cnt = 0


def visit_dir(directory):
    global cnt
    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.exists(f"D:/resource/avatars/{cnt}.pdf"):
                cnt += 1
                continue
            url = str(os.path.join(root, file))
            url = url.replace("index.mdx", "").replace("index.md", "").replace(
                ".mdx", "").replace(".md", "").replace("\\", "/").replace("docs/", "")
            url = "https://js.langchain.com/docs/" + url
            pyperclip.copy(f"{cnt}.pdf")
            webbrowser.get(
                'C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
            time.sleep(10)
            pyautogui.hotkey('ctrl', 'p')
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
            cnt += 1


def js_langchain():
    visit_dir("docs")


js_langchain()
