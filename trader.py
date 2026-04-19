from py_clob_client_v2.client import ClobClient

class PolyTrader:
    def __init__(self, private_key):
        host = "https://polymarket.com"
        self.client = ClobClient(host, chain_id=137, key=private_key)
        # Menyiapkan API Key otomatis
        self.client.set_api_creds(self.client.create_or_derive_api_key())

    def get_market_price(self, condition_id):
        # Logika untuk cek harga 'Yes' atau 'No' di Polymarket
        return self.client.get_orderbook(token_id=condition_id)

    def place_order(self, price, amount, side, token_id):
        # Logika eksekusi trade
        pass
