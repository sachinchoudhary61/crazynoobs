import smtplib

def smtp(name,l,otp,email):
    msg = "--*---*------WELCOME-----*---*--\n\n\n" \
          "          HI,%s \n\n" \
          "          This is confidential." \
          " For security reasons,\n" \
          "           DO NOT share the LINK with anyone. \n\n" \
          "             Link  : %s \n\n" \
          "          Link Genrated date     : %s \n\n" % (name, l, str(otp))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('stheartsachu@gmail.com', 'stoneheartsachu')
    server.sendmail('stheartsachu@gmail.com', email, msg)
    server.quit()
