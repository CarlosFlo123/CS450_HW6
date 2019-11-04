'''--------------------------------------------------------------------------
Author: Carlos Flores Valero
Northwestern Polytechnic University, Fremont, CA
Date: 11/01/2019
---------------------------------------------------------------------------'''

empty = []
def is_link(s):
  return s == empty or (len(s) == 2 and is_link(s[1]))

def extend_link(s, t):
  assert is_link(s) and is_link(t)
  if s == empty:
    return t
  else:
    return  link(first(s),  extend_link(rest(s), t))

def len_link_recursive(s):
  if  s == empty:
    return 0
  return  1+len_link_recursive(rest(s))

def first(s):
  assert is_link(s), "first only applies to linked lists."
  assert s != empty, "empty linked list has no first element."
  return s[0]

def link(first, rest):
  assert is_link(rest), "rest must be a linked list."
  return [first, rest]

def rest(s):
  assert is_link(s), "rest only applies to linked lists."
  assert s != empty, "empty linked list has no rest."
  return s[1]

#1______________________________________________
def cntn_link(s, elm):
  if s == empty:
    return False
  elif first(s) == elm:
    return True
  else:
    return False or cntn_link(rest(s), elm)

cntn_link (link(1, link(2, link(3, empty))), 1)
cntn_link (link(1, link(2, link(3, empty))), 4)


#2______________________________________________
def prnt_lnk(s):
  res = '<'
  while s != empty:
    res += str(first(s)) + ' '
    s = rest(s)
  res += '>'
  return res

prnt_lnk(link(1, link(2, link(3, link(4, empty)))))


#3______________________________________________
def rvrs_lnk(s):
  res = empty
  while len_link_recursive(s) > 0:
    res = extend_link(link(first(s), empty), res)
    s = rest(s)
  return res

s = [1, [2, [3, [4, [ ] ]]]]
s = extend_link(s, [5, []])
rvrs_lnk(s)
#[4, [3, [2, [1, [ ] ]]]]   <------------------


#4______________________________________________
def srt(lnk):
  if len_link_recursive(lnk) <= 1:
    return True
  elif first(lnk) > first(rest(lnk)):
    return False
  else:
    return True and srt(rest(lnk))

lnk1 = link(1, link(2, link(3, link(4, empty))))
srt(lnk1)
lnk2 = link(1, link(3, link(2, link(4, link(5, empty)))))
srt(lnk2)
lnk3 = link(3, link(3, link(3, empty)))
srt(lnk3)


#5______________________________________________
def sum_lnk(lnk, g):
  result = 0
  while len_link_recursive(lnk) > 0:
    result += g(first(lnk))
    lnk = rest(lnk)
  return result

sqr = lambda x: x * x
dbl = lambda y: 2 * y
lnk1 = link(1, link(2, link(3, link(4, empty))))
sum_lnk (lnk1, sqr)
lnk2 = link(3, link(5, link(4, link(6, empty))))
sum_lnk (lnk2, dbl)


#6______________________________________________
def change(lnk, u, v):
  result = empty
  while len_link_recursive(lnk) > 0:
    if first(lnk) == u:
      result = extend_link(result, [v, []])
    else:
      result = extend_link(result, [first(lnk), []])
    lnk = rest(lnk)
  return  result

l = link(1, link(2, link(3, empty)))
n=change(l, 3, 1)
n
m=change(n, 1, 2)
m
change(m, 5, 1)


#7______________________________________________
def apnd(lnk, m):
  return extend_link(lnk, [m, []])

l = link(1, link(2, (link(3, empty))))
n = apnd(l, 4)
first(rest(rest(rest(n))))


#8______________________________________________
def insrt(l, elm, ind):
  result = empty
  i = 0
  tmp = len_link_recursive(l)
  while len_link_recursive(l) > 0:
    if i == ind:
      result = extend_link(result, link(elm, empty))
      i += 1
    else:
      result = extend_link(result, link(first(l), empty))
      l = rest(l)
    i += 1
  if ind > i:
    result = extend_link(result, link(elm, empty))
  return result

l = link(11, link(12, link(13, empty)))
n = insrt(l, 2019, 1)
n
m = insrt(n, 2020, 20)
m
