
def maxgstcal(dict):
    maxgst=(dict[0][1]*dict[0][3])*(dict[0][2]/100)
    item=dict[0][0]
    for prod in dict:
        temp=(prod[1]*prod[3])*(prod[2]/100)
        if maxgst<temp:
            maxgst=temp
            item=prod[0]
    print("max GST is paid for the Product",item,":",maxgst)
    return 

def totalamount(dict):
    totamt=0
    for prod in dict:
        temp=prod[1]
        if prod[1]>=500:
            temp=temp-(temp*0.05)
        temp=(temp*prod[3])+(prod[1]*prod[3])*(prod[2]/100)
        totamt+=temp
    print("The amount to be paid to the shop_keeper:",totamt)
    return

dict=[["Leather Wallet",1100,18,1],["Umbrella",900,12,4],["Cigarette",200,28,3],["Honey",100,0,2]]
maxgstcal(dict)
totalamount(dict)