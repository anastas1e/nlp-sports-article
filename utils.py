import re
import spacy
import pandas as pd

nlp = spacy.load("en_core_web_lg")
doc = nlp(open("sports_article.txt").read())


def entity_recognition(text):
    people = [ent.text.strip() for ent in text.ents if
              ent.label_ == "PERSON" and re.search(r'(([A-Z][A-Za-z]+)\s([A-Z][A-Za-z]+))', ent.text)]
    organizations = [ent.text.strip() for ent in text.ents if ent.label_ == "ORG"]
    locations = [ent.text.strip() for ent in text.ents if ent.label_ == "LOC"]
    cities = [ent.text.strip() for ent in text.ents if ent.label_ == "GPE"
              and re.search(r'[@_!#$%^&*()<>?./\|}{~:]', ent.text) is None]
    dates = [ent.text.strip() for ent in text.ents if ent.label_ == "DATE" and re.search(r'^\w+\s\w+,*\s\d+', ent.text)]

    return [people, organizations, locations, cities, dates]


def entities_to_html(arrays):
    df = pd.DataFrame.from_dict({'PLAYERS': arrays[0],
                                 'FOOTBALL CLUB': arrays[1],
                                 'AREA': arrays[2],
                                 'CITY': arrays[3],
                                 'DATE': arrays[4]}, orient='index')

    df = df.transpose()
    df.replace(to_replace=[None], value='', inplace=True)
    df_html = df.to_html("templates/results.html")
    return df_html


def main():
    dicts = entity_recognition(doc)
    entities_to_html(dicts)
