from bs4 import BeautifulSoup
import requests, openpyxl

# creating an excel sheet to save the data after scrapping
excel = openpyxl.Workbook()
excel.sheetnames
sheet = excel.active
sheet.title = 'Top Rated Books'

# creating columns in excel sheet
sheet.append(['Rank','Name','Author','Avg. Rating', 'Count of Rating'])

# web scrapping
try:

    source = requests.get('https://www.goodreads.com/book/popular_by_date/2022')
    
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text,'html.parser')

    books = soup.find('div', class_ = "RankedBookList").find_all('article')

    for book in books:

        rank = book.find('div', class_ ='BookListItemRank').h2.text     
        name = book.find('h3', class_ = 'Text Text__title3 Text__umber').a.text
        author = book.find('div', class_ = 'ContributorLinksList').a.text
        avg_rating = book.find('span', class_ = 'Text Text__body3 Text__semibold Text__body-standard').text
        count_of_ratings = book.find('span', class_ = 'Text Text__body3 Text__subdued').text.split(' ')[0]

        print(rank, name, author, avg_rating, count_of_ratings) 
        # adding the scrapped data into the excel sheet
        sheet.append([rank, name, author, avg_rating, count_of_ratings])

except Exception as e:
    print(e)
    
# saving the excel sheet
excel.save('GoodReads Top 15 Books 2022.xlsx')



    