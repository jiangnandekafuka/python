def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
storage={}
init(storage)
print storage

def lookup(data,label,name):
    return  data[label].get(name)

me='magnus lie hetland'
storage['first']['magnus']=[me]
storage['middle']['lie']=[me]
storage['last']['hetland']=[me]

print lookup(storage,'middle','lie')

def store(data,full_name):
    names=full_name.split()
    if len(names)==2:names.insert(1,'')
    labels='first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name]=[full_name]
mynames={}
init(mynames)
store(mynames,'magnus lie hetland')
print lookup(mynames,'middle','lie')
