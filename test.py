import pickle

with open('backup.pickle', 'rb') as bp:
	data = pickle.load(bp)
	print('data: ', data)

#for t in data[849914042]:
print('t: ', data[849914042])