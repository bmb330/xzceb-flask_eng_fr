"""
Translator for IBM-Watson English to French and French to English
"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['APIKEY']
VERSION = '2018-05-01'
URL = os.environ['URL']


authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)



def english_to_french(english_text):
    """
    englishToFrench
    param englishText - english text to be translated
    return - frenchText - text translated to french
    """
    result = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return get_translated_text(result)


def get_translated_text(result):
    """
    getTranslatedText
    params: result - result returned from IBM-Watson Language Translation Service
    return: returns a string of the translated text from the dictionary object
            returned from the IBM-Watson instance
    """
    return result['translations'][0]['translation']


def french_to_english(french_text):
    """
    frenchToEnglish
    params: frenchText - french text to be translated
    return: englishText - text translated to english
    """
    result = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return get_translated_text(result)
