import cassiopeia as cass
from PIL import Image
import pprint

def print_item(item):
    print(f"\n{item.name}:")
    for key, val in item.to_dict().items():
        print(f"{key}: {val}")


items = cass.get_items(region="NA")
null_magic_mantle = items[110]
dagger = cass.Item(name="Dagger", region="NA")

#print(items[110].gold.to_dict())
print_item(dagger)
#print(dagger.stats.to_dict())
#dagger.image.image.show()
