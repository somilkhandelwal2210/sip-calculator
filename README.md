Title:
SIP calculator

Overview Of the project

In today's financial world, Systematic Investment Plans (SIPs) are a popular option for building wealth over time. However, figuring out compound interest with monthly contributions and seeing the growth can be tricky for most users. This project, the SIP Calculator & Visualizer, is a Python application that aims to make financial planning easier. It takes user inputs on investment amounts and expected returns, applies standard compounding formulas, and gives both a numerical summary and a visual graph of wealth growth over time.

Features

1. Precise Financial Calculation: Accurately calculates the Maturity Amount, Total Investment, and Wealth Gained (Interest) based on monthly inputs.

2. Visual Growth Tracking: Generates a dynamic line graph using Matplotlib to visualize how the investment grows month-by-month over the selected tenure.

3. Real-Time Reporting: Generates a timestamped calculation report, providing an instant summary of the investment plan.

4. Compound Interest Logic: Uses the geometric monthly rate formula to ensure high precision in return calculations, rather than simple averages.

5. Input Validation: Includes error handling to manage edge cases, such as 0% interest rates or invalid negative inputs.

Technologies/Tools used:

1.Python

2.Math(Numpy)

3.Matplotlib

4.Datetime

Steps to install and run the project

1. Ensure you have Python 3.x installed on your system.

2. Install the required visualization library by running this command in your terminal:

pip install matplotlib

3. Navigate to the project folder and run the script in terminal :

python SIP.py

Once the script is running, follow the on-screen prompts to enter your investment details:

Monthly Investment: Enter the amount in Rupees (e.g., 5000).

Time Period: Enter the duration in Years (e.g., 5).

Annual Return: Enter the expected interest rate in % (e.g., 12).

A graph window will open automatically showing your wealth growth over time.

Instructions for Testing

Testing Instructions
Run the script using python SIP.py and enter these sample values:

Investment: 5000

Time: 1 (Year)

Return: 12 (%)

Verify Results: Check that the console prints the financial summary and a Matplotlib graph window opens automatically to show the growth curve.



