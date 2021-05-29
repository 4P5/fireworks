## Generates a "box" of random fireworks.

import random
firework_result = ""

for i in range(50):
    firework_star = ""
    star_amount = random.randint(2,4)
    # star_amount = 3
    
    ## generate a firework star, varying in type, color, trail, etc. Make multiple of these and append them to the end of the "firework_star" variable, to be eventually placed in firework.
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

    ## append the current firework to a list, to be sent to the spawner
    firework_result += (firework_entity)

## spawndata for the sign, to make it easier to edit in future.
spawn_data = ("id:\"minecraft:falling_block\",BlockState:{{Name:\"minecraft:birch_sign\",Properties:{{rotation:\"0\"}}}},TileEntityData:{{Text1:'{{\"text\":\"Fireworks Box\",\"color\":\"dark_green\",\"bold\":true}}',Text2:'{{\"text\":\"Fire rate: 4/s\",\"color\":\"blue\",\"bold\":true}}',Text3:'{{\"text\":\"Unique: 75\",\"color\":\"blue\",\"bold\":true}}',Text4:'{{\"text\":\"Stars per: 1-2\",\"color\":\"blue\",\"bold\":true}}'}},Time:1,Motion:[0.0,0.1,0.0]".format())

## put all the previous data into a single /give command for a spawner.
final_spawner = ("give @p spawner{{BlockEntityTag:{{RequiredPlayerRange:100,SpawnData:{{{}}},SpawnCount:1,SpawnRange:0.1,MinSpawnDelay:5,MaxSpawnDelay:5,SpawnPotentials:[{}]}}}}".format(spawn_data,firework_result))


## open output.txt and write the final give command to there.
output = open("output.txt","w")
output.write(final_spawner)
output.close()
