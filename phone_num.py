Database = {'0803' : 'MTN',
            '0814' : 'MTN', 
            'O806' : 'MTN', 
            '0903' : 'MTN', 
            '0906' : 'MTN',
            '0805' : 'GLO',
            '0907' : 'GLO', 
            '0905' : 'GLO', 
            '0807' : 'GLO',
            '0809' : 'ETISALAT', 
            '0909' : 'ETISALAT', 
            '0817' : 'ETISALAT', 
            '0818' : 'ETISALAT',
            '0708' : 'AIRTEL', 
            '0701' : 'AIRTEL', 
            '0812' : 'AIRTEL', 
            '0902' : 'AIRTEL'
            }
num = input('Enter the Phone Number to Check : ')
check = num[0:4]

# check = '0817'

if check in Database:
    print("The Number is an {} line. ".format(Database[check]))
else:
    print("Pls Check the line and try again")
