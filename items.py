import cassiopeia as cass
from PIL import Image

items = cass.get_items(region="NA")
null_magic_mantle = items[110]
dagger = cass.Item(name="Dagger", region="NA")

print(items[110].gold.to_dict())
print(dagger.gold.to_dict())
print(dagger.stats.to_dict())
dagger.image.image.show()
