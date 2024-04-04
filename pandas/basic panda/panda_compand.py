import numpy as np
import pandas as pd


dict1 = ['a','b','c','d']

ds = pd.Series(dict1)



print(ds)

type(ds)

daily_rates_dollars =pd.Series([23,34,56,67,34])
print(daily_rates_dollars)
####################################################




###############################
aray_a = np.array([10,20,30,40,50])
print(aray_a)


#####################################
###### for size##########
print(type(aray_a))



#####################################################################################
################ using an index
import pandas as pd

price_per_cetagory =  {'product': 222250, 'product B':16600,'product C': 15600}
print(price_per_cetagory)

print(type(price_per_cetagory))

price_per_cetagory  = pd.Series(price_per_cetagory)
print(price_per_cetagory)



type(price_per_cetagory)

print(price_per_cetagory.index)


type(price_per_cetagory)
############################################################






##########label based vs position based #######################################
import pandas as pd

series_A = pd.Series ([12,23,45,56,78])
print(series_A)

print(series_A.index)

list(series_A.index)


price_per_cetagory = pd.Series( {'product': 222250, 'product B':16600,'product C': 15600})
print(price_per_cetagory)
print(price_per_cetagory.index)

print(type(price_per_cetagory.index))


################################################################





##############more work in pyhton############################
import pandas as pd
series_A = pd.Series([12,34,45])
price_per_cetagory = pd.Series({
    "apple": 5,
    "banana": 10,
    "orange": 7
})


print(series_A)
#################
print(series_A[0])
##################
print(price_per_cetagory)
#########################
print(price_per_cetagory['apple'])
print(price_per_cetagory[1])

###############################
series_b = pd.Series([10,20,30,40] , index=[1,2,3,4])
print(series_b)
##############################
print(series_b[1])
#####################################

####integer written as string 

import pandas as pd
series_c  = pd.Series([12,32,34,56,32], index = ['1','2','3','4','5'])
print(series_c)

print(series_c[1]) # implcit pyhton index return 32

print(series_c['1'])  # label based indexing

print(series_c[0])



####################################################






############Using methods in pyhton#############################
import pandas as pd
start_date_deposits = pd.Series({
    '7/4/2014'   : 2000,
    '1/2/2015'   : 2000,
    '12/8/2012'  : 1000,
    '2/20/2015'  : 2000,
    '10/28/2013' : 2000,
    '4/19/2015'  : 2000,
    '7/4/2016'   : 2000,
    '4/24/2014'  : 2000,
    '9/3/2015'   : 4000,
    '7/25/2016'  : 2000,
    '5/1/2014'   : 2000,
    '3/29/2013'  : 2000,
    '10/3/2014'  : 2000,
    '9/18/2015'  : 2500
})

print(start_date_deposits)
##### top 5 value 
print(start_date_deposits.head())
######### for some##
print(start_date_deposits.tail())
############
print(start_date_deposits.max())
print(start_date_deposits.min())
print(start_date_deposits.idxmax())
print(start_date_deposits.idxmin())





#####################################################





##############paramenter and argument #########################



import pandas as pd
start_date_deposits = pd.Series({
    '7/4/2014'   : 2000,
    '1/2/2015'   : 2000,
    '12/8/2012'  : 1000,
    '2/20/2015'  : 2000,
    '10/28/2013' : 2000,
    '4/19/2015'  : 2000,
    '7/4/2016'   : 2000,
    '4/24/2014'  : 2000,
    '9/3/2015'   : 4000,
    '7/25/2016'  : 2000,
    '5/1/2014'   : 2000,
    '3/29/2013'  : 2000,
    '10/3/2014'  : 2000,
    '9/18/2015'  : 2500
})

print(start_date_deposits.head(5))



#############################################################




############intro to panadas dataframes####################
import pandas as pd
data = {'ProductName':['Product A', 'Product B', 'Product C'], 'ProductPrice':[22250, 16600, 12500]}
df = pd.DataFrame(data)
print(df)

#################################
data = {'ProductName':['Product A', 'Product B', 'Product C','product D'], 'ProductPrice':[22250, 16600, 12500 , 12543]}
df = pd.DataFrame(data)
print(df)

##############################





###########specify the index##################
import pandas as pd
data = {'ProductName':['Product A', 'Product B', 'Product C','product D'], 'ProductPrice':[22250, 16600, 12500 , 12543]}
df = pd.DataFrame(data , index =['A','B','C','D'])
print(df)
############another method#############################
data = {'ProductName':['Product A', 'Product B', 'Product C','product D'], 'ProductPrice':[22250, 16600, 12500 , 12543]}
product_ID =['A','B','C','D']
df = pd.DataFrame(data, index = product_ID)
print(df)
###############################################





#################################################
import pandas as pd
data = [{'ProductName':'Product A', 'ProductPrice':22250}, 
        {'ProductName':'Product B', 'ProductPrice':16600}, 
        {'ProductName':'Product C', 'ProductPrice':12500},
        {'ProductName':'Product D'}]
df = pd.DataFrame(data)
print(df)


###########using pandas#######################################

import pandas as pd
series_product  = pd.Series(['product A','product B','prodcut C'])
series_price = pd.Series([22250,16600,12500])

data = {'productName':series_product ,'prodct_price' :series_price}
df = pd.DataFrame(data)
print(df)


############################################

ser_products = pd.Series(['Product A', 'Product B', 'Product C'], index = ['A', 'B', 'C'])
ser_prices = pd.Series([22250, 16600, 12500], index = ['A', 'B', 'C'])

data = {'ProductName':ser_products, 'ProductPrice':ser_prices}
df = pd.DataFrame(data)
print(df)

##############list of list#############################
data = [['prodcut A',22250],['product B',16600],['product C',12500,5000]]
df = pd.DataFrame(data)

#############################################





###############data frame in profesional way########
import pandas as pd
df = pd.DataFrame(data =[['product A',22250],['product B',16600],['product C',12500]],
                  columns  =['productName','ProductPrice'],
                  index = ['A','B','C']     )
print(df)

print(df.shape)




