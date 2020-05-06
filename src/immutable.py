def size(n):
    if n is None:
        return 0
    else:
        return len(n)
# def cons(head):
#     """add new element to head of the list"""
#     return Node(head)

def remove(lst, index):
    if index < 0 or index > len(lst):
        return False
    lst = list(lst)
    for i in range(index + 1, len(lst)):
        lst[i - 1] = lst[i]
    del lst[len(lst)-1]  #delete the last element
    return lst

def add(lst, index, n):
    if index < 0 or index > len(lst):
        return False
    lst = list(lst)
    if lst is None:
        return n
    else:
        lst.insert(index, n)
    return lst

def from_list(lst):
    res = []
    # for e in reversed(lst):
    for e in (lst):
        # res = add(e, 0, res)
        res.append(e)
    return res

def to_list(n):
    if n == None:
        return []
    res = []
    cur = n
    for i in range(len(n)):
        if cur[i] != None:
            res.append(cur[i])
    return res

def find(lst, n):
    if lst == None:
        return False
    lst = list(lst)
    for i in range(len(lst)):
        if lst[i] == n:
            return i
    return False

def filter(lst, filt):
    res = []
    for i in range(len(lst)):
        if type(lst[i]) != filt:
            res.append(lst[i])
    return res

def map(lst, f):
    lst = list(lst)
    for i in range(len(lst)):
        cur = lst[i]
        lst[i] = f(cur)

# def reduce(lst):


def reverse(lst):
    lst = lst[::-1]
    return lst

def mempty():
    return None

def mconcat(a, b):
    if a is None:
        return b
    tmp = reverse(a)
    res = b
    for i in range(len(tmp)):
            res = add(res, 0, tmp[i])
    return res

def iterator(lst):
    cur = lst
    def foo():
        nonlocal cur
        for i in range(len(cur)):
            tmp = cur[i]
        # if cur is None:
        #     raise StopIteration
        # tmp = cur.value
        return tmp
    return foo

class Node(object):
    def __init__(self, value):
        """node constructor"""
        self.value = value