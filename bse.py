from bsedata.bse import BSE
import pandas as pd

b = BSE()
df = pd.read_csv(r'Equity.csv')

"""dic = b.getQuote('500128')
print(dic['pChange'])"""
def topgainers():
    topGainers = b.topGainers()
    msg = ""
    for i in topGainers:
        msg += i['securityID']+"    "+i["LTP"]+"     +"+ i["pChange"]+"%\n"
    return msg
def toplosers():
    topLosers = b.topLosers()
    msg = ""
    for i in topLosers:
        msg += i['securityID']+"    "+i["LTP"]+"     -"+ i["pChange"]+"%\n"
    return msg

def idtocode(id):
    code = None
    for i in range(len(df['Security Code'])):
        if df['Security Id'][i] == id:
            code = str(df['Security Code'][i])
    return code

def stockprice(c_name):
    try:
        c_name= c_name.upper()
        code = idtocode(c_name)
        dic = b.getQuote(code)
        ret = ""
        ret += "Company: "+str(dic['companyName'])+"\nCurrent Value: "+str(dic['currentValue'])+"\nChange: "+str(dic['pChange'])+"%"
        return ret
    except:
        return "invalid input"

def stockhistory(code,time):
    try:
        code = code.upper()
        his = b.getPeriodTrend(idtocode(code),time)
        his2 = ""
        for i in his:
            his2+= str((str(i['date'])[0:15])+"   :   "+str(i['value']))
            his2+= "\n"
        return his2
    except:
        return "invalid input"







        




            
