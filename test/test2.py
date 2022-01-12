animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['b'].append('buffalo')
animals['c'].append('crocodile')
animals['d'] = ['donkey']
animals['d'].append('dingo')
animals['d'].append('dolphin')
def bigest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the smallest number of values associated with it
    '''
    # Your Code Here
    k=list(animals.keys())
    v=list(animals.values())
    c=0
    b=""
    for x in range(0,len(k)):
        if len(v[x])>c:
            c=len(v[x])
            b=k[x]
    return b
print(bigest(animals))