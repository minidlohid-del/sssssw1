import os
import time
import logging
from steam.client import SteamClient
from steam.enums import EResult

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

STEAM_USERNAME = "sss102ax"
STEAM_PASSWORD = "loh_1111"
GAMES_TO_IDLE = [730] # CS2

def main():
    print("[System] Connecting to Steam...")
    client = SteamClient()
    client.set_credential_location(".") 

    @client.on('logged_on')
    def handle_logged_on():
        print(f"[Success] Logged in as {STEAM_USERNAME}!")
        
        # Запускаем цикл на 20 минут, который каждые 30 секунд включает CS2 заново
        print("[System] Starting loop to force CS2 status...")
        for minute in range(40): # 40 раз по 30 секунд = 20 минут
            if not client.logged_on:
                print("[Warning] Disconnected from Steam inside loop.")
                break
            
            # Жёстко пинаем Стим, чтобы игра не вылетала
            client.games_played(GAMES_TO_IDLE)
            time.sleep(30)
            
        print("[System] 20 minutes finished. Logging out...")
        client.logout()

    @client.on('error')
    def handle_error(result):
        print(f"[Error] Connection failed: {result}")

    result = client.login(username=STEAM_USERNAME, password=STEAM_PASSWORD)
    if result == EResult.OK:
        client.run_forever()

if __name__ == "__main__":
    main()
