import cassiopeia as cass
from PIL import Image
import re
import pprint

def print_item(item_dict):
    '''
    Function for printing an item in the terminal.
    '''
    print(f"\n{item_dict['name']}:")
    for key, val in item_dict.items():
        print(f"{key}: {val}\n")

def detag_text(text):
    '''
    Remove html tags from item descriptions.
    '''
    clean_re = '<.*?>'
    text = text.replace('<br>',', ')
    clean_text = re.sub(clean_re, '', text)
    print(f"{clean_text} clean text")
    return clean_text

def strip_item(item_dict):
    '''
    Strips item of any features we do not care about
    '''
    strip_features = ['name','stats', 'plaintext', 'buildsInto', 'sanitizedDescription','gold','id','image']
    stripped_item = {key: value for key, value in item_dict.items() if key in strip_features}
    stripped_item['sanitizedDescription'] = detag_text(stripped_item['sanitizedDescription'])
    return stripped_item

def get_item_data():
    '''
    Function to download item data and store it in a JSON file.
    '''
    items_dict = {}
    items = cass.get_items(region="NA")
    item = items[110]
    item = item.to_dict()
    print('-------------')
    cleaned_item = strip_item(item)
    print_item(cleaned_item)


if __name__ == "__main__":
    #items = cass.get_items(region="NA")
    #null_magic_mantle = items[110]
    #dagger = cass.Item(name="Dagger", region="NA")

    #print(items[110].gold.to_dict())
    #print_item(dagger)
    #print(dagger.stats.to_dict())
    #dagger.image.image.show()
    get_item_data()
