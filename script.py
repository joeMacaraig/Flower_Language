from hash_map import HashMap
from flower_lib import flower_definitions

#main
flower = HashMap(len(flower_definitions))

for flowers in flower_definitions: 
    flower.assign(flowers[0], flowers[1])

print(flower.retrieve('lavender'))
print(flower.retrieve('rose'))
print(flower.retrieve('poppy'))