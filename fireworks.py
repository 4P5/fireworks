## Generates a "box" of random fireworks.

######## CONFIG
# star_amount = 3 # how many unique firework stars per firework. This controls how long the firework will explode for, and how laggy it will be.
fire_rate = 20 # fire every n ticks (1 tick is 0.05 seconds, or 1/20th of a second.
firework_amount = 50 # how many unique fireworks to generate. At 1 per second, it would take ~50 seconds to see the same one.
########

import random
firework_result = ""

## until we have enough fireworks, begin generating a firework
for i in range(firework_amount): 
    firework_star = ""
    star_amount = random.randint(2,4)
    
    ## generate a firework star, varying in type, color, trail, etc. Make multiple of these and append them to the end of the "firework_star" variable, to be eventually placed in the firework.
    for i in range(star_amount):
        random_type = random.randint(0,4)
        random_flicker = random.randint(0,1)
        random_trail = random.randint(0,1)
        random_color = random.randint(0,16777215)
        random_fade = random.randint(0,16777215)
        firework_star += ("{{Type:{}b,Flicker:{}b,Trail:{}b,Colors:[I;{}],FadeColors:[I;{}]}},".format(random_type,random_flicker,random_trail,random_color,random_fade))

    ## generate some more random numbers. This time it's for the entity itself
    random_lifetime = random.randint(30,40)
    random_motion_x = random.uniform(-0.02,0.02)
    random_motion_z = random.uniform(-0.02,0.02)

    ## generate the entity tag. This is what the spawner will spawn. We want a lot of these. It has the explosions embedded in it.
    firework_entity = ("{{Weight:1,Entity:{{id:\"minecraft:firework_rocket\",LifeTime:{},Motion:[{},0.6,{}],FireworksItem:{{id:firework_rocket,Count:1,tag:{{Fireworks:{{Explosions:[{}]}}}}}}}}}},".format(random_lifetime,random_motion_x,random_motion_z,firework_star))

    ## append the current firework to a list, to be sent to the spawner when the loop is over
    firework_result += (firework_entity)

## spawndata for the info sign, automatically generated based on config
spawn_data = ("id:\"minecraft:falling_block\",BlockState:{{Name:\"minecraft:birch_sign\",Properties:{{rotation:\"0\"}}}},TileEntityData:{{Text1:'{{\"text\":\"Fireworks Box\",\"color\":\"dark_green\",\"bold\":true}}',Text2:'{{\"text\":\"Fire rate: {}t\",\"color\":\"blue\",\"bold\":true}}',Text3:'{{\"text\":\"Unique: {}\",\"color\":\"blue\",\"bold\":true}}',Text4:'{{\"text\":\"Stars per: {}\",\"color\":\"blue\",\"bold\":true}}'}},Time:1,Motion:[0.0,0.1,0.0]".format(fire_rate,star_amount,firework_amount))

## put all the previous data into a single /give command for a spawner.
final_spawner = ("give @p spawner{{BlockEntityTag:{{RequiredPlayerRange:100,SpawnData:{{{}}},SpawnCount:1,SpawnRange:0.1,MinSpawnDelay:{},MaxSpawnDelay:{},SpawnPotentials:[{}]}}}}".format(spawn_data,firework_result,fire_rate,fire_rate))

## open output.txt and write the final give command to there.
output = open("output.txt","w")
output.write(final_spawner)
output.close()
