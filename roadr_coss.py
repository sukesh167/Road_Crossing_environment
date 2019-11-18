mport random


class environment:
  
  
  def __init__(self,**agents):
    
    #initialising the blank environment
    self.env=[[[None for i in range(50)]for j in range(5)]for k in range(2)]
    #initialising the road with vehicles
    self.env[0][1:4]=[[random.choice([None] * 5 + list("🚲🚗🚌🚕🏍🛵🚚")) for k in range(50)]for j in range(3)]
    self.env[1][1:4]=[[random.choice([None] * 5 + list("🚲🚗🚌🚕🏍🛵🚚")) for k in range(50)]for j in range(3)]
    #creating people crossing road
    self.crossers=[person(name,function,"alive",None,None,[None,None,None],None) for name, function in agents.items()]
    self.namlen=len(self.crossers)
    self.crossers.extend([crossing_agent("{:02d}".format(i),self.agent_func,"alive",None,None,[None,None,None],None) for i in range(self.namlen,50)])
    #putting crossers in the side walks
    l=[i.name for i in self.crossers]
    random.shuffle(l)
    self.rand_ins(self.env[0][-1],l[:25])
    self.rand_ins(self.env[1][-1],l[25:])
    #initialisng the speeds for the lanes
    self.speed=[[random.randint(1,3) for i in range(3)]for j in range(2)]
    
    #calculating positions of each crosser
    for i in self.crossers:
        i.initial_position=self.position(i.name)
        i.position=i.initial_position
        i.final_position[1]=i.initial_position[1]
        i.final_position[0]=(1-i.initial_position[0])

  
  #randomizing side walk position of crossers
  def rand_ins(self,lst, seq):
    ins_loc = random.sample(range(10,40), len(seq))
    ins = dict(zip(ins_loc, seq))
    input = iter(lst)
    lst[:] = [ins[pos] if pos in ins else next(input)
              for pos in range(len(lst))]
  
  
  #crossing function for agents
  def agent_func(self,*args):
    return(random.choice(["up","down","left","right"]))
    
  
  #calculating position
  def position(self,name):
    for i in range(len(self.env)):
      for j in range(len(self.env[i])):
        for k in range(len(self.env[i][j])):
          if self.env[i][j][k]==name:
            return([i,j,k])
  
  
  #changing the environment for a single timestep
  def change(self):
    for i in range(2):
      for j in range(3):
        for k in range(1,self.speed[i][j]+1):
          self.env[i][j+1].pop(k-1)
          self.env[i][j+1].append(random.choice([None] * 5 + list("🚲🚗🚌🚕🏍🛵🚚")))
  
  
  def left_check(self,pos,i):
    if (pos[2]-1) >= 10: 
      if self.env[pos[0]][pos[1]][pos[2]-1]==None:
        i.position[2]-=1
      else:
        i.state="is dead"
    else:
      i.state="is not on zebra crossing"
          
  def right_check(self,pos,i):
    if (pos[2]+1) < 40:  
      if self.env[pos[0]][pos[1]][pos[2]+1]==None:
        i.position[2]+=1
      else:
        i.state="is dead"
    else:
      i.state="is not on zebra crossing"
       
  def up_check(self,pos,i):
    try:
      if pos[0]==0:
        if pos[1]==0 and self.env[1-pos[0]][pos[1]+1][pos[2]]==None:
          i.position[0]=1-i.position[0]
          i.position[1]+=1
        elif pos[1]!=0 and self.env[pos[0]][pos[1]-1][pos[2]]==None:
          i.position[1]-=1
        else:
          i.state="is dead"
      elif pos[0]==1:
        if self.env[pos[0]][pos[1]+1][pos[2]]==None:
          i.position[1]+=1
        else:
          i.state="is dead" 
    except:
      i.state="is out of the road"
        
  def down_check(self,pos,i):
    try:
      if pos[0]==1:
        if pos[1]==0 and self.env[1-pos[0]][pos[1]+1][pos[2]]==None:
          i.position[0]=1-i.position[0]
          i.position[1]+=1
        elif pos[1]!=0 and self.env[pos[0]][pos[1]-1][pos[2]]==None:
          i.position[1]-=1
        else:
          i.state="is dead"
      elif pos[0]==0:
        if self.env[pos[0]][pos[1]+1][pos[2]]==None:
          i.position[1]+=1
        else:
          i.state="is dead"
    except:
      i.state="is out of the road"
          
    
  #moving the environment
  def check(self):
    for i in self.crossers:
      self.env[i.initial_position[0]][i.initial_position[1]][i.initial_position[2]]=None
      if i.state=="alive":
        i.choice=i.func_name(self.pr,self.env,self.speed,i.position)
      if i.position[0]==i.final_position[0] and i.position[1]==i.final_position[1]:
          i.state="has crossed"
      if i.state!="alive" and i.state!="has crossed":
        self.env[i.position[0]][i.position[1]][i.position[2]]=None
         
    self.change()  
    
    for j in self.crossers:
      if j.state=="alive":
        pos=j.position
        if j.initial_position[0]==0:
          if j.choice=="up":
            self.up_check(pos,j)

          elif j.choice=="down":
            self.down_check(pos,j)
              
          elif j.choice=="left":
            self.left_check(pos,j)  
                
          elif j.choice=="right":
            self.right_check(pos,j)
          
          else:
            j.state="has not made a right choice"
            
        if j.initial_position[0]==1:        
          if j.choice=="down":
            self.up_check(pos,j)
            
          if j.choice=="up":
            self.down_check(pos,j)
              
          elif j.choice=="right":
            self.left_check(pos,j)
            
          elif j.choice=="left":
            self.right_check(pos,j)
          
          else:
            j.state="has not made a right choice"

      
#      if i.function is True and i.state=="alive":
#        pos=i.position
#        if i.initial_position[1]==4:
#          if i.position[1]==0:
#            i.initial_position=i.position
#            break
#          else:
#            if self.env[pos[0]][pos[1]-1][pos[2]]==None:
#              i.position[1]=i.position-1
#            else:
#              i.state="dead"
#        if i.initial_position[1]==0:
#          if self.env[pos[0]][pos[1]+1][pos[2]]==None:
#            i.position[1]=i.position-1
#          else:
#            i.state="dead"
#    self.change()
    
    
  def pr(self,pos):
    env1=self.env[1-pos[0]]
    env2=self.env[pos[0]]
    [print('#',end="  ") for i in range(50)]
    print("\n")
    sim1 = "\n".join(
        [" ".join(["--" if pos is None else str(pos) for pos in lane[::-1]]) for lane in env1[::-1]])
    print(sim1)
    sim0 = "\n".join(
        [" ".join(["--" if pos is None else str(pos) for pos in lane]) for lane in env2])
    print(sim0)
    [print('#',end="  ") for i in range(50)]
    print("\n")
        
          
class crossing_agent:
  def __init__(self,name,func_name,state,position,initial_position,final_position,choice):
    self.name=name
    self.func_name=func_name
    self.state=state
    self.position=position
    self.initial_position=initial_position
    self.final_position=final_position
    self.choice=choice

class person(crossing_agent):
  def __init__(self,name,func_name,state,position,initial_position,final_position,choice):
    crossing_agent.__init__(self,name,func_name,state,position,initial_position,final_position,choice)
    

def world_road_cross(**agents):  
  world=environment(**agents)
  for name, function in agents.items():
    print(name, function)
  world.pr([0,0,0])
  while True:
    world.check()
    count=0
    for i in world.crossers:
      if i.state=="alive":
        count+=1
    if count==0:
      break
  world.pr([0,0,0])

