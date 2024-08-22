import tkinter as tk

dad_sent = {'January': 2515, 'February': 13500, 'March': 18500, 'April': 16300, 'May': 15500, 'June': 6200,
            'July': 3000, 'August': 14000, 'September': 6000, 'October': 23700, 'November': 43000, 'December': 19000}
mom_sent = {'January': 1000, 'February': 500, 'March': 6400, 'April': 1500, 'May': 8500, 'June': 500, 'July': 500,
            'August': 5600, 'September': 1200, 'October': 6200, 'November': 10300, 'December': 0}

atm = 101000
dad_total = mom_total = 0

for i, j in dad_sent.items():
    dad_total += j
for i, j in mom_sent.items():
    mom_total += j

root = tk.Tk()
root.geometry('600x600')
root.title('Expenses over the year')

l1 = tk.Label(root, text=f'Dad sent a total amount of Rs. {dad_total} in 2023 including ATM transactions',
              font=('Arial', 12, "bold"))
l1.place(x=10, y=10)

l3 = tk.Label(root, text=f'Excluding the ATM transactions, the amount sent is Rs. {dad_total - atm}',
              font=('Arial', 12, "bold"))
l3.place(x=10, y=40)

l2 = tk.Label(root, text=f'Mom sent a total amount of Rs. {mom_total} in 2023', font=('Arial', 12, "bold"))
l2.place(x=10, y=70)

text = 'Fuel was Rs. 14358.77, on an average about Rs. 900 a month\n' \
       'Vodafone/ Airtel bills accounts for Rs. 5786 in the entire year\n' \
       'Food had an average spend of Rs. 158 every month\n' \
       'Stationary account for an average of Rs. 50 every month\n' \
       'Groceries have an average of Rs. 3000 every month\n' \
       'Haircuts have a spend of Rs. 75 every month\n' \

l4 = tk.Label(root, text=text, font=('Arial', 12, "bold"))
l4.place(x=10, y=100)

text1 = f'Total sent to me is Rs. {mom_total + dad_total} and \n' \
        f'excluding the ATM it is Rs. {mom_total + dad_total - atm}\n' \
        f'Average sent per month would be Rs. {((mom_total + dad_total)/12).__round__(2)} including ATM\n' \
        f'Excluding ATM, Average sent per month would be Rs. {(mom_total + dad_total - atm)/12}'

l5 = tk.Label(root, text=text1, font=('Arial', 12, "bold"))
l5.place(x=10, y=250)

text2 = 'Fuel every month will account Rs. 1400 Airtel bill to Rs. 700 Miscellaneous costs upto 500 a month\n'

root.mainloop()
