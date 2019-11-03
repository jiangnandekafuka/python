lst=[1,2,2,3]
lst.append(4)
print(lst)

print(lst.count(2))

mst=[6,7,8]
lst.extend(mst)
print(lst)

print(lst.index(2))

lst.insert(3,'four')
print(lst)

print(lst.pop())
print(lst)

print(lst.remove(1))
print(lst)

lst.reverse()
print(lst)


del lst[4]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

hml=['dushf','shduifhuishfu','shduhfuhsuhfudsfdf']
hml.sort(key=len)
print(hml)
