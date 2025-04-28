#convert BBG code (first 3 letters unless it's crosses or FTSE future) to IG epic
def ep(BBG_code):
    if BBG_code == "EUR":
        return "CS.D.EURUSD.TODAY.IP"
    if BBG_code == "JPY":
        return "CS.D.USDJPY.TODAY.IP"
    if BBG_code == "AUD":
        return "CS.D.AUDUSD.TODAY.IP"
    if BBG_code == "GBP":
        return "CS.D.GBPUSD.TODAY.IP"
    if BBG_code == "CAD":
        return "CS.D.USDCAD.TODAY.IP"
    if BBG_code == "NZD":
        return "CS.D.NZDUSD.TODAY.IP"
    if BBG_code == "AUDJPY":
        return "CS.D.AUDJPY.TODAY.IP"
    if BBG_code == "EURCHF":
        return "CS.D.EURCHF.TODAY.IP"
    if BBG_code == "EURGBP":
        return "CS.D.EURGBP.TODAY.IP"
    if BBG_code == "EURJPY":
        return "CS.D.EURJPY.TODAY.IP"
    if BBG_code == "GBPJPY":
        return "CS.D.GBPJPY.TODAY.IP"
    if BBG_code == "CHF":
        return "CS.D.USDCHF.TODAY.IP"
    if BBG_code == "XAU":
        return "CS.D.USCGC.TODAY.IP"
    if BBG_code == "XAG":
        return "CS.D.USCSI.TODAY.IP"
    if BBG_code == "CLA":
        return "CC.D.CL.USS.IP"
    if (BBG_code == "ESA") or (BBG_code == "SPX"):
        return "IX.D.SPTRD.DAILY.IP"
    if (BBG_code == "ESA_SG"):
        return "IX.D.SPTRD.FGM2.IP" #50 SGD per pts
    if (BBG_code == "SPX_SG"):
        return "IX.D.SPTRD.IFG.IP" #1 SGD per pts
    if (BBG_code == "NQA") or (BBG_code == "NDX"):
        return "IX.D.NASDAQ.CASH.IP"
    if (BBG_code == "DMA") or (BBG_code == "DJI"):
        return "IX.D.DOW.DAILY.IP"
    if (BBG_code == "RTYA") or (BBG_code == "RTY"):
        return "IX.D.RUSSELL.DAILY.IP"
    if (BBG_code == "GXA") or (BBG_code == "DAX"):
        return "IX.D.DAX.DAILY.IP"
    if (BBG_code == "Z A") or (BBG_code == "UKX"):
        return "IX.D.FTSE.DAILY.IP"
    if (BBG_code == "CFA") or (BBG_code == "CAC"):
        return "IX.D.CAC.DAILY.IP"
    if (BBG_code == "VGA") or (BBG_code == "SX5E"):
        return "IX.D.STXE.CASH.IP"
    if (BBG_code == "NKA") or (BBG_code == "NKY"):
        return "IX.D.NIKKEI.DAILY.IP"
    if (BBG_code == "XPA") or (BBG_code == "AS51"):
        return "IX.D.ASX.MONTH1.IP"
    if (BBG_code == "HIA") or (BBG_code == "HSI"):
        return "IX.D.HANGSENG.DAILY.IP"
    if (BBG_code == "WNA") or (BBG_code == "WN1"):
        return "IR.D.ULTRA100.Month1.IP"
    if (BBG_code == "XBT") or (BBG_code == "XBTUSD"):
        return "CS.D.BITCOIN.TODAY.IP"
    if (BBG_code == "XET") or (BBG_code == "XETUSD"):
        return "CS.D.ETHUSD.TODAY.IP"
    if (BBG_code == "XETXBT"):
        return "CS.D.ETHXBT.TODAY.IP"
    if (BBG_code == "JPY_SG"):
        return "CS.D.USDJPY.CSD.IP"
    if (BBG_code == "JPY_MINI_SG"):
        return "CS.D.USDJPY.CSM.IP"
    if (BBG_code == "EURJPY_MINI_SG"):
        return "CS.D.EURJPY.CSM.IP"
    if (BBG_code == "GBPJPY_MINI_SG"):
        return "CS.D.GBPJPY.CSM.IP"
    else:
        return "epic not found"

