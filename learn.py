from single import Single
import flappy
import gc

GENERATIONS = 15          
SURVIVORS = 3             #survivors per generation
CHILDREN = 5              #children per survivor
INIT_POPULATION = 40

def sort(e):
        return e.getTime()

ais= [Single() for i in range(0,INIT_POPULATION)]

for i in range(0,GENERATIONS):
        print("-> generation "+str(i)+" <-")
        for ai in ais:
                ai.setTime(flappy.main(ai))
                print(str(ai.getTime()))

        ais.sort(key = sort, reverse=True)
        ais = ais[0:SURVIVORS]
        for i,ai in enumerate(ais[0:SURVIVORS]):
                print("procreating survivor "+str(i+1))
                for j in range(0,CHILDREN):
                        ais.append(ai.procreate())
                        
        gc.collect()

ais[0].save()