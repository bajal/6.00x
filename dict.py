animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def howMany(aDict):
    count=0
    
    for key in aDict.keys():
        count += len(aDict[key])
        
    return count

def biggest(aDict):
    biggest=None
    tmplen=0
    for key in aDict.keys():
       # print len(aDict[key])
        if len(aDict[key])>=tmplen:
         #   biggest=aDict[key]
         tmplen=len(aDict[key])
         biggest=key
    return biggest
