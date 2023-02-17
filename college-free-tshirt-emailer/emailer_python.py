import smtplib
import spreadsheet_python as sp
#import testspreadsheet_python as ts


my_email = 'colehfeely@gmail.com'
my_password = ''

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(my_email,my_password)
    


    
    
    
    for i in range(1632,len(sp.names)):
        print(sp.names[i],i)
        print(sp.emails[i])
        subject = 'Consider attending in the spring'
        body = 'Dear Office of Admissions, (Message asking for T-Shirt) (Address) (Sincerely, Name)'%sp.names[i]
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(my_email,sp.emails[i],msg)
