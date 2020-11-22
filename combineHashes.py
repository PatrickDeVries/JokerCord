import pickle

path1 = './pickledHashes.p'
path2 = '../../JokerCord2/JokerCord/pickledHashes.p'
path3 = '../../JokerCord/pickledHashes.p'
p1 = pickle.load(open(path1, 'rb'))
p2 = pickle.load(open(path2, 'rb'))
p3 = pickle.load(open(path3, 'rb'))

fp = {}

for key in p1:
    fp[key] = p1[key]
    
for key in p2:
    fp[key] = p2[key]
    
for key in p3:
    fp[key] = p3[key]
    
print(len(fp))

pickle.dump(fp, open(path1, 'wb'))
pickle.dump(fp, open(path2, 'wb'))
pickle.dump(fp, open(path3, 'wb'))
