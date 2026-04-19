import requests

def get_active_btc_markets():
    # Filter market BTC yang aktif dan belum selesai
    url = "https://polymarket.com"
    response = requests.get(url)
    markets = response.json()
    
    for m in markets:
        print(f"Market: {m['question']}")
        print(f"Condition ID: {m['conditionId']}")
        # Token ID: [0] biasanya YES, [1] biasanya NO
        print(f"Token IDs: {m['clobTokenIds']}") 
        print("-" * 30)

# Jalankan ini untuk mendapatkan ID yang akan dimasukkan ke bot
get_active_btc_markets()
