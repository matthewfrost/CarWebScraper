import requests, bs4, smtplib

from email.mime.text import MIMEText
from email import message

class Car:
    def __init__(self, Mileage, Link):
 #       self.Price = Price
        self.Mileage = Mileage
        self.Link = Link
            
    def getDetails(self):
        return " Mileage: " + self.Mileage + " Link: " + self.Link
        
url = requests.get('http://www.lookers.co.uk/volkswagen/used-cars/search/?condition%5B%5D=Used&distance%5B%5D=0&make%5B%5D=VOLKSWAGEN&model%5BVOLKSWAGEN%5D%5B%5D=POLO&finance%5B%5D=price&price%5Bmax%5D%5B%5D=12000&transmission%5B%5D=Manual&fuel-type%5B%5D=Petrol&engine-size%5Brange%5D%5B%5D=1-2&num-doors%5B%5D=5&registered-at%5Bmin%5D%5B%5D=1%20year&mileage%5Brange%5D%5B%5D=-5000&per_page=72&order=price')
url.raise_for_status()
html = bs4.BeautifulSoup(url.text, "html.parser")
cars = html.select('.list-item')
tsi = list()
for car in cars:
    variant = car.select('.variant')
    if(len(variant) > 0):
        if('1.2 TSI' in variant[0].getText()):
 #           price = car.select('.value')[0].text
            mileage = car.select('.mileage')[0].select('a')[0].contents[0]
            link = ('http://www.lookers.co.uk' + car.select('.mileage')[0].select('a')[0].get('href'))
            found = Car( mileage, link)
            tsi.append(found)
body = 'From: carscraper@matthewfrost.co \n Subject: Cars Found \n'
for car in tsi:
    body += car.getDetails()
    

m1 = message.Message()

m1.add_header('from','carscraper@matthewfrost.co')
m1.add_header('subject','Cars found')
m1.set_payload(body + '\n')


server.sendmail("carscraper@matthewfrost.co", "myemail", m1.as_string())
    
            
