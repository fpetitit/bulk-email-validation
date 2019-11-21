import re
import pandas as pd

#read emails csv
data = pd.read_csv('emails.csv')

#get first column of data only
df = data.iloc[:,0]

#flatten column to get list of emails
flat_emails = df.values.flatten()

#convert all upper case characters to lower case so that you dont get false positives from regex
emails = map(lambda x:x.lower(),flat_emails)

bad_emails_count = 0
bad_emails = []

for email in emails:
    
     match = re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)

     if match == None:
         print("%s has bad syntax" % (email))
         bad_emails_count += 1
         bad_emails.append(email)
    
print("---------------------%d emails are not correct----------------------------" %(bad_emails_count))
print("---------------------------------------------------------------------------")
print(bad_emails)
