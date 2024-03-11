import pyap
import spacy
import warnings


warnings.filterwarnings("ignore")
def detect_address(text):
    '''This function detects address entities from a text'''
    pyap_addresses = pyap.parse(text, country='US')
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text)

    # Extract named entities (persons)
    spacy_location_entities = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return pyap_addresses, spacy_location_entities

def censor_address(text, stats):
    '''This function detects address from a text and censors them with special characters'''
    pyap_addresses, spacy_loc_entities = detect_address(text)

    for address in pyap_addresses:
        text = text.replace(str(address), 'X' * len(str(address)))
    for tag in spacy_loc_entities:
        text = text.replace(tag, 'X' * len(tag))
    stats['addresses masked'] = len(pyap_addresses) + len(spacy_loc_entities)
    
    return text, stats