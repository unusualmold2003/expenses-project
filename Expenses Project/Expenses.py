import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image,ImageTk

class E_2023:
    sizes2 = [90, 80, 353, 1492, 790.5, 263, 170, 352.82, 170, 0]
    sizes3 = [10, 80, 1499, 954, 1601.13, 307, 0, 762, 469, 105]
    sizes4 = [67, 150, 425, 1325, 0, 242, 170, 352.82, 1004, 0]
    sizes5 = [70, 1290, 2505.75, 837.6, 2133.33, 145, 398.34, 0, 16167, 0]

    def February(self):
        df1 = pd.read_csv('D:\\Python Programs\\Random Things\\Expenses Project\\CSV Files\\Expenses Project - February Expenses.csv')
        d1 = df1['Xerox']
        d2 = df1['Stationary']
        d3 = df1['Groceries']
        d4 = df1['Food']
        d5 = df1['Petrol']
        d6 = df1['Medicine']
        d7 = df1['Haircut']
        d8 = df1['Vodafone']
        d9 = df1['Misc']
        total = sum(df1['Total'])
        print("Total expenditure over the month of February:", total)

        dict1 = {'Xerox': sum(d1), 'Stationary': sum(d2), 'Groceries': sum(d3), 'Food': sum(d4), 'Petrol': sum(d5),
             'Medicine': sum(d6), 'Haircut': sum(d7), 'Vodafone': sum(d8), 'Misc': sum(d9)}
        labels = []
        sizes = []
        my_explode = [0, 0, 0, 0.4, 0, 0, 0, 0, 0]
        for x, y in dict1.items():
            labels.append(x)
            sizes.append(y)

        # plt.pie(sizes, labels=labels, explode=my_explode, shadow=True, autopct='%1.1f%%')
        window = tk.Tk()
        window.geometry("500x500")
        window.title("Expenses over the month of February")
        Search_image = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\March Pics\\Figure_February.png")
        myimage = tk.Label(master = window, image=Search_image)
        myimage.place(x=20,y=20)

        l1 = tk.Label(master=window, text="Expenses over the month of February :{0}".format(total), font=('Arial', 14))
        l1.place(x=65, y=250)
        # plt.title("Total Expenses in February")
        # plt.axis('equal')
        # plt.show()
        window.mainloop()

    def March(self):
        global sizes3,sizes2
        df1 = pd.read_csv('D:\\Python Programs\\Random Things\\Expenses Project\\CSV Files\\Expenses Project - March Expenses.csv')
        d1 = df1['Xerox']
        d2 = df1['Stationary']
        d3 = df1['Groceries']
        d4 = df1['Food']
        d5 = df1['Petrol']
        d6 = df1['Medicine']
        # d7 = df1['Haircut']
        d8 = df1['Vodafone']
        d9 = df1['Misc']
        d10 = df1['Taxi']
        total = sum(df1['Total'])
        print("Total expenditure over the month of March:", total)
        dict1 = {'Xerox': sum(d1), 'Stationary': sum(d2), 'Groceries': sum(d3), 'Food': sum(d4), 'Petrol': sum(d5),
             'Medicine': sum(d6), 'Vodafone': sum(d8), 'Misc': sum(d9), 'Taxi':sum(d10)}

        labels = []
        sizes = []
        my_explode = [0, 0, 0, 0, 0.4, 0, 0, 0, 0]
        for x, y in dict1.items():
            labels.append(x)
            sizes.append(y)

        # plt.pie(sizes, labels=labels, explode=my_explode, shadow=True, autopct='%1.1f%%')
        window = tk.Tk()
        window.geometry("1700x1000")
        window.title("Expenses over the month of March")

        l1 = tk.Label(window, text="Expenses over the month of March: Rs {0}".format(total), font=('Arial', 14))
        l1.place(x=1100, y=120)

        Search_image = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\March Pics\\Figure_March.png")
        myimage = tk.Label(image=Search_image)
        myimage.place(x=20,y=20)

        Search_image1 = tk.PhotoImage(file="D:\Python Programs\Random Things\Expenses Project\Pics\March Pics\Screenshot 2023-04-07 133419.png")
        myimage1 = tk.Label(image=Search_image1)
        myimage1.place(x=700,y=20)

        Search_image2 = tk.PhotoImage(file="D:\Python Programs\Random Things\Expenses Project\Pics\March Pics\March_Comparison.png")
        myimage2 = tk.Label(image=Search_image2)
        myimage2.place(x=700,y=300)

        # dict_text = tk.Text(window)
        # dict_text.pack()
        # for key, value in dict1.items():
        #     dict_text.insert(tk.END, f"{key}: {value}\n")

        # plt.title("Total Expenses in March")
        # plt.axis('equal')
        # plt.show()

        percentage = []
        for i in range(len(sizes3)):
            if(sizes2[i]==0):
                break
            else:
                percentage.append((((sizes3[i]-sizes2[i])/sizes2[i])*100))

        # plt.bar(labels,percentage)
        # plt.yticks([-100, -75, -50, -25, 0, 25, 50, 75, 100], ['-100', '-75', '-50', '-25','0%', '25%', '50%', '75%', '100%'])
        # plt.title('Increase/Decrease over the month')
        # plt.xlabel('Categories')
        # plt.ylabel('Percentage increase')
        # plt.show()

        window.mainloop()

    def April(self):
        global sizes4,sizes5
        df1 = pd.read_csv('D:\Python Programs\Random Things\Expenses Project\CSV Files\Expenses Project - April Expenses.csv')
        d1 = df1['Xerox']
        d2 = df1['Stationary']
        d3 = df1['Groceries']
        d4 = df1['Food']
        d5 = df1['Petrol']
        d6 = df1['Medicine']
        d7 = df1['Haircut']
        d8 = df1['Vodafone']
        d9 = df1['Misc']
        d10 = df1['Taxi']
        total = sum(df1['Total'])
        print("Total expenditure over the month of April:", total)
        dict1 = {'Xerox': sum(d1), 'Stationary': sum(d2), 'Groceries': sum(d3), 'Food': sum(d4), 'Petrol': sum(d5),
             'Medicine': sum(d6), 'Haircut':sum(d7), 'Vodafone': sum(d8), 'Misc': sum(d9), 'Taxi':sum(d10)}

        labels = []
        sizes = []
        my_explode = [0, 0, 0, 0, 0.4, 0, 0, 0, 0]
        for x, y in dict1.items():
            labels.append(x)
            sizes.append(y)

        # plt.pie(sizes, labels=labels, explode=my_explode, shadow=True, autopct='%1.1f%%')
        window = tk.Tk()
        window.geometry("1700x1000")
        window.title("Expenses over the month of April")

        l1 = tk.Label(window, text="Expenses over the month of April: Rs {0}".format(total), font=('Arial', 14))
        l1.place(x=20, y=500)

        Search_image = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\Figure_April.png")
        myimage = tk.Label(image=Search_image)
        myimage.place(x=20,y=20)

        Search_image1 = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\dictionary_april.png")
        myimage1 = tk.Label(image=Search_image1)
        myimage1.place(x=700,y=20)

        Search_image2 = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\April_Comparison.png")
        myimage2 = tk.Label(image=Search_image2)
        myimage2.place(x=700,y=300)


        # dict_text = tk.Text(window)
        # dict_text.pack()
        # for key, value in dict1.items():
        #     dict_text.insert(tk.END, f"{key}: {value}\n")

        # plt.title("Total Expenses in March")
        # plt.axis('equal')
        # plt.show()

        percentage = []
        for i in range(len(sizes4)):
            if(sizes3[i]==0):
                percentage.append(sizes4[i])
            else:
                percentage.append((((sizes4[i]-sizes3[i])/sizes3[i])*100))

        # plt.bar(labels,percentage)
        # plt.yticks([-500, -400, -300, -200, -100, -75, -50, -25, 0, 25, 50, 75, 100, 200, 300, 400, 500], ['-500%', '-400%', '-300%', '-200%','-100%', '-75%', '-50%', '-25%','0%', '25%', '50%', '75%', '100%', '200%', '300%', '400%', '500%'])
        # plt.title('Increase/Decrease over the month')
        # plt.xlabel('Categories')
        # plt.ylabel('Percentage changes')
        # plt.grid()
        # plt.show()

        window.mainloop()

    def May(self):
        global sizes4,sizes5
        df1 = pd.read_csv('D:\\Python Programs\\Random Things\\Expenses Project\\CSV Files\\Expenses Project - August Expenses.csv')
        d1 = df1['Xerox']
        d2 = df1['Stationary']
        d3 = df1['Groceries']
        d4 = df1['Food']
        d5 = df1['Petrol']
        d6 = df1['Medicine']
        d7 = df1['Haircut']
        d8 = df1['Vodafone']
        d9 = df1['Misc']
        d10 = df1['Taxi']
        total = df1['Total'].sum()
        print("Total expenditure over the month of May:", total)
        dict1 = {'Xerox': sum(d1), 'Stationary': sum(d2), 'Groceries': sum(d3), 'Food': sum(d4), 'Petrol': sum(d5),
             'Medicine': sum(d6), 'Haircut':sum(d7), 'Vodafone': sum(d8), 'Misc': sum(d9), 'Taxi':sum(d10)}

        labels = []
        sizes = []
        # my_explode = [0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0]
        for x, y in dict1.items():
            labels.append(x)
            sizes.append(y)

        plt.pie(sizes, labels=labels, shadow=True, autopct='%1.1f%%')
        plt.show()
        window = tk.Tk()
        window.geometry("1700x1000")
        window.title("Expenses over the month of May")

        l1 = tk.Label(window, text="Expenses over the month of May: Rs ${:,.2f}".format(total), font=('Arial', 14))
        l1.place(x=20, y=500)

        Search_image = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\Figure_April.png")
        myimage = tk.Label(image=Search_image)
        myimage.place(x=20,y=20)

        Search_image1 = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\dictionary_april.png")
        myimage1 = tk.Label(image=Search_image1)
        myimage1.place(x=700,y=20)

        Search_image2 = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\April_Comparison.png")
        myimage2 = tk.Label(image=Search_image2)
        myimage2.place(x=700,y=300)


        # dict_text = tk.Text(window)
        # dict_text.pack()
        # for key, value in dict1.items():
        #     dict_text.insert(tk.END, f"{key}: {value}\n")

        # plt.title("Total Expenses in March")
        # plt.axis('equal')
        # plt.show()

        percentage = []
        for i in range(len(sizes5)):
            if(sizes4[i]==0):
                percentage.append(sizes5[i])
            else:
                percentage.append((((sizes5[i]-sizes4[i])/sizes4[i])*100))

        # plt.bar(labels,percentage)
        # plt.yticks([-500, -400, -300, -200, -100, -75, -50, -25, 0, 25, 50, 75, 100, 200, 300, 400, 500], ['-500%', '-400%', '-300%', '-200%','-100%', '-75%', '-50%', '-25%','0%', '25%', '50%', '75%', '100%', '200%', '300%', '400%', '500%'])
        # plt.title('Increase/Decrease over the month')
        # plt.xlabel('Categories')
        # plt.ylabel('Percentage changes')
        # plt.grid()
        # plt.show()

        window.mainloop()

    def August(self):
        global sizes4,sizes5
        df1 = pd.read_csv('D:\\Python Programs\\Random Things\\Expenses Project\\CSV Files\\Expenses Project - May Expenses.csv')
        d1 = df1['Xerox']
        d2 = df1['Stationary']
        d3 = df1['Groceries']
        d4 = df1['Food']
        d5 = df1['Petrol']
        d6 = df1['Medicine']
        d7 = df1['Haircut']
        d8 = df1['Vodafone']
        d9 = df1['Misc']
        d10 = df1['Taxi']
        total = df1['Total'].sum()
        print("Total expenditure over the month of August:", total)
        dict1 = {'Xerox': sum(d1), 'Stationary': sum(d2), 'Groceries': sum(d3), 'Food': sum(d4), 'Petrol': sum(d5),
             'Medicine': sum(d6), 'Haircut':sum(d7), 'Vodafone': sum(d8), 'Misc': sum(d9), 'Taxi':sum(d10)}

        labels = []
        sizes = []
        # my_explode = [0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0]
        for x, y in dict1.items():
            labels.append(x)
            sizes.append(y)

        plt.pie(sizes, labels=labels, shadow=True, autopct='%1.1f%%')
        plt.show()
        window = tk.Tk()
        window.geometry("1700x1000")
        window.title("Expenses over the month of August")

        l1 = tk.Label(window, text="Expenses over the month of August: Rs ${:,.2f}".format(total), font=('Arial', 14))
        l1.place(x=20, y=500)

        # Search_image = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\Figure_April.png")
        # myimage = tk.Label(image=Search_image)
        # myimage.place(x=20,y=20)

        # Search_image1 = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\dictionary_april.png")
        # myimage1 = tk.Label(image=Search_image1)
        # myimage1.place(x=700,y=20)

        # Search_image2 = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\April Pics\\April_Comparison.png")
        # myimage2 = tk.Label(image=Search_image2)
        # myimage2.place(x=700,y=300)

        # dict_text = tk.Text(window)
        # dict_text.pack()
        # for key, value in dict1.items():
        #     dict_text.insert(tk.END, f"{key}: {value}\n")

        # plt.title("Total Expenses in March")
        # plt.axis('equal')
        # plt.show()

        percentage = []
        for i in range(len(sizes5)):
            if(sizes4[i]==0):
                percentage.append(sizes5[i])
            else:
                percentage.append((((sizes5[i]-sizes4[i])/sizes4[i])*100))

        # plt.bar(labels,percentage)
        # plt.yticks([-500, -400, -300, -200, -100, -75, -50, -25, 0, 25, 50, 75, 100, 200, 300, 400, 500], ['-500%', '-400%', '-300%', '-200%','-100%', '-75%', '-50%', '-25%','0%', '25%', '50%', '75%', '100%', '200%', '300%', '400%', '500%'])
        # plt.title('Increase/Decrease over the month')
        # plt.xlabel('Categories')
        # plt.ylabel('Percentage changes')
        # plt.grid()
        # plt.show()

        window.mainloop()

    def choice(self):
        choice = input("Enter the month:")
        choice.islower()

        if choice == 'february' or choice == 'feb' or choice == '2':
            E_2023.February(self)
        elif choice == 'march' or choice == 'mar' or choice == '3':
            E_2023.March(self)
        elif choice == 'april' or choice == 'apr' or choice == '4':
            E_2023.April(self)
        elif choice == 'may' or choice == '5':
            E_2023.May(self)
        elif choice == 'august' or choice == 'aug' or choice == '8':
            E_2023.August(self)
        else:
            print("Invalid choice")
            E_2023.choice(self)

    # E_2023.choice()


