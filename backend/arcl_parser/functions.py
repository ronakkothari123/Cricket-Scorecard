import requests
from bs4 import BeautifulSoup
from classes import Batsman, Bowler
import json


def get_text(row):
    texts = []
    for item in row.find_all("td"):
        texts.append(item.text if item.text != "\xa0" else "n/a")

    return texts


def clean(row):
    ret = []
    for i in row:
        if i == 0:
            ret.append(None)

        ret.append(i)

    return ret


def bowling(row):
    return Bowler(*row[:]).to_dict()


def batting(row):
    return Batsman(*row[:]).to_dict()


def rate_wickets(row):
    ret = [{
        "rate": float(row[1])
    }, {
        "wickets": int(row[6])
    }]

    return ret


def overs(row):
    ret = [{
        "overs": row[1]
    }, {
        "total": int(row[6])
    }]

    return ret


def byes(row):
    ret = [{
        "byes": row[-2]
    }]

    return ret


def total(row):
    return []


def extras(row):
    ret = [{
        "extras": row[3]
    }]

    return ret


def parse(url):
    HANDLER = {
        "8": batting,
        "7": bowling,
        "rate": rate_wickets,
        "overs": overs,
        "byes": byes,
        "n/a": extras,
        "total": total
    }

    SPECIAL_WORDS = ["Rate", "Overs", "Byes",
                     "Total", "n/a"]  # n/a is for extras

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    inningsNumber = 1
    ret = []
    firstInnings = {}

    infos = soup.find_all("tr")

    for info in infos:
        processed = get_text(info)
        cleaned = clean(processed)
        if len(processed) <= 1:
            continue

        key = processed[0]

        if key in SPECIAL_WORDS:
            res = HANDLER[str(key).lower()](cleaned)

            for i in res:
                ret.append(i)

            if key == "Total" and inningsNumber == 1:
                inningsNumber += 1
                firstInnings = ret[:]
                ret = []
            continue

        ret.append(HANDLER[f'{len(processed)}'](cleaned))

    return json.dumps(
        {'results': {"firstInnings": firstInnings, "secondInnings": ret}})
