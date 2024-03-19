import os
import time
import threading
import multiprocessing as mp
from collections import OrderedDict
from binance import ThreadedWebsocketManager, BinanceSocketManager

from typing import Dict

# install 'python-binance' library!
from binance import Client as BinanceClient
# install 'kucoin-python' library!
from kucoin.client import Client as KucoinClient
# install 'pybit' library!
from pybit.unified_trading import HTTP as BybitClient
# install 'coinbase' library!
from coinbase.wallet.client import Client as CoinbaseClient
# install 'okx-api' library!
import okx.PublicData as OkxPublicData
# install 'gate-api' library!
import gate_api.api as GateIOClient
# install 'mexc-api' library!
import mexc_client.client as MexcClient

class BotController:

    def __init__(self, symbol):

        self.symbol = symbol
        self.kucoin_key = 'XXX_KUCOIN_API_KEY_XXX'
        self.kucoin_sec = 'XXX_KUCOIN_API_SECRET_XXX'
        self.kucoin_passphrase = 'XXX_KUCOIN_PASSPHRASE_XXX'
        self.mexc_key = 'XXX_MEXC_API_KEY_XXX'
        self.mexc_sec = 'XXX_MEXC_API_SECRET_XXX'
        self.bybit_key = 'XXX_BYBIT_API_KEY_XXX'
        self.bybit_sec = 'XXX_BYBIT_API_SECRET_XXX'
        self.gateio_key = 'XXX_GATEIO_API_KEY_XXX'
        self.gateio_secret = 'XXX_GATEIO_API_SECRET_XXX'
        self.okx_key = 'XXX_OKX_API_KEY_XXX'
        self.okx_sec = 'XXX_OKX_API_SECRET_XXX'
        self.okx_passphrase = 'XXX_OKX_PASSPHRASE_XXX'
        self.cb_key_name = "XXX_COINBASE_API_KEY_NAME_XXX"
        self.cb_key_secret = "XXX_COINBASE_API_SECRET_XXX"
        self.gateio_client = GateIOClient.FuturesApi()
        self.mexc_client = MexcClient.mexc_futures()
        self.bybit_client = BybitClient(api_key=self.bybit_key, api_secret=self.bybit_sec, testnet=False)
        self.cb_client = CoinbaseClient(api_key=self.cb_key_name, api_secret=self.cb_key_secret)
        self.okx_public_client = OkxPublicData.PublicAPI(api_key=self.okx_key, api_secret_key=self.okx_sec, passphrase=self.okx_passphrase)
        self.kucoin_client = KucoinClient(self.kucoin_key, self.kucoin_sec, self.kucoin_passphrase)
        self.binance_client = BinanceClient()
        self.all_coins_dict = {}
        self.binance_ws = ThreadedWebsocketManager(
            api_key='XXX_BINANCE_API_KEY_XXX',
            api_secret='XXX_BINANCE_API_SECRET_XXX'
        )

    def start(self):

        s = '' if len(self.symbols) == 1 else 's'
        print(f'Launching bot controller on {len(self.symbols)} market{s}...')

        # EXAMPLE CLIENT CALL FOR ALL SYMBOLS THAT ARE TRADING ON BINANCE FUTURES AND ITS DATA!
        market_structures_binance = self.binance_client.futures_exchange_info()['symbols']

        # EXAMPLE CLIENT CALL FOR ALL SYMBOLS THAT ARE TRADING ON BINANCE FUTURES!
        symbols_from_binance = [entry['symbol'] for entry in market_structures_binance]



        # HERE IS AN EXAMPLE OF HOW TO CREATE A DICTIONARY THAT CONTAINS ALL THE TRADED SYMBOLS AND SPLIT IT BY THE DIFFERENT EXCHANGES!
        for coin in set(symbols_from_kucoin + symbols_from_binance + symbols_from_bybit + symbols_from_coinbase + symbols_from_mexc):
            exchanges_list = []
            if coin in symbols_from_kucoin:
                exchanges_list.append('kucoin')
            if coin in symbols_from_binance:
                exchanges_list.append('binance')
            if coin in symbols_from_bybit:
                exchanges_list.append('bybit')
            if coin in symbols_from_coinbase:
                exchanges_list.append('coinbase')
            if coin in symbols_from_okx:
                exchanges_list.append('okx')
            if coin in symbols_from_gateio:
                exchanges_list.append('gateio')
            if coin in symbols_from_mexc:
                exchanges_list.append('mexc')
            self.all_coins_dict[coin] = exchanges_list


            # THIS SHOWS US THE STRUCTURE OF ALL THE COINS WE ARE INTERESTED IN AND HAVE SPECIFIED IN MAIN!
            binance_structure = [mkt for mkt in market_structures_binance if mkt['symbol'].upper() == symbol]


        # HERE YOU CAN START DIFFERENT WEBSOCKETS CONTAINING ORDERBOOK DEPTH DATA!

        # BINANCE DEPTH SOCKET, SPECIFIY THE DEPTH!
        self.binance_ws.start_futures_depth_socket(callback=self.handle_binance_depth_data, symbol=self.symbol, depth=str(20))



        
    def handle_binance_depth_data(msg):
        print(msg)




