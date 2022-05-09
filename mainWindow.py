import tkinter
from tkinter import *
from matplotlib.pyplot import margins
from numpy import *
import numpy as np

numberOfCustomers = 0
numberOfSuppliers = 0
customerEntries = {}
supplierEntries = {}
transportEntries = {}


def mainWindow():
    rootWindow = Tk()
    rootWindow.title("Middleman problem")
    rootWindow.configure(background="#fcdec5")
    rootWindow.resizable(width=False, height=False)
    global numberOfCustomers
    global numberOfSuppliers
    numberofCustomers = 0
    numberOfSuppliers = 0

    def submitInputData():

        def calculate():
            customersArray = np.arange(numberOfCustomers * 2).reshape(numberOfCustomers, 2)
            suppliersArray = np.arange(numberOfSuppliers * 2).reshape(numberOfSuppliers, 2)
            transportCostsArray = np.arange(numberOfCustomers * numberOfSuppliers).reshape(numberOfCustomers,
                                                                                           numberOfSuppliers)
            print(numberOfCustomers, numberOfSuppliers)
            temp5 = 0
            for i in range(0, numberOfSuppliers):
                for j in range(0, 2):
                    temp4 = int(supplierEntries[i + j + temp5].get())
                    suppliersArray[i][j] = temp4
                temp5 += 1
            print(suppliersArray)
            temp5 = 0
            for i in range(0, numberOfCustomers):
                for j in range(0, 2):
                    temp4 = int(customerEntries[i + j + temp5].get())
                    customersArray[i][j] = temp4
                temp5 += 1
            print(customersArray)
            temp5 = 0
            tempArray = []
            for i in range(0, numberOfCustomers * numberOfSuppliers):
                temp4 = int(transportEntries[i].get())
                tempArray.append(temp4)

            transportCostsArray = np.reshape(tempArray, (int(numberOfSuppliers), int(numberOfCustomers)))
            print(transportCostsArray)

            totalCost = 0
            revenue = 0
            middlemansProfit = 0

            resultsWindow = Tk()
            resultsWindow.resizable(width=False, height=False)
            resultsWindow.title("Results")
            resultsWindow.configure(bg="#fcdec5")

            resultLabel1 = Label(resultsWindow, text='Total cost:\t{}'.format(totalCost), font=("Helvetica,15"))
            resultLabel1.grid(sticky=N, row=0, column=0)
            resultLabel1.configure(fg='black', background="#fcdec5")

            resultLabel2 = Label(resultsWindow, text='Revenue:\t{}'.format(revenue), font=("Helvetica,15"))
            resultLabel2.grid(sticky=N, row=1, column=0)
            resultLabel2.configure(fg='black', background="#fcdec5")

            resultLabel3 = Label(resultsWindow, text='Middlemans profit:\t{}'.format(middlemansProfit),
                                 font=("Helvetica,15"))
            resultLabel3.grid(sticky=N, row=2, column=0)
            resultLabel3.configure(fg='black', background="#fcdec5")

            resultsWindow.mainloop()

        global numberOfCustomers
        global numberOfSuppliers
        global customerEntries
        global supplierEntries
        global transportEntries
        numberOfSuppliers = numberOfSuppliersEntry.get()
        numberOfCustomers = numberOfCustomersEntry.get()
        numberOfSuppliers = int(numberOfSuppliers)
        numberOfCustomers = int(numberOfCustomers)
        # print(numberOfSuppliers, numberOfCustomers)
        rootWindow.destroy()
        inputTableWindow = Tk()
        inputTableWindow.resizable(width=False, height=False)
        inputTableWindow.title("Input Data Tables")
        inputTableWindow.configure(bg="#fcdec5")

        columnLabel1 = Label(inputTableWindow, text="Supplier's ID")
        columnLabel1.grid(sticky=N, row=0, column=0)
        columnLabel1.configure(fg='black', bg="#fcdec5")

        columnLabel2 = Label(inputTableWindow, text="Supply")
        columnLabel2.grid(sticky=N, row=0, column=1)
        columnLabel2.configure(fg='black', bg="#fcdec5")

        columnLabel3 = Label(inputTableWindow, text="Selling price")
        columnLabel3.grid(sticky=N, row=0, column=2)
        columnLabel3.configure(fg='black', bg="#fcdec5")

        temp = 0
        temp2 = 0
        temp3 = 0
        cCounter = 0
        sCounter = 0
        tCounter = 0

        for i in range(0, numberOfSuppliers):
            columnLabel = Label(inputTableWindow, text='{}:'.format(i + 1), font=("Helvetica,15"))
            columnLabel.grid(sticky=N, row=i + 1, column=0)
            columnLabel.configure(fg='black', bg="#fcdec5")

            supplierEntries[sCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"))
            supplierEntries[sCounter].grid(sticky=N, row=i + 1, column=1)
            supplierEntries[sCounter].configure(fg="black")

            sCounter += 1

            supplierEntries[sCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"), fg="black")
            supplierEntries[sCounter].grid(sticky=N, row=i + 1, column=2)
            # suppliersData.append(supplierEntries[sCounter])

            sCounter += 1

            temp += 1

        columnLabel1 = Label(inputTableWindow, text="Customers's ID")
        columnLabel1.grid(sticky=N, row=temp + 2, column=0)
        columnLabel1.configure(fg='black', bg="#fcdec5")

        columnLabel2 = Label(inputTableWindow, text="Demand")
        columnLabel2.grid(sticky=N, row=temp + 2, column=1)
        columnLabel2.configure(fg='black', bg="#fcdec5")

        columnLabel3 = Label(inputTableWindow, text="Purchasing price")
        columnLabel3.grid(sticky=N, row=temp + 2, column=2)
        columnLabel3.configure(fg='black', bg="#fcdec5")

        for i in range(0, numberOfCustomers):
            columnLabel = Label(inputTableWindow, text='{}:'.format(i + 1), font=("Helvetica,15"))
            columnLabel.grid(sticky=N, row=temp + 3 + i, column=0)
            columnLabel.configure(fg='black', bg="#fcdec5")

            customerEntries[cCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"))
            customerEntries[cCounter].grid(sticky=N, row=temp + 3 + i, column=1)
            customerEntries[cCounter].configure(fg="black")
            # customersData.append(customerEntries[cCounter])
            cCounter += 1

            customerEntries[cCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"))
            customerEntries[cCounter].grid(sticky=N, row=temp + 3 + i, column=2)
            # entry.grid_columnconfigure(1, weight=1)
            customerEntries[cCounter].configure(fg="black")
            # customersData.append(customerEntries[cCounter])
            cCounter += 1

            temp2 += 1

        label = Label(inputTableWindow, width=10, font=("Helvetica,15"))
        label.grid(sticky=N, row=temp + temp2 + 3, column=0)
        label.configure(bg="#fcdec5")
        columnLabel2.configure(fg='black', bg="#fcdec5")

        for i in range(0, numberOfCustomers):
            label = Label(inputTableWindow, width=10, text='C{}:'.format(i + 1), font=("Helvetica,15"))
            label.grid(sticky=N, row=temp + temp2 + 3, column=i + 1)
            label.configure(bg="#fcdec5")
            columnLabel2.configure(fg='black', bg="#fcdec5")

        for i in range(0, numberOfSuppliers):
            label = Label(inputTableWindow, width=10, text='S{}:'.format(i + 1), font=("Helvetica,15"))
            label.grid(sticky=N, row=temp + temp2 + 4 + i, column=0)
            label.configure(bg="#fcdec5")
            columnLabel2.configure(fg='black', bg="#fcdec5")
            for j in range(0, numberOfCustomers):
                transportEntries[tCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"))
                transportEntries[tCounter].grid(sticky=N, row=temp + temp2 + 4 + i, column=j + 1)
                transportEntries[tCounter].configure(fg="black")
                # transportCostsData.append(transportEntries[tCounter])
                tCounter += 1
            temp3 = temp + temp2 + 4 + i

        submitButton = Button(inputTableWindow, text='Calculate', command=calculate, font=("Helvetica,15"), width=20)
        submitButton.grid(row=temp3 + 1, column=1)
        submitButton.config(fg='black', background="#fcdec5")

        inputTableWindow.mainloop()

    numberOfSuppliersLabel = Label(rootWindow, text="Number of suppliers", font=("Helvetica,15"))
    numberOfSuppliersLabel.grid(sticky=N, row=1, column=0)
    numberOfSuppliersLabel.configure(fg='black', background="#fcdec5")

    numberOfSuppliersEntry = Entry(rootWindow, width=20, fg="black", font=("Helvetica,15"))
    numberOfSuppliersEntry.grid(sticky=N, row=1, column=1, padx=3)

    numberOfCustomersLabel = Label(rootWindow, text="Number of clients", font=("Helvetica,15"))
    numberOfCustomersLabel.grid(sticky=N, row=2, column=0)
    numberOfCustomersLabel.configure(fg='black', background="#fcdec5")

    numberOfCustomersEntry = Entry(rootWindow, width=20, fg="black", font=("Helvetica,15"))
    numberOfCustomersEntry.grid(sticky=N, row=2, column=1, padx=3)

    button = Button(rootWindow, text='Submit data', command=submitInputData, font=("Helvetica,15"))
    button.grid(row=5, column=0)
    button.config(fg='black', background="#cfad91")

    rootWindow.mainloop()
