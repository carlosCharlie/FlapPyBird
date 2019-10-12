from single import Single
import flappy
import gc

def sort(e):
        return e.getTime()

ais= [Single() for i in range(0,40)]

for i in range(0,30):
        print("-> generation "+str(i)+" <-")
        for ai in ais:
                ai.setTime(flappy.main(ai))
                print(str(ai.getTime()))

        ais.sort(key = sort, reverse=True)
        ais = ais[0:3]
        for i,ai in enumerate(ais[0:3]):
                for j in range(0,13):
                        ais.append(ai.procreate())
                        
        gc.collect()

ais[0].save()