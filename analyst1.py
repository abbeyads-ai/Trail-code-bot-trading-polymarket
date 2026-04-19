def analyze_arbitrage(self, chainlink_price, market_data):
    prompt = f"""
    Tugas: Cari celah Arbitrase pada Polymarket berdasarkan harga Real-time.
    
    Data:
    - Target Harga Market: {market_data['target_boundary']}
    - Harga BTC Saat Ini (Chainlink): ${chainlink_price}
    - Harga Share 'YES' di Polymarket: {market_data['yes_price']}
    - Waktu Selesai Market: {market_data['time_remaining']}

    Instruksi:
    1. Jika Harga BTC > Target dan Harga YES < 0.90, ini adalah peluang BUY_YES (Undervalued).
    2. Jika Harga BTC < Target dan Harga NO < 0.90, ini adalah peluang BUY_NO (Undervalued).
    3. Hitung selisihnya (Potential Profit).

    Jawab dengan JSON:
    {{
        "decision": "BUY_YES/BUY_NO/HOLD",
        "potential_profit_percent": "xx%",
        "confidence": 0.0-1.0,
        "reason": "Penjelasan singkat"
    }}
    """
    # ... (kirim ke API Claude seperti kode sebelumnya)
