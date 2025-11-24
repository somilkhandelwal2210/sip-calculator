import math
import matplotlib.pyplot as plt
import datetime 

def SIP_calc(i,t,a):
    tm = t*12
    a1 = a/100
    #calculation of total invrstment
    total_ivst = i*tm
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("-------- SIP Calculation Report --------")

    if(t <= 0 or i <= 0 or a < 0):
        print("Monthly Investment, Time Period and Return Rate should be positive")
        
    if(a==0):
        maturity_amt = i*tm
        print("maturity amount at 0% intersest (in rupees) :",maturity_amt)
        print("interest amount : 0")

    else:
        # calculation of monthly rate
        r = math.pow((1+a1),(1/12)) - 1
       # calculation of Maturity Amount
        p = 1+r
        z = math.pow(p,tm) - 1
        x = (i*z)/r
        maturity_amt = x*(1+r)
        interest_amt = maturity_amt - total_ivst


        print("Matured Amount after",t,"years (in rupees) :",int(maturity_amt))
        print("Total investment after",t,"years (in rupees) :",int(total_ivst))
        print("Interest Amount (in rupees) :",int(interest_amt))
        print("Date of calculation:",current_time)

        # Calculation and storing of Matured Amounts for each month
        
        mt = []
        for month in range(1, tm + 1):
            current_maturity = (i * (math.pow(1 + r, month) - 1) / r) * (1 + r)
            mt.append(current_maturity)
        
        # Plotting the data
        plt.figure(figsize = (10,5))
        plt.plot(range(1,tm+1), mt, label = "Matured Amounts")
        plt.title('SIP Growth Over Time')
        plt.xlabel('No. of months')
        plt.ylabel('Matured Amount (in rupees in millions)')
        plt.legend()
        plt.grid(True)
        plt.show() 

# Testing
x = float(input("Enter Monthly Investment Amount (in rupees) :"))
y = int(input("Enter Time period (in Years) :"))
z = float(input("Enter Annual return (in %) :"))
   
SIP_calc(x,y,z)
