import os
import time
from dotenv import load_dotenv
from oracle import ChainlinkOracle
from trader import PolyTrader

load_dotenv()

def main():
    oracle = ChainlinkOracle(os.getenv("POLYGON_RPC"))
    trader = PolyTrader(os.getenv("PRIVATE_KEY"))

    print("Bot dimulali...")

    while True:
        try:
            # 1. Ambil harga asli dari Chainlink
            real_price = oracle.get_btc_price()
            print(f"Harga Chainlink BTC: ${real_price}")

            # 2. Logika Strategi (Contoh Sederhana)
            # Misal: Jika harga BTC > 70.000, cek market "BTC di atas 70k" di Polymarket
            # Jika harga 'Yes' masih murah, beli.
            
            # 3. Tunggu sebelum pengecekan berikutnya (misal 30 detik)
            time.sleep(30)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
