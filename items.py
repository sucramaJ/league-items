import cassiopeia as cass
from PIL import Image
import pprint

def print_item(item_dict):
    print(f"\n{item_dict['name']}:")
    for key, val in item_dict.items():
        print(f"{key}: {val}\n")

def clean_item(item_dict):
    clean_features = ['name','stats', 'plaintext', 'buildsInto', 'sanitizedDescription','gold','id','image']
    clean_item = {key: value for key, value in item_dict.items() if key in clean_features}
    return clean_item

def get_item_data():
    items_dict = {}
    items = cass.get_items(region="NA")
    item = items[110]
    item = item.to_dict()
    print_item(item)
    print('-------------')
    cleaned_item = clean_item(item)
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
