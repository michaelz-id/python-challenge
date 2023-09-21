import os
import csv

#Declare variables
RowCount = 0
NetProfit = 0
TotalChange = 0
ValueChange = 0
PrevProfit = None
average_change = 0
Profit = 0
MaxInc = 0
MaxDec = 0
MaxInc_month = ""
MaxDec_month = ""


#file path
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open csv
with open(budget_csv) as csvfile:

    #Check
    #print(csvfile)

    # csv reader with delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
  
    #Exclude header from the count
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #Count records, exclude header
        RowCount = RowCount+1
               
        NetProfit = NetProfit + int(row[1])

        #calc the monthly change from the previous row          
        Profit =  int(row[1])
        if PrevProfit is not None:
            ValueChange = Profit - PrevProfit
            TotalChange = TotalChange + ValueChange

        #print(ValueChange)

        #set variable to return the month for the max increase and decrease
        month = row[0] 
        
        #calc max increase and decrease in monthly profits
        if ValueChange > MaxInc:
            MaxInc = ValueChange
            MaxInc_month = month
        elif ValueChange < MaxDec:
            MaxDec = ValueChange 
            MaxDec_month = month
        #set first profit
        PrevProfit = Profit

average_change = TotalChange / (RowCount -1)
average_change = "{:.2f}".format(average_change)

#print results
print("Financial Analysis")

print("------------------------------------------")

print('Total Months: ', RowCount)
print('Total Profit: $', NetProfit)
print('Average Change: $', average_change)
print('Greatest Increase in Profits: ', MaxInc_month, '($', MaxInc,')')
print('Greatest Decrease in Profits: ', MaxDec_month, '($', MaxDec,')')

#save to file
save_path = ("analysis")

name_of_file = 'Financial_Analysis.txt'

path_file = os.path.join(save_path, name_of_file)

with open(path_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------------------\n")
    txtfile.write(f'Total Months: {RowCount}\n')
    txtfile.write(f'Total Profit ${NetProfit}\n')
    txtfile.write(f'Average Change: ${average_change}\n')
    txtfile.write(f'Greatest Increase in Profits: {MaxInc_month} (${MaxInc})\n')
    txtfile.write(f'Greatest Decrease in Profits: {MaxDec_month} (${MaxDec})\n')  