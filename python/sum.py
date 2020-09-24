def sum(lst, n):
    trans = lst
    for i in range(len(trans)-1):
        for j in range(i+1, len(trans)):
            if(trans[i]+trans[j] == n):
                return True

    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()