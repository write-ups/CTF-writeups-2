from keras.models import load_model
import numpy as np

def get_proba(ip):
       ip = np.array(ip, dtype='float32')/255
       # reshape profile as required by the trained model
       ip = ip.reshape([1,28,28,1])
       # load model
       predicted = model.predict(ip)[0][1]
       return predicted

def pack(arr):
       outstr = ""
       for x in arr:
              outstr += "0x%x"%x
       return outstr

model = load_model('./keras_model')
profile = [0 for _ in range(784)]

max_res = 0

for j in range(784):
       for i in range(0,0xFF,0x10):
              profile[j] = i
              res = get_proba(profile)
              if(max_res < res):
                     max_res = res
                     optimized_profile = pack(profile)
                     print("maximized to %2.4f"%max_res)

              if (max_res>=0.99):
                     break


# YOU CAN SUBMIT THE FAKE PROFILE AS SHOWN BELOW
# curl http://ml.ctf.nullcon.net/predict?profile=0x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x80x750xfe0xdc0x590x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00xd0x5f0xd40xfd0xfd0xfd0x9d0x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x100x5f0xd10xfd0xfd0xfd0xf50x7d0x120x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x280x600xce0xfd0xfe0xfd0xfd0xc60x400x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x2c0xb60xf00xfd0xfd0xfd0xfe0xfd0xc60x180x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00xf0x3c0x3c0xa80xfd0xfd0xfe0xc80x170x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x460xf70xfd0xfd0xf50x150x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x4b0xcf0xfd0xfd0xcf0x5c0x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x4f0xdb0xfd0xfd0xfd0x8a0x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x690xfa0xfd0xfd0xfd0x220x10x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x5f0xfe0xfe0xfe0xfe0x5e0x00x00x00x00x00x30xd0xd0xd0x80x00x00x00x00x00x00x00x00x00x00x00x00x6b0xfd0xfd0xfd0xcc0xf0x00x00x00x00x150xa60xfd0xfd0xfd0xd40x190x00x00x00x00x00x00x00x00x00x00x210xd90xfd0xfd0x840x400x00x00x120x2b0x9d0xab0xfd0xfd0xfd0xfd0xfd0xa00x20x00x00x00x00x00x00x00x00x30xa60xfd0xfd0xf20x310x110x310x9e0xd20xfe0xfd0xfd0xfd0xfd0xfd0xfd0xfd0xfd0xb0x00x00x00x00x00x00x00x00xa0xe30xfd0xfd0xcf0xf0xac0xfd0xfd0xfd0xfe0xf70xc90xfd0xd20xd20xfd0xfd0xaf0x40x00x00x00x00x00x00x00x00xa0xe40xfd0xfd0xe00x570xf20xfd0xfd0xb80x3c0x360x90x3c0x230xb60xfd0xfd0x340x00x00x00x00x00x00x00x00x00xd0xfd0xfd0xfd0xfd0xe70xfd0xfd0xfd0x5d0x560x560x560x6d0xd90xfd0xfd0x860x50x00x00x00x00x00x00x00x00x00x20x730xfd0xfd0xfd0xfd0xfd0xfd0xfd0xfd0xfe0xfd0xfd0xfd0xfd0xfd0x860x50x00x00x00x00x00x00x00x00x00x00x00x30xa60xfd0xfd0xfd0xfd0xfd0xfd0xfd0xfe0xfd0xfd0xfd0xaf0x340x50x00x00x00x00x00x00x00x00x00x00x00x00x00x70x230x840xe10xfd0xfd0xfd0xc30x840x840x840x6e0x40x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x00x0