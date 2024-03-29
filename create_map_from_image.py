#by _gloop/gloop#5445
config_file_path = "config.json"
ages = {
    "hope" : "true",
    "sun" : "false",
    "dark" : "false",
    "tears" : "false",
    "moon" : "false",
    "chaos" : "false",
    "wonders" : "false",
    "ice" : "false",
    "ash" : "false",
    "despair" : "false"
}
laws = {
    #==Vegetation==#
    "grow_trees" : "false",
    "grow_grass" : "false",
    "vegetation_seeds" : "false",
    "vegetation_seeds" : "false",
    "biome_overgrowth" : "false",
    #==Animals==#
    "animals_spawn" : "false",
    "animals_babies" : "false",
    "peaceful_monsters" : "false",
    #==Disasters==#
    "disasters_nature" : "false",
    "disasters_other" : "false",
    #==Civilizations==#
    "angry_civilians" : "false",
    "border_stealing" : "false",
    "rebellions" : "false",
    "civ_babies" : "false",
    "civ_army" : "false",
    "kingdom_expansion" : "false",
    "civ_limit_population_100":"false",
    #==Miscellaneous==#
    "hunger" : "false",
    "old_age" : "false",
    "erosion" : "false",
    "forever_tumor_creep" : "true",
    "grow_minerals" : "false",
    "forever_lava" : "true",
}
default_config = {
    "use_explosives" : True,
    "use_grey_goo" : False,
    "use_dithering" : True,
    "use_water_bomb" : False,
    "use_snow_mountains" : False,
    "use_water" : True,
    "show_image" : False,
    "image_scale" : [576,576],
    "input_file_path" : "test.png",
    "output_file_path" : "C:\\Users\\Gabe\\AppData\\LocalLow\\mkarpenko\\WorldBox\\saves\\save6\\map.wbox",
    "laws" : laws,
    "ages" : ages, 
}
import zlib,os,json,sys
from PIL import Image

def generate_config_file():
    d={
        "use_explosives" : True,
        "use_grey_goo" : False,
        "use_dithering" : True,
        "use_water_bomb" : False,
        "use_snow_mountains" : False,
        "use_water" : True,
        "show_image" : False,
        "image_scale" : [576,576],
        "input_file_path" : "test.png",
        "output_file_path" : "map.wbox",
        "laws" : laws,
        "ages" : ages, 
    }
    with open(config_file_path,"w") as f:
        f.write(json.dumps(d,indent=4))
        print("A")

if os.path.isfile(config_file_path):
    with open(config_file_path) as f:
        data = f.read()
        if data:
            data = json.loads(data)
        else:
            data = default_config
            generate_config_file()
    use_explosives = data["use_explosives"]
    use_grey_goo = data["use_grey_goo"]
    use_dithering = data["use_dithering"]    
    use_water_bomb = data["use_water_bomb"]
    use_snow_mountains = data["use_snow_mountains"]
    use_water = data["use_water"]
    show_image = data["show_image"]
    image_scale = data["image_scale"]
    input_file_path = data["input_file_path"]
    output_file_path = data["output_file_path"]
else:
    generate_config_file()
TILE_PALETTE={
    'hills': '5b5e5c',
    'mountains': '414545',
    'soil_high:frozen_low': 'bad5d3',
    'soil_low:frozen_high': 'd3e4e3',
    'soil_high:permafrost_low': '8cacc8',
    'soil_low:permafrost_high': 'adc7dc',
    'deep_ocean:snow_sand': '9bcfcc',
    'deep_ocean:ice': 'a2cce7',
    'soil_high:tumor_low': 'ed5182',
    'soil_low:tumor_high': 'fd1863',
    'soil_high:biomass_low': '45c842',
    'soil_low:biomass_high': '41a840',
    'soil_high:pumpkin_low': '8f9339',
    'soil_low:pumpkin_high': '696c02',
    'soil_high:cybertile_low': '9ea6a3',
    'soil_low:cybertile_high': '858886',
    'deep_ocean:road': 'bc9579',
    'deep_ocean:fuse': '804a4a',
    'deep_ocean:field': 'a16238',
    'soil_high:jungle_low': '459d51',
    'soil_low:jungle_high': '1f7020',
    'soil_high:swamp_low': '4b473d',
    'soil_low:swamp_high': '443e34',
    'soil_high:wasteland_low': '7a8868',
    'soil_low:wasteland_high': '677155',
    'soil_high:desert_low': 'e5c56d',
    'soil_low:desert_high': 'e1ba5a',
    'soil_high:crystal_low': '60d8cd',
    'soil_low:crystal_high': '5ccfc4',
    'soil_high:candy_low': 'ed8ba3',
    'soil_low:candy_high': 'f0819d',
    'soil_high:lemon_low': 'cee470',
    'soil_low:lemon_high': '8acf55',
    'soil_high:grass_low': '77a542',
    'soil_low:grass_high': '536137',
    'soil_high:savanna_low': 'daa11e',
    'soil_low:savanna_high': 'c58c1a',
    'soil_high:enchanted_low': '87d566',
    'soil_low:enchanted_high': '74af52',
    'soil_high:mushroom_low': '63713f',
    'soil_low:mushroom_high': '556338',
    'soil_high:corrupted_low': '6a5268',
    'soil_low:corrupted_high': '523e50',
    'soil_high:infernal_low': '963425',
    'soil_low:infernal_high': '67362c',
    'sand': 'f2e395',
    'soil_low': 'e2934b',
    'soil_high': 'b66f3a',
    'lava0': 'fc4921',
    'lava1': 'fda800',
    'lava2': 'fdfd00',
    'lava3': 'fdfd00'
}

