#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles.append('ducati')
#print(motorcycles)
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles.insert(0,'ducati')

print(motorcycles)

del  motorcycles[0]

print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)