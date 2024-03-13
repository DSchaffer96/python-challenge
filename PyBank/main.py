import os
import csv

#Set path for file
bank_csv = os.path.join("Resources","budget_data.csv")

monthCount=0
netAmount=0
prevRow=0
change=0
changeSum=[]

#Keeps track of the greatest increases and decreases
grtstInc=0
gIncMonth=""
grtstDec=9999999
gDecMonth=""

#File reader
with open(bank_csv,'r') as bank_in:
    reader=csv.reader(bank_in,delimiter=",")

    #Skip header
    header=next(bank_in)

    for row in reader:
        change=prevRow-int(row[1])       #Tracks the amount of money made or lost from month to month
        changeSum.append(change)         #Sum of all the changes
        monthCount+=1                    #Counts the total amount of months
        netAmount=netAmount+int(row[1])  #Sums up the net amount of money remaining at the end
        prevRow=int(row[1])              #Sets prevRow to the current row to calculate the next change

        #Tracks which months had the greatest increase and decrease
        if change>grtstInc:
            grtstInc=change
            gIncMonth=row[0]
        elif change<grtstDec:
            grtstDec=change
            gDecMonth=row[0]
    

    avgChanges=sum(changeSum)/len(changeSum)      #Calculates the average change amount

#File writer
bank_output=os.path.join('analysis','financial_analyis.csv')
with open(bank_output, 'w') as bankFile:
    writer = csv.writer(bankFile, delimiter=',')
    writer.writerow(['Financial Analysis'])
    writer.writerow(['--------------------------------------------------------'])
    writer.writerow(['Total Months: ',str(monthCount)])
    writer.writerow(['Total: $',str(netAmount)])
    writer.writerow(['Average Change: $','${:.2f}'.format(avgChanges)])
    writer.writerow(['Greatest Increase in Profits: ',gIncMonth,' ($',str(grtstInc),')'])
    writer.writerow(['Greatest Decrease in Profits: ',gDecMonth,' ($',str(grtstDec),')'])
    print("Financial Analysis")
    print("--------------------------------------------------------")
    print("Total Months: "+str(monthCount))
    print("Total: $"+str(netAmount))
    print("Average Change: "+'${:.2f}'.format(avgChanges))
    print("Greatest Increase in Profits: "+gIncMonth+" ($"+str(grtstInc)+")")
    print("Greatest Decrease in Profits: "+gDecMonth+" ($"+str(grtstDec)+")")