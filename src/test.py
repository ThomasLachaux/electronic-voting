import copy

a = {'A': 1, 'B': 2}

def set(a):
  a = copy.deepcopy(a)
  a['A'] = 4

set(a)
print(a)