#Be extra careful with IG SG. this file got copied from IG UK app
#IG UK pricing convention, usually a multiple of BBG prices
#this list is still expanding
def IG_price_multiple(BBG_code):
    if BBG_code == "EUR Curncy":
        return 10000
    if BBG_code == "JPY Curncy":
        return 100
    if BBG_code == "AUD Curncy":
        return 10000
    if BBG_code == "GBP Curncy":
        return 10000
    if BBG_code == "CAD Curncy":
        return 10000
    if BBG_code == "NZD Curncy":
        return 10000
    if BBG_code == "AUDJPY Curncy":
        return 100
    if BBG_code == "EURCHF Curncy":
        return 10000
    if BBG_code == "EURGBP Curncy":
        return 10000
    if BBG_code == "EURJPY Curncy":
        return 100
    if BBG_code == "GBPJPY Curncy":
        return 100
    if BBG_code == "CHF Curncy":
        return 10000
    if BBG_code == "XAG Curncy":
        return 100
    if BBG_code == "CLA Comdty":
        return 100
    if (BBG_code == "WNA Comdty") or (BBG_code == "WN1 Comdty"):
        return 100
    else:
        return 1
    
#convert IG epic (UK or SG) to BBG code 
def BBG(epic):
    if epic == "CS.D.EURUSD.TODAY.IP":
        return "EUR Curncy"
    if epic == "CS.D.USDJPY.TODAY.IP":
        return "JPY Curncy"
    if epic == "CS.D.AUDUSD.TODAY.IP":
        return "AUD Curncy"
    if epic == "CS.D.GBPUSD.TODAY.IP":
        return "GBP Curncy"
    if epic == "CS.D.USDCAD.TODAY.IP":
        return "CAD Curncy"
    if epic == "CS.D.NZDUSD.TODAY.IP":
        return "NZD Curncy"
    if epic == "CS.D.AUDJPY.TODAY.IP":
        return "AUDJPY Curncy"
    if epic == "CS.D.EURCHF.TODAY.IP":
        return "EURCHF Curncy"
    if epic == "CS.D.EURGBP.TODAY.IP":
        return "EURGBP Curncy"
    if epic == "CS.D.EURJPY.TODAY.IP":
        return "EURJPY Curncy"
    if epic == "CS.D.GBPJPY.TODAY.IP":
        return "GBPJPY Curncy"
    if epic == "CS.D.USDCHF.TODAY.IP":
        return "CHF Curncy"
    if epic == "CS.D.USCGC.TODAY.IP":
        return "XAU Curncy"
    if epic == "CS.D.USCSI.TODAY.IP":
        return "XAG Curncy"
    if epic == "CC.D.CL.USS.IP":
        return "CLA Comdty"
    if (epic == "IX.D.SPTRD.MONTH1.IP") or (epic == "IX.D.SPTRD.MONTH2.IP") or (epic == "IX.D.SPTRD.MONTH3.IP") or (epic == "IX.D.SPTRD.MONTH4.IP"):
        return "ESA Index"
    if (epic == "IX.D.SPTRD.DAILY.IP"):
        return "SPX Index"
    if (epic == "IX.D.SPTRD.FGM2.IP"): #50 SGD per pts
        return "ESA Index"
    if (epic == "IX.D.SPTRD.IFG.IP"): #1 SGD per pts
        return "SPX Index" 
    if (epic == "IX.D.NASDAQ.CASH.IP"):
        return "NDX Index"
    if (epic == "IX.D.DOW.DAILY.IP"):
        return "DJI Index"
    if (epic == "IX.D.RUSSELL.DAILY.IP"):
        return "RTY Index"
    if (epic == "IX.D.DAX.DAILY.IP"):
        return "DAX Index"
    if (epic == "IX.D.FTSE.DAILY.IP"):
        return "UKX Index"
    if (epic == "IX.D.CAC.DAILY.IP"):
        return "CAC Index"
    if (epic == "IX.D.STXE.CASH.IP"):
        return "SX5E Index"
    if (epic == "IX.D.NIKKEI.DAILY.IP"):
        return "NKY Index"
    if (epic == "IX.D.ASX.MONTH1.IP"):
        return "XPA Index"
    if (epic == "IX.D.HANGSENG.DAILY.IP"):
        return "HSI Index"
    if (epic == "IR.D.ULTRA100.Month1.IP"):
        return "WNA Comdty"
    if (epic == "CS.D.BITCOIN.TODAY.IP"):
        return "XBT Curncy"
    if (epic == "CS.D.ETHUSD.TODAY.IP"):
        return "XET Curncy"
    if (epic == "CS.D.ETHXBT.TODAY.IP"):
        return "XETXBT Curncy"
    if (epic == "CS.D.USDJPY.CSD.IP"): #SG epic
        return "JPY Curncy"
    if (epic == "CS.D.USDJPY.CSM.IP"): #SG epic
        return "JPY Curncy"
    if (epic == "CS.D.EURJPY.CSM.IP"): #SG epic
        return "EURJPY Curncy"
    if (epic == "CS.D.GBPJPY.CSM.IP"): #SG epic
        return "GBPJPY Curncy"
    else:
        return "epic not found"
    
