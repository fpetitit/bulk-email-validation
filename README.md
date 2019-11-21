## Bulk email validation script in python
the script validates emails using a regular expression.
Given a csv file of emails, the script will go through the emails and check if they are valid. The script will then output the number of bad emails as well as the specific emails that would have failed validation.

*Emails are converted to lower case before being validated*

### How to use

Put a CSV file containing the addresses into the directory of the script and name it "emails.csv".

Launch the command :
```
/usr/bin/python3 ./email_validation.py
```

It should display all the emails with errors.
