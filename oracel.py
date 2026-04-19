from web3 import Web3

class ChainlinkOracle:
    def __init__(self, rpc_url):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        # Alamat BTC/USD Aggregator di Polygon
        self.address = "0xc907E11305CC23f932e139190740a1262d197395"
        self.abi = '[{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"}]'

    def get_btc_price(self):
        contract = self.w3.eth.contract(address=self.address, abi=self.abi)
        _, price, _, _, _ = contract.functions.latestRoundData().call()
        return price / 10**8