#convert OANDA code to BBG code (first 3 letters unless it's crosses or FTSE future)
def OANDA_to_BBG(OANDA_code):
    if OANDA_code == "AUD_CAD":
        return "AUDCAD"
    if OANDA_code == "AUD_JPY":
        return "AUDJPY"
    if OANDA_code == "AUD_NZD":
        return "AUDNZD"
    if OANDA_code == "AUD_USD":
        return "AUD"
    if OANDA_code == "AU200_AUD":
        return "XPA"
    if OANDA_code == "BCO_USD":
        return "COA"
    if OANDA_code == "CN50_USD":
        return "XUA"
    if OANDA_code == "XCU_USD":
        return "XCU"
    if OANDA_code == "EUR_AUD":
        return "EURAUD"
    if OANDA_code == "EUR_CAD":
        return "EURCAD"
    if OANDA_code == "EUR_CHF":
        return "EURCHF"
    if OANDA_code == "EUR_GBP":
        return "EURGBP"
    if OANDA_code == "EUR_JPY":
        return "EURJPY"
    if OANDA_code == "EUR_NOK":
        return "EURNOK"
    if OANDA_code == "EUR_USD":
        return "EUR"
    if OANDA_code == "EU50_EUR":
        return "VGA"
    if (OANDA_code == "FR40_EUR"):
        return "CFA"
    if (OANDA_code == "GBP_CHF"):
        return "GBPCHF"
    if (OANDA_code == "GBP_JPY"):
        return "GBPJPY" 
    if (OANDA_code == "GBP_NZD"):
        return "GBPNZD"
    if (OANDA_code == "GBP_USD"):
        return "GBP"
    if (OANDA_code == "DE30_EUR"):
        return "GXA"
    if (OANDA_code == "XAU_USD"):
        return "XAU"
    if (OANDA_code == "NATGAS_USD"):
        return "NGA"
    if (OANDA_code == "NL25_EUR"):
        return "AEX"
    if (OANDA_code == "NZD_USD"):
        return "NZD"
    if (OANDA_code == "SGD_JPY"):
        return "SGDJPY"
    if (OANDA_code == "XAG_USD"):
        return "XAG"
    if (OANDA_code == "SG30_SGD"):
        return "STI"
    if (OANDA_code == "UK100_GBP"):
        return "UKX"
    if (OANDA_code == "NAS100_100"):
        return "NQA"
    if (OANDA_code == "US2000_US"):
        return "RTY"
    if (OANDA_code == "SPX500_USD"):
        return "ESA"
    if (OANDA_code == "US30_USD"):
        return "DMA"
    if (OANDA_code == "USD_CAD"):
        return "CAD"
    if (OANDA_code == "USD_CHF"):
        return "CHF"
    if (OANDA_code == "USD_CNH"):
        return "CNH"
    if (OANDA_code == "USD_HKD"):
        return "HKD"
    if (OANDA_code == "USD_JPY"):
        return "JPY"
    if (OANDA_code == "USD_MXN"):
        return "MXN"
    if (OANDA_code == "USD_NOK"):
        return "NOK"
    if (OANDA_code == "JPY225Y_JPY"):
        return "NKA"
    if (OANDA_code == "USD_SGD"):
        return "SGD"
    if (OANDA_code == "USD_ZAR"):
        return "ZAR"
    if (OANDA_code == "WTICO_USD"):
        return "CLA"
    else:
        return "epic not found"