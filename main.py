import smtplib
try:
    #Create your SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

   #Use TLS to add security
    smtp.starttls()

    #User Authentication
    smtp.login("adresse_émetteur","mot de passe")

    #Defining The Message
    message = "hello i send you a message using python"

    Subject: "Test Email"

    #Sending the Email
    smtp.sendmail("émetteur", "recepteur", message)

    #Terminating the session
    smtp.quit()
    print ("Email sent successfully!")

except Exception as ex:
    print("Something went wrong....",ex)

