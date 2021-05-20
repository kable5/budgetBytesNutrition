import requests
from bs4 import BeautifulSoup
import xlwt


def getInfo(soup):
    nut_elems = soup.find_all(class_='wprm-nutrition-label-text-nutrition-value')
    recipe = soup.find(class_='title')
    serving = soup.find(class_='wprm-nutrition-label-text-nutrition-unit')

    for nut_elem in nut_elems:
        print(nut_elem.text, end='\n' * 2)

    print(recipe.text, end='\n' * 2)

    print(serving.text, end='\n' * 2)

    wb = xlwt.Workbook()
    ws = wb.add_sheet("My Sheet")

    ws.write(0, 1, "Servings")
    ws.write(0, 2, "Calories")
    ws.write(0, 3, "Carbohydrates")
    ws.write(0, 4, "Protein")
    ws.write(0, 5, "Fat")
    ws.write(0, 6, "Sodium")
    ws.write(0, 7, "Fiber")

    ws.write(1, 0, recipe.text)
    index = 1
    for nut_elem in nut_elems:
        if index == 1:
            ws.write(1, index, nut_elem.text+' '+serving.text)
        else:
            ws.write(1, index, nut_elem.text)
        index = index + 1

    wb.save("nutritionalInfo.xls")


if __name__ == '__main__':

    URL = 'https://www.budgetbytes.com/cinnamon-pecan-cauli-oats/'
    page = requests.get(URL)
    pageSoup = BeautifulSoup(page.content, 'html.parser')
    getInfo(pageSoup)
