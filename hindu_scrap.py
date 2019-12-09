import requests
from bs4 import BeautifulSoup
#l ="https://www.thehindu.com/search/?q=cricket&order=DESC&sort=publishdate&page=1"
#url ="https://www.thehindu.com/search/?q=cricket"
#r = requests.get(url)


#soup = BeautifulSoup(r.content, 'html.parser')

# m =soup.find_all("div",{"class":"75_1x_StoryCard mobile-padding"})
#all_inside_urls=soup.find_all("a",{"class":"story-card75x1-text"})

#urls=[]
#for inside_url in all_inside_urls :
#    data_url = inside_url["href"]
#    urls.append(data_url)

#print(urls)





def get_search_data(search_query):
    url ="https://www.thehindu.com/search/?q={}&order=DESC&sort=publishdate&page=1".format(search_query)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    all_inside_urls=soup.find_all("a",{"class":"story-card75x1-text"})
    urls=[]
    for inside_url in all_inside_urls :
        data_url = inside_url["href"]
        r = requests.get(data_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        article_title= soup.title.text
        if soup.find_all("div",{"class":"img-container picture"}):
            image_url_details=soup.find_all("div",{"class":"img-container picture"})
            image_description = image_url_details[0].picture.img["alt"]
            image_url = image_url_details[0].picture.find("source")["srcset"]
        else :
            image_url = "NA"
            image_description = "NA"
        article_intro = soup.find("h2",class_="intro")
        article_content = soup.findAll('div', id=lambda x: x and x.startswith('content-body-'))
        data = {"data_url":data_url,"article_title":article_title,"image_description":image_description,"image_url":image_url,"article_intro":str(article_intro),"article_content":str(article_content)}

        urls.append(data)
    return urls

def get_all_data():
    pass 
data = get_search_data("cricket")
#url ="https://www.thehindu.com/sport/cricket/2nd-t20i-india-look-to-seal-series-against-windies-with-improved-bowling-show/article30229912.ece"
#r = requests.get(url)
#soup = BeautifulSoup(r.content, 'html.parser')
#article_title= soup.title.text
#image_url_details=soup.find_all("div",{"class":"img-container picture"})
#image_description = image_url[0].picture.img["alt"]
#image_url = image_url[0].picture.find("img")["data-src-template"]
#article_intro = =soup.find_all("h2",class_="intro")
#article_content = =soup.find("div",id="content-body-14269002-30229912")
print(data)

