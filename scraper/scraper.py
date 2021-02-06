from bs4 import BeautifulSoup
import requests
import csv

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify()) #prettify is a method

match = soup.title.text #only give 1st tag
match2 = soup.find('div', class_='footer') #pass in arguments to narrow it
#for match3 in soup.find_all('div', class_='article'):

#print(match)
#print(match2)
#print(match3)
    #headline = match3.h2.a.text
    #print(headline)

    #summary = match3.p.text
    #print(summary)

    #print()
source = requests.get('http://coreyms.com').text
soup2 = BeautifulSoup(source, 'lxml')
#print(soup2.prettify())

csv_file = open('scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])


for article in soup2.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_="entry-content").p.text
    print(summary)

    try:

        vid_src = article.find('iframe', class_="youtube-player")['src'] #access like dictionary
        #print(vid_src)


        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        #print(vid_id)

        yt_link = f'https://youtube.com/watch?v={vid_id}' #format strings
        print(yt_link)

    except Exception as e:
        yt_link = None

    print()

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()

"""source2 = requests.get('https://en.wikipedia.org/wiki/Dot-com_bubble').text
soup3 = BeautifulSoup(source2, 'lxml')
print(soup3.prettify())
"""

