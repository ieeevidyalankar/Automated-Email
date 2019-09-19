import csv
from PIL import Image,ImageDraw,ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import shutil


def sending_mail(email_sender, email_receiver, names, password):
    subject='certificate'
    msg=MIMEMultipart()
    msg['From']= email_sender
    msg['to']= email_receiver
    msg['subject']= subject
    body ="""""" #add body no changes are to be made here
    msg.attach(MIMEText(body,'plain'))
    img_data = open('{}.png'.format(names), 'rb').read()
    #HTML body embeded in the email no changes are to be made here
    html="""\
    <html>
    <head>
    <H1>Greetings %s!</H1>
    </head>
    <body>
    <p><h4>Thanks for attending FUNDAMENTALS OF PYTHON AND DATA VISUALISATION Workshop
    <br><br>Kindly find your E-Certificate for the same, attached along with this mail.
    <br>We look forward to seeing you at all our future workshops, seminars and events!
    <br><br>Regards,
    <br>IEEE-VIT Student Branch
    <br><center><br>Connect with us on
    <br><p><a href="http://ieee.vit.edu.in/index.html"><img src="https://png.icons8.com/metro/1600/domain.png" height="50" width="50" hspace="20"><a href="https://www.instagram.com/ieeevit/"><img src="https://images-na.ssl-images-amazon.com/images/I/71VQR1WetdL.png" height="50" width="50" hspace="20"><a href="https://www.facebook.com/IEEEVIT1/"><img src="https://ioufinancial.com/wp-content/uploads/2017/02/facebook.png" height="50" width="50" hspace="20"></a>
    <br><br>
    <font size="2">Ask us anything about programming, meet like minded people, build projects.<br>
<center>Join the Coders Republic Group now:</font><br><br>
    <a href="https://chat.whatsapp.com/GNjVY5fSZav73fl77vGPj2"><img src="http://www.idroexpert.com/wp-content/uploads/soon-873316_960_720.png" height="50" width="50" hspace="20"></a><br><br>
    <p>For any errors in certificate<a href="https://goo.gl/forms/8dqLFOmrG3KZs65f2"> click here</a></p>
    <img src="cid:myimage" width=800 height=800 />
    <hr>
    </body>
    </html>
    """%names
    part2 = MIMEText(html, 'html')
    #body = MIMEText('<H1>Greetings %s!</H1><p><h4>Thanks for attending Introduction to PYTHON and Image processing With OpenCV Workshop.<br><br>We hope that the event was beneficial for you.<br><br>Kindly find your E-Certificate for the same, attached along with this mail.<br>We look forward to seeing you at all our future workshops, seminars and events!<br><br>Regards,<br>IEEE-VIT Student Branch<br><center><br>Follow us on<br><p><a href="https://twitter.com/vidyalankarieee?lang=en"><img src="http://icons.iconarchive.com/icons/sicons/basic-round-social/512/twitter-icon.png" height="50" width="50" hspace="20"><a href="https://www.instagram.com/ieeevit/"><img src="https://images-na.ssl-images-amazon.com/images/I/71VQR1WetdL.png" height="50" width="50" hspace="20"><a href="https://www.facebook.com/IEEEVIT1/"><img src="https://ioufinancial.com/wp-content/uploads/2017/02/facebook.png" height="50" width="50" hspace="20"></a><br><h7>click to follow<br></center><p>For any errors in certificate<a href="https://docs.google.com/forms/d/e/1FAIpQLScIov5y2i4nk6UzJMTmxW9D777GdSh2QaoTICNU7Scc9PwcOA/viewform?c=0&w=1&usp=mail_form_link"> click here</p><img src="cid:myimage" height="40" width="50"/>'%names, _subtype='html')
    msg.attach(part2)
    img = MIMEImage(img_data, 'jpg')
    img.add_header('Content-Id', '<myimage>')
    img.add_header("Content-Disposition", "inline", filename="{}.png".format(names))
    msg.attach(img)
    text = msg.as_string()
    session = smtplib.SMTP('smtp.gmail.com', 587)#server as per requirement       
    session.starttls()         
    session.login(email_sender, password)        
    session.sendmail(email_sender, email_receiver, text)         
    session.quit()

def passes(file,img,textfont):
    with open(file,'r') as csv_file:
        x=csv.reader(csv_file)
        x=csv.DictReader(csv_file)
        
        for row in x:
            image1=Image.open(img).convert('RGBA')
            # check row with the [....] heading
            names=row['Names'].upper()
            email_receiver=row['Email']
            print(email_receiver)
            txt = Image.new('RGBA', image1.size, (255,255,255,0))
            font_type = ImageFont.truetype(textfont,50)#font size
            d=ImageDraw.Draw(txt)
            x,y = image1.size
            a,b = font_type.getsize(names)
            d.text(xy = (510-a/2,315),text=names, font = font_type, fill=(255, 255, 255,255))#change 440 and 240 with desired x y positions fill=(...) is the color of font
            out = Image.alpha_composite(image1, txt)
            out.save("{}.png".format(names))
            print("{}.png".format(names))
            out.show()
            sending_mail('Your_email',email_receiver,names,'your_password')#login credentials 
passes('clean_ws1.csv','Workshop1.png','Nimbus_Mono_L_Bold.ttf')#files as per format 