if use_grey_goo:
    TILE_PALETTE|={
        'grey_goo': '575b88'
    }
if use_explosives:
    TILE_PALETTE|={
        'soil_low:tnt': 'a00000',
        'soil_low:fireworks': 'b23cca',
        'soil_low:tnt_timed': '7e0000',
        'soil_low:landmine': '990000',
    }

if use_water_bomb:
    TILE_PALETTE|={
    'soil_low:water_bomb': '6d00cc',     
    }
if use_water:
    TILE_PALETTE|={
        'deep_ocean': '3370cc',
        'close_ocean': '4084e2',
        'shallow_waters': '55aef0',
        'pit_deep_ocean': '898989',
        'pit_close_ocean': 'a0a0a0',
        'pit_shallow_waters': 'c1c1c1',
        'border_water': '3370cc',
        'border_pit': '3370cc',
    }
if use_snow_mountains:
    TILE_PALETTE|={
        'hills:snow_block': 'c0cac9',
        'mountains:snow_block': 'ffffff',
    }

def hex_to_rgb(h):
    l = [int(h[i : i + 2], 16) for i in range(0, 6, 2)]
    return l
def rgb_to_hex(c):
    if len(c):
        return "".join(hex(i)[2:].rjust(2,"0") for i in c)
    return ""

tile_types,palette_colors = list(TILE_PALETTE.keys()),TILE_PALETTE.values()
palette_colors = [hex_to_rgb(i) for i in palette_colors]
palette_colors = [i for l in palette_colors for i in l]
CHUNK_SIZE = 64
def convert_image(image):
    p_img = Image.new('P', (16, 16))
    p_img.putpalette(palette_colors + [0]*(768 - len(palette_colors)))
    image = image.convert("RGB")
    image = image.resize(image_scale)
    w,h = image.size
    print(w,h)
    chunk_w,chunk_h = (w // CHUNK_SIZE),(h // CHUNK_SIZE)
    size = (chunk_w * CHUNK_SIZE,chunk_h * CHUNK_SIZE)
    image = image.resize(size)
    image = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    if use_dithering:
        dither_mode = Image.Dither.FLOYDSTEINBERG
    else:
        dither_mode = 0
    converted_image = image.quantize(palette=p_img, dither=dither_mode)
    return converted_image,chunk_w,chunk_h

world_laws = [{"name": "world_law_"+k,"boolVal":v} for k,v in laws.items()]
world_laws += [{"name": "age_"+k,"boolVal":v} for k,v in ages.items()]
def generate_map_data(tile_data):
    tiles,tile_amounts = tile_data
    map_data = {
        "saveVersion":13,
        "width":map_width,"height":map_height,
        "mapStats":{"name" : "Generated","month":4,"year":0,"worldTime":0,"deaths":0,"housesDestroyed":0,"population":0},
        "worldLaws":{ 
            "list":world_laws
        },
        "tileMap":tile_types+["mountains"]*(128-len(tile_types)),
        "tileArray":tiles,
        "tileAmounts":tile_amounts,
        "tiles" : [],
        "cities" : [],
        "actors" : [],
        "buildings" : [],
        "kingdoms" : []
    }
    return map_data

def key_in_dict_tuple(n,d):
    return n in [i[0] for i in d.keys()]
def get_index(n,d):
    if key_in_dict_tuple(n,d):
        return max([i[1] for i in d.keys() if i[0]==n])
    return 0
def progress_bar(length,n):
    amount_complete = int(n*length)
    return "#"*amount_complete+("."*(length-(amount_complete)))
def display_progress(n,total):
    print(f"{(n/total)*100:.0f}% Complete.. "+progress_bar(30,(n/total)),end=" \r")
def generate_tile_data(f):
    data = [0]+list(f.getdata())
    tiles,tile_amounts = [],[]
    current_tiles={}
    amt = 0
    previous_tile = 0
    print(f.size[0])
    for idx,tile in enumerate(reversed(data)):

        if int(idx%(len(data)/100))==0:
            display_progress(idx,len(data))

        if sum(current_tiles.values())==f.size[0]:
            tiles.append([i[0] for i in current_tiles.keys()])
            tile_amounts.append([i for i in current_tiles.values()])
            current_tiles = {}

        tile_index = get_index(tile,current_tiles)
        if tile==previous_tile:
            amt+=1
        else:
            tile_index+=1
    
        if (tile,tile_index) in current_tiles:
            current_tiles[(tile,tile_index)]+=1
        else:
            current_tiles[(tile,tile_index)]=1
        
        previous_tile=tile

    return tiles,tile_amounts

with Image.open(input_file_path) as im:
    im2,map_width,map_height = convert_image(im)
    
if show_image:  
    im2.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT).show()

tile_data = generate_tile_data(im2)
map_data = generate_map_data(tile_data)
with open("map1.wbox","wb") as f:
    f.write(zlib.compress(json.dumps(map_data).encode("utf8")))

with open(output_file_path,"wb") as f:
    f.write(zlib.compress(json.dumps(map_data).encode("utf8")))

