import smtplib

def smtp2(name,l,otp,email):
    msg = "--*---*------WELCOME-----*---*--\n\n\n" \
          "          HI,%s \n\n" \
          "          This is confidential." \
          " For security reasons,\n" \
          "Use this OTP to Reset your Password \n" \
          "           DO NOT share the OTP with anyone. \n\n" \
          "             OTP  : %s \n\n" \
          "          OTP Genrated Time and Date     : %s \n\n" % (name, l, str(otp))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('stheartsachu@gmail.com', 'stoneheartsachu')
    server.sendmail('stheartsachu@gmail.com', email, msg)
    server.quit()
