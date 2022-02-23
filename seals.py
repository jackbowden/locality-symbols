import requests
from bs4 import BeautifulSoup
import os.path
from os import path, system

# brew install tesseract-lang
# get beautful soup, requests, fuzzywuzzy, python-Levenshtein package in the py requirements file or whatever
# incorporate this into api docker container, redeploy
# accept lower case locality, state name, then return best fuzzy search


#statename = "GA"

#states = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MP", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UM", "UT", "VA", "VI", "VT", "WA", "WI", "WV", "WY"]
states = ["CA"]

for statename in states:

    os.system("mkdir \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "\"")
    os.system("mkdir \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "/seals\"")
    os.system("mkdir \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "/flags\"")

    fuck = 0

    adict = dict()

    thechoices = []

    # if statename != "CA":
    html = requests.get(
        'https://www.crwflags.com/fotw/flags/us-' + statename + 'mun.html').text
    # else:
    #     html = requests.get(
    #     'https://www.crwflags.com/fotw/flags/us-' + statename + '.html').text

    bs = BeautifulSoup(html, features="html.parser")
    possible_links = bs.find_all('a')
    for link in possible_links:
        if link.has_attr('href') and link.attrs['href'][:3] == "us-" and path.exists("/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ").gif"):
            print(link.attrs['href'] + " is " + link.text.lower())
            fuck += 1
            adict[link.text.lower()] = link.attrs['href'][:-5]
            thechoices.append(link.text.lower())
            #thechoices.append(link.attrs['href'])
            print(str(path.exists("/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ").gif")))
            os.system("cp \"/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ").gif\" \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "/seals/" + link.text.lower() + ".gif\"")

    html = requests.get(
        'https://www.crwflags.com/fotw/flags/us-" + statename + "-in.html').text
    bs = BeautifulSoup(html, features="html.parser")
    possible_links = bs.find_all('a')
    for link in possible_links:
        if link.has_attr('href') and link.attrs['href'][:3] == "us-" and path.exists("/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ").gif"):
            if "city" not in link.text.lower():
                print(link.attrs['href'] + " is " + link.text.lower() + " city")
                adict[link.text.lower() + " city"] = link.attrs['href'][:-5]
                thechoices.append(link.text.lower() + " city")
                #thechoices.append(link.attrs['href'])
                os.system("cp \"/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ").gif\" \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "/seals/" + link.text.lower() + " city.gif\"")
            else:
                print(link.attrs['href'] + " is " + link.text.lower())
                adict[link.text.lower()] = link.attrs['href'][:-5]
                thechoices.append(link.text.lower())
                #thechoices.append(link.attrs['href'])
                os.system("cp \"/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ").gif\" \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "/seals/" + link.text.lower() + ".gif\"")
            print(str(path.exists("/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ").gif")))
            fuck += 1

    print (fuck)


    # from fuzzywuzzy import process
    # str2Match = "richmond city"
    # Ratios = process.extract(str2Match,thechoices)
    # print(Ratios)
    # # You can also select the string with the highest matching percentage
    # highest = process.extractOne(str2Match,thechoices)
    # print(highest[0] + " " + adict.get(highest[0]))


    fuck = 0

    adict = dict()

    thechoices = []

    # if statename != "CA":
    html = requests.get(
        'https://www.crwflags.com/fotw/flags/us-' + statename + 'mun.html').text
    # else:
    #     html = requests.get(
    #     'https://www.crwflags.com/fotw/flags/us-' + statename + '.html').text
    
    bs = BeautifulSoup(html, features="html.parser")
    possible_links = bs.find_all('a')
    for link in possible_links:
        if link.has_attr('href') and link.attrs['href'][:3] == "us-" and path.exists("/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ".gif"):
            print(link.attrs['href'] + " is " + link.text.lower())
            fuck += 1
            adict[link.text.lower()] = link.attrs['href'][:-5]
            thechoices.append(link.text.lower())
            #thechoices.append(link.attrs['href'])
            print(str(path.exists("/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ".gif")))
            os.system("cp \"/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ".gif\" \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "/flags/" + link.text.lower() + ".gif\"")

    html = requests.get(
        'https://www.crwflags.com/fotw/flags/us-" + statename + "-in.html').text
    bs = BeautifulSoup(html, features="html.parser")
    possible_links = bs.find_all('a')
    for link in possible_links:
        if link.has_attr('href') and link.attrs['href'][:3] == "us-" and path.exists("/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ".gif"):
            if "city" not in link.text.lower():
                print(link.attrs['href'] + " is " + link.text.lower() + " city")
                adict[link.text.lower() + " city"] = link.attrs['href'][:-5]
                thechoices.append(link.text.lower() + " city")
                #thechoices.append(link.attrs['href'])
                os.system("cp \"/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ".gif\" \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "/flags/" + link.text.lower() + " city.gif\"")
            else:
                print(link.attrs['href'] + " is " + link.text.lower())
                adict[link.text.lower()] = link.attrs['href'][:-5]
                thechoices.append(link.text.lower())
                #thechoices.append(link.attrs['href'])
                os.system("cp \"/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ".gif\" \"/Users/jackbowden/Documents/loc-symb-work/locality-symbols/US/" + statename + "/flags/" + link.text.lower() + ".gif\"")
            print(str(path.exists("/Users/jackbowden/Documents/loc-symb-work/Flags/u/" + link.attrs['href'][:-5] + ".gif")))
            fuck += 1

    print (fuck)