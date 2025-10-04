'''
1. create 2d array to store the positions of blocks in the grid
2. open google doc using url
3. parse for cell values and positions
4. insert cell with value and position
5. reverse grid
6. print grid
'''

import requests
from bs4 import BeautifulSoup as bs

def characterGrid(url, spaces=''):
    # 1. create a 2d array to store the positions of blocks in the grid.
    '''
    [
        ['█','▀','▀','▀'],
        ['█','▀','▀',' '],
        ['█',' ']
    ]

    █▀▀▀
    █▀▀ 
    █ 
    '''
    grid = []

    # 2. open google doc using url
    response = requests.get(url + '?embedded=true')

    # 3. parse response for cell values and positions 
    if (response.status_code == 200): 
        soup = bs(response.text, 'html.parser')
        # ...search for elements
        for row in soup.find_all("tr"):
            cells = [td.get_text(strip=True) for td in row.find_all('td')]
            if cells and cells[0] != 'x-coordinate':
        # ...handle search result
                # 4. insert cells from values and positions
                insert(grid, int(cells[0]), cells[1], int(cells[2]))
        # 5. reverse
        grid = reverseRows(grid)
        # 6. print
        printGrid(grid, spaces)
    # error handling
    else: print("❌ Failed:", response.status_code)

def printGrid(grid, spaces):
    if (len(grid) == 0): print('empty grid')
    for row in grid:
        content = ''
        for cell in row:
            content += cell + spaces
        print(content)
    print('')

def rowExists(grid, y):
    return y <= len(grid) - 1

def cellExists(grid, x, y):
    return rowExists(grid, y) and x <= len(grid[y]) - 1

def createRow(grid, y):
    if (rowExists(grid, y)): return
    createRow(grid, y - 1)
    grid.append([])

def createCell(grid, x, y):
    if (not rowExists(grid, y)): createRow(grid, y)
    if (not cellExists(grid, x, y)): createCell(grid, x-1, y)
    grid[y].append('')

def insert(grid, x, value, y):
    if (not cellExists(grid, x, y)): createCell(grid, x, y)        
    grid[y][x] = value

def remove(grid, x, y):
    grid[y][x] = ''

def reverseRows(grid):
    reverse = []
    i = len(grid) - 1
    while i > -1:
        reverse.append(grid[i])
        i -= 1
    return reverse

url = 'https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub'
characterGrid(url)
url2 = 'https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub'
characterGrid(url2)
characterGrid(url2, '    ')