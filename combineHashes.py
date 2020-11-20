import pickle

path1 = './pickledHashes.p'
path2 = '../JokerCord2/JokerCord/pickledHashes.p'
p1 = pickle.load(open(path1, 'rb'))
p2 = pickle.load(open(path2, 'rb'))

p3 = {}
for key in p1:
    p3[key] = p1[key]
    
for key in p2:
    p3[key] = p2[key]
    
pickle.dump(p3, open(path1, 'wb'))
pickle.dump(p3, open(path2, 'wb'))
