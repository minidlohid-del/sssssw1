import os
import time
import logging
from steam.client import SteamClient

# Включаем логи, чтобы видеть всё в панели GitHub Actions
logging.basicConfig(level=logging.INFO)

STEAM_USERNAME = "sss102ax"
STEAM_PASSWORD = "loh_1111"

# ID 730 — это строго CS2. Пока качаем только её.
GAMES_TO_IDLE = [730]

def main():
    print("[System] Connecting to Steam servers via GitHub Actions...")
    client = SteamClient()

    @client.on('logged_on')
    def handle_logged_on():
        print(f"[Success] Logged in as {STEAM_USERNAME}!")
        
        # Запускаем CS2
        print(f"[System] Sending request to play CS2...")
        client.games_played(GAMES_TO_IDLE)
        print("[Success] CS2 is active! Farming started.")
        
        # Скрипт будет держать игру запущенной 20 минут в рамках этого запуска
        print("[System] Keeping connection alive for 20 minutes...")
        time.sleep(1200) 
        
        print("[System] Session finished. Disconnecting gracefully...")
        client.logout()

    @client.on('error')
    def handle_error(result):
        print(f"[Error] Login failed: {result}")

    # Логинимся
    client.login(username=STEAM_USERNAME, password=STEAM_PASSWORD)
    
    # Даем скрипту поработать, пока не сработает logout() внутри события
    for _ in range(25):
        if not client.logged_on and _ > 0:
            break
        time.sleep(60)

if __name__ == "__main__":
    main()