import os
import time
import logging
from steam.client import SteamClient
from steam.enums import EResult

# Включаем полные логи самой библиотеки Steam, чтобы увидеть внутренние пакеты
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

STEAM_USERNAME = "sss102ax"
STEAM_PASSWORD = "loh_1111"
GAMES_TO_IDLE = [730] # CS2

def main():
    print("[System] Initializing Steam Client...")
    client = SteamClient()
    
    # Заставляем библиотеку прикидываться стандартным десктопным клиентом
    client.set_credential_location(".") 

    @client.on('logged_on')
    def handle_logged_on():
        print(f"[Success] Logged in successfully as {STEAM_USERNAME}!")
        client.games_played(GAMES_TO_IDLE)
        print("[Success] CS2 hours farming started!")
        time.sleep(1200) # Держим сессию 20 минут
        client.logout()

    @client.on('error')
    def handle_error(result):
        print(f"[Error] Connection failed with result code: {result} ({EResult(result).name})")

    print("[System] Attempting to establish connection to Steam CM...")
    
    # Пробуем подключиться напрямую
    result = client.login(username=STEAM_USERNAME, password=STEAM_PASSWORD)
    
    if result == EResult.OK:
        client.run_forever()
    else:
        print(f"[Error] Initial login result: {result} ({EResult(result).name})")

if __name__ == "__main__":
    main()
