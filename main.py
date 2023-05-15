from colorama import Fore, Style
from tradingview_ta import TA_Handler, Interval, get_multiple_analysis
import tradingview_ta, requests, argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--proxy", help="Use HTTP proxy")
arg_parser.add_argument("--secureproxy", help="Use HTTPS proxy")

args = arg_parser.parse_args()
proxies = {}
if args.proxy:
    proxies["http"] = args.proxy
if args.secureproxy:
    proxies["https"] = args.secureproxy

class CryptoTrading:
    def __init__(
            self,
            symbol: str = "BTCUSDT",
            exchange: str = "BINANCE",
            interval: str = Interval.INTERVAL_1_DAY
    ) -> None:
        self.symbol = symbol
        self.exchange = exchange
        self.interval = interval
        self.handler = TA_Handler(
            symbol=symbol,
            interval=interval,
            screener="crypto",
            exchange=exchange,
            proxies=proxies
        )
    def get_hist(self):
        print(
            "{}#!{} Please compare with {}https://www.tradingview.com/symbols/{}:{}/technicals/{}. (Check for indicators)".format(
                Fore.BLUE, Style.RESET_ALL, Fore.LIGHTMAGENTA_EX, self.symbol, self.exchange, Style.RESET_ALL))
        return self.handler.get_indicators()


if __name__ == "__main__":
    binance = CryptoTrading("BTCUSDT", "BINANCE", )
    print("{}#1{} {}".format(Fore.BLUE, Style.RESET_ALL, binance.get_hist()))
    binance = CryptoTrading("XBTUSD", "BITMEX", )
    print("{}#2{} {}".format(Fore.BLUE, Style.RESET_ALL, binance.get_hist()))