class E_2024:
    # sizes_jan = [90, 80, 353, 1492, 790.5, 263, 170, 352.82, 170, 0]

    @staticmethod
    def January():
        dad_sent = 1500+15000+500+2000+1000+1000+1000+1000
        mom_sent = 6500
        df1 = pd.read_csv('D:\\Python Programs\\Random Things\\Expenses Project\\CSV Files\\2024\\Expenses Project - '
                          'January Expenses.csv')
        d1 = df1['Xerox']
        d2 = df1['Stationary']
        d3 = df1['Groceries']
        d4 = df1['Food']
        d5 = df1['Petrol']
        d6 = df1['Medicine']
        d7 = df1['Haircut']
        d8 = df1['Vodafone']
        d9 = df1['Misc']
        d10 = df1['Taxi']
        total = df1['Total'].sum()
        print("Total expenditure over the month of January 2024: Rs. ", total)
        print("Total amount sent by Mom over the month of January 2024:", mom_sent)
        print("Total amount sent by Dad over the month of January 2024:", dad_sent)
        dict1 = {'Xerox': sum(d1), 'Stationary': sum(d2), 'Groceries': sum(d3), 'Food': sum(d4), 'Petrol': sum(d5),
                 'Medicine': sum(d6), 'Haircut': sum(d7), 'Vodafone': sum(d8), 'Misc': sum(d9), 'Taxi':sum(d10)}

        labels = []
        sizes = []
        my_explode = [0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0]
        for x, y in dict1.items():
            labels.append(x)
            sizes.append(y)

        plt.pie(sizes, labels=labels, shadow=True, autopct='%1.1f%%', explode=my_explode)
        plt.show()
        window = tk.Tk()
        window.geometry("1700x1000")
        window.title("Expenses over the month of January 2024")

        l1 = tk.Label(window, text="Expenses over the month of January 2024: Rs {:,.2f}".format(total), font=('Arial', 14))
        l1.place(x=20, y=500)

        # Search_image = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\Pics\\
        # April Pics\\Figure_April.png")
        # myimage = tk.Label(image=Search_image)
        # myimage.place(x=20,y=20)

        # Search_image1 = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\
        # Pics\\April Pics\\dictionary_april.png")
        # myimage1 = tk.Label(image=Search_image1)
        # myimage1.place(x=700,y=20)

        # Search_image2 = tk.PhotoImage(file="D:\\Python Programs\\Random Things\\Expenses Project\\
        # Pics\\April Pics\\April_Comparison.png")
        # myimage2 = tk.Label(image=Search_image2)
        # myimage2.place(x=700,y=300)

        # dict_text = tk.Text(window)
        # dict_text.pack()
        # for key, value in dict1.items():
        #     dict_text.insert(tk.END, f"{key}: {value}\n")

        # plt.title("Total Expenses in March")
        # plt.axis('equal')
        # plt.show()

        # percentage = []
        # for i in range(len(sizes5)):
        #     if(sizes4[i]==0):
        #         percentage.append(sizes5[i])
        #     else:
        #         percentage.append((((sizes5[i]-sizes4[i])/sizes4[i])*100))

        # plt.bar(labels,percentage)
        # plt.yticks([-500, -400, -300, -200, -100, -75, -50, -25, 0, 25, 50, 75, 100, 200, 300, 400, 500],
        # ['-500%', '-400%', '-300%', '-200%','-100%', '-75%', '-50%', '-25%','0%', '25%', '50%', '75%', '100%',
        # '200%', '300%', '400%', '500%'])
        # plt.title('Increase/Decrease over the month')
        # plt.xlabel('Categories')
        # plt.ylabel('Percentage changes')
        # plt.grid()
        # plt.show()

        window.mainloop()


def choose():
    year = int(input("Enter the Year:"))
    if year == 2023:
        E_twozero = E_2023()
        choice = input("Enter the month:")
        choice.islower()

    elif year == 2024:
        E_twofour = E_2024()
        choice = input("Enter the month:")
        choice.islower()

        if choice == 'january' or choice == 'jan' or choice == '1':
            E_twofour.January()
        else:
            print("Invalid choice")
            choose()


choose()
