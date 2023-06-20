from selectorlib import  Extractor
import requests
class Temperature:



    base_url = "https://www.timeanddate.com/weather/"
    yaml_path = "temp.yaml"

    def __init__(self,country,city):
        self.city = city.replace(" ","-")
        self.country = country.replace(" ","-")

    def build_url(self):
        url = self.base_url+self.country+"/"+self.city
        return url

    def webscrping(self):
        r = requests.get(self.build_url())

        c = r.text
        e = Extractor.from_yaml_file(self.yaml_path)
        res = e.extract(c)
        temp = res['temp']
        if temp == None:
            return None
        else :
            return temp

    def get(self):
        ans = self.webscrping()
        if ans == None:
            return "sorry unable to find the location"
        t = float(ans.replace('\xa0°C',""))

        return t


temper = Temperature(country="India",city="Pal")
print(temper.get())
