import random
from tensorflow import keras
import numpy as np
class Single:

    def __init__(self,model=None):
 
        if model==None:
            self.model = keras.models.Sequential([
                keras.layers.Dense(5,input_shape=(5,)),
                keras.layers.Dense(2),
                keras.layers.Dense(1,activation="sigmoid")
            ])
        else:
            self.model = model

        self.model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

    
    def getJump(self,upx,upy,downx,downy,posy):
        return self.model.predict(np.array([np.array([upx,upy,downx,downy,posy])]))[0][0]>0.5

    def procreate(self):
        child = Single()
        for i_l, layer in enumerate(child.model.layers):
            for i_n, neuron in enumerate(layer.get_weights()):
                for i_w,weight in enumerate(neuron):

                    if type(weight) is np.ndarray:
                        for i_w2 in range(0,weight.size):
                            if random.random()<0.98:
                                    weight[i_w2] = self.model.layers[i_l].get_weights()[i_n][i_w][i_w2]

                    elif random.random()<0.98:
                                weight = self.model.layers[i_l].get_weights()[i_n][i_w]

        return child

    def setTime(self,time):
        self.time = time

    def getTime(self):
        return self.time

    def save(self):
        self.model.save("./save.h5")

    @staticmethod
    def load():
        return Single(model=keras.models.load_model("./save.h5"))