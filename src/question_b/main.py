class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    apple = Stock("AAPL", "Apple Inc")
    caterpillar = Stock("CAT", "Caterpillar")
    kodak = Stock("EK", "Eastman Kodak")
    google = Stock("GOOG", "Google")
    microsoft = Stock("MSFT", "Microsoft")

    stocks = {
        apple.get_symbol(): apple,
        caterpillar.get_symbol(): caterpillar,
        kodak.get_symbol(): kodak,
        google.get_symbol(): google,
        microsoft.get_symbol(): microsoft
    }

    print("Symbol\tCompany Name")
    for symbol, stock in stocks.items():
        print(f"{stock.get_symbol()}\t{stock.get_company_name()}")
