def rm_smallest(d):
    if not bool(d):
        return d
    counter = True

    for key, value in d.items():
        if(counter):
            minvalue = value
            minkey = key
            counter = False
        if(value < minvalue):
            minvalue = value
            minkey = key
    d.pop(minkey)

    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()