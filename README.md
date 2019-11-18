# Road_Crossing_environment
envrionment to make an angent cross road with 50 other agents
## example code:     
```
def func(printer,env,speed,position):
  printer(position)
  print(speed,position)
  return(random.choice(["up","down","left","right"]))
world_road_cross(ss=func) 
```
"yp" stands for your place
```                                                    |                       Z  E  B  R  A       C  R  O  S  S  I  N  G                        |  
env[1][4]              -- -- -- -- -- -- -- -- -- -- 30 49 33 04 -- 24 44 07 -- 34 28 40 45 -- 31 12 02 41 21 17 36 -- 42 39 43 10 -- 06 25 14 -- -- -- -- -- -- -- -- -- --
env[1][3] speed[1][2]  🚚 🚗 🛵 🛵 🚲 -- -- 🚗 🏍 🚕 🛵 -- 🚕 -- 🚚 🚗 🚲 -- 🚲 🚲 🚗 🚕 🏍 🏍 -- 🚌 -- -- 🚚 🚚 -- -- -- 🚚 🚗 🏍 -- 🚲 🚚 🚲 🚌 🚕 -- 🚚 -- -- 🚌 🛵 -- 🛵
env[1][2] speed[1][1]  🛵 🚌 🚌 -- 🚲 🛵 🚲 🚌 -- -- -- -- 🚕 🚌 🚗 -- -- -- -- -- -- 🛵 🏍 🚲 🛵 -- 🏍 -- -- 🛵 -- -- 🚗 -- -- 🏍 🏍 🛵 🏍 -- 🚕 🚚 🚚 -- 🚚 -- -- -- 🚌 🚲
env[1][1] speed[1][0]  🚲 -- -- -- 🚚 🚲 🚗 -- 🚚 -- -- 🚲 🏍 🚗 🏍 🏍 -- 🚲 -- 🚗 🚌 -- 🚲 🚲 🏍 🛵 -- 🚲 🚗 -- 🚗 -- -- 🏍 🚗 🚌 🛵 🛵 -- 🛵 🚲 🏍 -- -- 🚗 🚲 -- 🏍 -- 🚚
env[1][0]              -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
env[0][0]              -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
env[0][1] speed[0][0]  -- 🏍 🚲 🚲 🚕 🚌 -- 🚲 🚚 🚲 🏍 🏍 🏍 -- 🛵 🛵 -- -- -- 🏍 -- 🛵 -- 🛵 -- -- 🚗 🏍 🏍 🚚 -- 🚚 🛵 -- -- 🚕 -- 🚕 🚚 🚕 -- 🚕 🚗 🚌 🚌 🚲 -- 🚚 🚗 🏍
env[0][2] speed[0][1] 🏍 -- -- -- -- -- 🚗 -- 🛵 🏍 🚚 -- -- 🛵 🛵 🚚 🚗 -- -- -- 🚌 -- -- -- -- 🚕 -- 🚗 🛵 -- 🛵 🚗 🚚 🚌 🚚 -- 🚌 -- -- 🚲 -- -- 🚗 -- 🚌 🚲 🛵 🚗 🚌 --
env[0][3] speed[0][2] -- 🚌 -- 🚚 -- 🛵 -- -- -- 🚲 🚌 -- 🛵 🏍 🚲 🚲 🛵 🚗 🚗 -- 🚲 -- -- 🚗 🚲 -- 🚚 -- -- 🚗 -- -- 🚲 🚌 -- 🚚 🚌 🛵 🚌 -- 🚕 🛵 🚲 -- -- 🛵 🏍 🚌 -- 🚗
env[0][4]             -- -- -- -- -- -- -- -- -- -- 01 37 05 47 32 16 -- 38 13 19 48 11 35 yp 03 29 26 -- 23 15 09 -- -- 08 27 22 -- 46 20 18 -- -- -- -- -- -- -- -- -- --    
```
The idea is to cross the road using the zebra crossing along with 50 others.⋅⋅
write a function that returns - "up" or "down" or "left" or "right" GIVEN ENVIRONMENT, SPEED OF VEHICLES IN EACH LANE, YOUR POSITION CO-ORDINATES.
*retruning anything other than the mentioned will get you killed.
*the zebra crossing extends only from env[:][:][10] to env[:][:][40].
*you take only one step at a timestep, assume the middle lane is a single lane.
*you'll die if you go outside the zebra crossing or go out of the road or collide with a fellow crosser.
