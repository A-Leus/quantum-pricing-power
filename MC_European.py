from numpy import *
from numpy.random import standard_normal, seed
import re

seed(150000)
steps=100
paths=1000000


x = re.compile('\d+(\.\d+)?')
val = input("Enter your option (Call /Put):").lower()
while (val  != str("call") and val != str("put")):
    val = input("Entered value is wrong.Please try again...\nEnter your option (call / put): ").lower() 
    
spot_price = input('Enter the spot price:')
while  x.match(spot_price)==None:
    spot_price = input("Entered value is wrong.Please try again...\nEnter spot price: ")
    
volatility = input("Enter the implied volatility:")
while x.match(volatility)==None:
    volatility = input("Entered value is wrong.Please try again...\nEnter volatility: ")
volatility=float(volatility)
   
rate = input("Enter interest rate:")
while x.match(rate)==None:
    rate = input("Entered value is wrong.Please try again...\nEnter rate: ")
rate=float(rate)
     
days = input("Enter days to maturity:")
while x.match(days)==None:
    days = input("Entered value is wrong.Please try again...\nEnter days to maturity: ")
days=float(days)
days=days/250
        
strike_price = input("Enter strike price:")
while x.match(strike_price)==None:
    strike_price = input("Entered value is wrong.Please try again...\nEnter strike price: ")
strike_price =float(strike_price)

dt=days/steps

df=exp(-rate*dt)

S=zeros((steps+1,paths),'d')
S[0,:]=spot_price


for x in range(1, steps+1,1):
    ran=standard_normal(paths)
    S[x,:]=S[x-1,:]*exp((rate-volatility**2/2)*dt+volatility*ran*sqrt(dt))

if val=="put":
    h=maximum(strike_price-S[-1],0)
else:
    h=maximum(-strike_price+S[-1],0)
estimator=exp(-rate*days)*sum(h)/paths

print(estimator)
     



