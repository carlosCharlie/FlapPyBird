from single import Single
import flappy

ai = Single.load()
print("Life: "+str(flappy.main(ai)))