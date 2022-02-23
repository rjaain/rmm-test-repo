##################################################
# data simulator: this project aims to create 
# data for realistic testing of pulsops testing #
# authors: rahul jain & nitin "tintin" garg
#############################################################################################################
#AIM:  simulatio  and testing of product. So we want to emulate different scenarios                         #
# Product should be able to handle                                                                          #
# Current State: I edit start and end dates and I generate on flat file which is imported to db             #
# Future State: We should be able to scheudle it to run every day to generate and insert data for that day  #
#############################################################################################################
import random
import datetime

def generate_cols(dtnm,cust_id_start,cust_id_end,basket_num):
    """
    this function will generate a basket
    args:
    dtnm - date passed in postgres format eg. '1989-05-23'
    """
    orderbasketid = int(dtnm.replace('-',''))*10000+ basket_num 
    itemcount = random.randrange(1,10)
    businesstypeid = 2
    random_time  = random.randrange(481,1365)
    datecreated	= dtnm + " {:02d}:{:02d}:00".format(int(random_time/60),random_time%60)
    countryid = 1
    customerid = random.randrange(cust_id_start,cust_id_end)
    if customerid%2 :
        cityid	=100
        merchantid = random.randrange(1,20)
    else :
        cityid = 101
        merchantid=random.randrange(21,40)
    orderzoneid	='' #plan is to first assign customers a zone and then use that to populate the field
    orderzonelat=''
    orderzonelong=''
    merchantzoneid='' #will be same as user's merchantid
    merchantzonelat=''
    merchantzonelong=''
    ordervalue=random.randrange(10,100) #this will come later when we have generated item data
    platformdeliveryfee=random.randrange(1,5) #fixing it for now for simplicity
    promo_percent = random.randrange(1,5)
    promo_percent_arr = [0,5,10,15,20]
    if promo_percent == 1:
        merchantpromocode=''
        merchantpromo=0
    else:
        merchantpromocode="Promo - {} % OFF".format(promo_percent_arr[promo_percent-1]) #keeping it blank for now
        merchantpromo=promo_percent_arr[promo_percent-1]
    promo_percent = random.randrange(1,5)
    if promo_percent == 1:
        platformpromocode=''
        platformpromo=0
    else:
        platformpromocode="Promo - {} % OFF".format(promo_percent_arr[promo_percent-1]) #keeping it blank for now
        platformpromo=promo_percent_arr[promo_percent-1]
    tax=round(0.05*ordervalue,2) #this will be generated at 5% of order value
    netpaidbycustomer=round(ordervalue - (merchantpromo*ordervalue)/100 -  (platformpromo*ordervalue)/100,2)
    orderplacedtime= datecreated
    ordercurrency=1
    random_time = random_time + 1
    orderacceptedtime= dtnm + " {:02d}:{:02d}:00".format(int(random_time/60),random_time%60)
    riderassignedtime= dtnm + " {:02d}:{:02d}:50".format(int(random_time/60),random_time%60)
    riderid= 1000*cityid + random.randrange(1,999)
    random_time = random_time + random.randrange(10,30)
    rideronwaytime= dtnm + " {:02d}:{:02d}:00".format(int(random_time/60),random_time%60)
    random_time = random_time + random.randrange(10,40)
    orderdeliveredtime= dtnm + " {:02d}:{:02d}:00".format(int(random_time/60),random_time%60)
    deliveryrating= random.randrange(1,5)
    merchantrating=random.randrange(1,5)
    orderstatus=1
    var_list  = ['orderbasketid','itemcount','businesstypeid','datecreated','customerid','countryid','cityid','orderzoneid', 'orderzonelat','orderzonelong','merchantid','merchantzoneid','merchantzonelat','merchantzonelong','ordervalue','ordercurrency','platformdeliveryfee','merchantpromocode','merchantpromo','platformpromocode','platformpromo','tax','netpaidbycustomer','orderplacedtime','orderacceptedtime','riderassignedtime','riderid','rideronwaytime','orderdeliveredtime','deliveryrating','merchantrating','orderstatus']
    final_outp=''
    for x in var_list:
        if x == 'orderstatus':
            final_outp = final_outp + "{}".format(eval(x))
        else:
            final_outp = final_outp + "{},".format(eval(x))
    print(final_outp)

###########
########
cust_start=100000
cust_end=110000
cust_lapse=1000
cust_incr=10000
date_start=datetime.date(2022,1,1)
date_end=datetime.date(2022,2,28)
while(date_start<date_end):
    if date_start > datetime.date(2022,2,20) :
        for x in range(1,random.randrange(1001,2001)):
            generate_cols(date_start.isoformat(),cust_start,cust_end,x)
    cust_start=cust_start+cust_lapse
    cust_end=cust_end+cust_incr
    date_start=date_start+datetime.timedelta(days=1)
