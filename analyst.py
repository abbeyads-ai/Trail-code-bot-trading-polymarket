import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

class BrainAnalyst:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def analyze_trade(self, chainlink_price, polymarket_data):
        """
        chainlink_price: Harga BTC real-time
        polymarket_data: Info market (Pertanyaan, Harga YES, Harga NO)
        """
        
        prompt = f"""
        Anda adalah bot trading profesional. Analisis data berikut:
        1. Harga Real-time BTC (Chainlink): ${chainlink_price}
        2. Pertanyaan Market: "{polymarket_data['question']}"
        3. Harga 'YES' saat ini: ${polymarket_data['yes_price']}
        4. Harga 'NO' saat ini: ${polymarket_data['no_price']}

        Berikan keputusan trading. Jawab HANYA dengan format JSON:
        {{
            "decision": "BUY_YES" | "BUY_NO" | "HOLD",
            "reason": "Alasan singkat",
            "confidence_score": 0.0 - 1.0
        }}
        """

        response = self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Mengembalikan output dalam bentuk string/dict untuk diproses main.py
        return response.content[0].text
