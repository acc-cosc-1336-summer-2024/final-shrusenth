class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


stock1 = Stock("AAPL", "Apple Inc.")
stock2 = Stock("CAT", "Caterpillar Inc.")
stock3 = Stock("EK", "Eastman Kodak")
stock4 = Stock("GOOG", "Google Inc.")
stock5 = Stock("MSFT", "Microsoft Inc.")

stocks = {
    stock1.get_symbol(): stock1,
    stock2.get_symbol(): stock2,
    stock3.get_symbol(): stock3,
    stock4.get_symbol(): stock4,
    stock5.get_symbol(): stock5
}
