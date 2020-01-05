

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum

class Testapp(Eclient,EWrapper):
    def __init__(self,self):
        EClient.__init__(self,self)
    def error(self, reqId, errorCode, errorString):
        print(reqId,"error")
    def tickPrice(self, reqId, tickType:, price,attrib):
        print(price)

def main():
    app=TestApp()
    app.connect("127.0.0.1",7497,0)

    contract= Contract()
    contract.symbol= "AAPL"
    contract.secType= "STK"
    contract.exchange="SMART"
    contract.currency= "USD"
    contract.primaryExchange="NASDAQ"
    app.reqMarketDataType(4)
    app.reqMktData(1, contract, "",False,False, [])
    app.run()

if __name__="__main__":
    main()