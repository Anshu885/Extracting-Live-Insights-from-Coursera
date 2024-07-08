import requests
from bs4 import BeautifulSoup
import pandas as pd

Course_Title=[]
Educator=[]
Rating=[]
meta_data=[]

for i in range(1, 84):
    url = f"https://www.coursera.org/search?query=courses&page={i}&sortBy=BEST_MATCH"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    course_elements = soup.find_all('h3',class_='cds-CommonCard-title css-6ecy9b')
    for name in course_elements:
        Course_Title.append(name.text)
    

    educator= soup.find_all('p',class_='cds-ProductCard-partnerNames css-vac8rf')
    for name in educator:
        Educator.append(name.text)
  

    review_tag = soup.find_all('div', class_='cds-CommonCard-ratings')
    for name in review_tag:
        Rating.append(name.text)
   

    meta = soup.find_all('div', class_='cds-CommonCard-metadata')
    for m in meta:
        meta_data.append(m.text)
   

df=pd.DataFrame({"Course Title":Course_Title,"Educator":Educator,"Rating":Rating,"meta_data":meta_data})
print(df)
df.to_csv("coursera.csv",index=False)