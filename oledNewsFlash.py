import os
import json
import urllib3
from OmegaExpansion import oledExp

# Takes in details of a headline and prints it to the OLED screen
# Some basic error checking built into print ordering to prevent overwriting of text,
# and proper truncation of titles
def writeHeadline (title, time, author):
    if oledExp.driverInit() != 0:
        print 'ERROR: Could not initialize the OLED Expansion'
        return False

    oledExp.clear()

    # writes the authors at the bottom - might overflow back to page 0
    oledExp.setCursor(6,0)
    oledExp.write(author)

    # writes the headline to the screen to clear overflow from author
    oledExp.setCursor(0,0)
    oledExp.write('    ' + title) # indenting the title to look a bit better

    # writes timestamp at the end to ensure it doesn't get overwritten
    oledExp.setCursor(5,0)
    oledExp.write(time)


# creates a GET request to the newsapi /articles endpoint
# requires API key and source to be passed in, default sorts by 'latest'
def getNewsJson (apiKey, source, sortMode='latest'):
    # creates a new http
    http = urllib3.PoolManager()

    # construct the url from the data given
    url = 'https://newsapi.org/v1/articles?' + 'source=' + source + "&sortBy=" + sortMode

    # Adds your API key to the header
    headers = {
        'X-API-KEY' : apiKey
    }

    # make the actual request
    newsRequest = http.request(
        'GET',
        url,
        headers = headers
    )

    # get the data and converts it from json
    return json.loads(newsRequest.data.decode('utf-8'))


if __name__ == '__main__':

    # gets the location of this script
    dirName = os.path.dirname(os.path.abspath(__file__))

    # read the config file relative to the script location
    with open( '/'.join([dirName, 'config.json']) ) as f:
    	config = json.load(f)

    newsJson = getNewsJson (
        config['X-API-KEY'],
        config['source'],
        config['sortBy']
    )

    # isolate the first article for cleaner code
    latest = newsJson['articles'][0]

    # error checking printout
    # print (latest['title'])
    # print (latest['publishedAt'])
    # print (latest['author'])

    # sends the headline off to be written
    writeHeadline (
        latest['title'],
        latest['publishedAt'],
        latest['author']
    )
