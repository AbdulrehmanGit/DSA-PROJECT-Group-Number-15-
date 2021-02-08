import random # importing random for coin tosses
class Node():
    """A node in a skip list"""
    def __init__(self, key, height):
        self.key = key
        self.next = [None]*(height + 1)#this is to hold and manage the nodes
    def height(self):
        return len(self.next) - 1
class SkiplistSSet():
    def __init__(self):
        self.height = 0
        self.n = 0
        self.sentinel = self.new_node(None, 32) # sentinel is a dummy head at the start of the list and it has the highest height
        self.stack = [None]*(self.sentinel.height() + 1)#stack array is created in order to keep a track of nodes
    def new_node(self, key, height):
        return Node(key, height)
    def pick_height(self):# this function simulates coin tossing in order to determine the height (k) of a new node
        z = random.getrandbits(32) #this is the random integer
        k = 0 #k is the height of incoming Element
        while z & 1:
            k += 1
            z = z // 2
        return k
    def find_pred_node(self, x):
        u = self.sentinel
        r = self.height
        while r >= 0:
            while u.next[r] != None and u.next[r].x < x:#u moves to right in the express lanes
                # till there's an elemeent which is greater than u,
                # if it is greater then it moves down the list (from L(r-1 to L(r))
                u = u.next[r]  # go right in list  r
            r -= 1  # go down into list r - 1
        return u
    def find(self, x):
        u = self.find_pred_node(x)
        if u.next[0] == None:
            return None
        return u.next[0].x
    def add(self, x):
        u = self.sentinel
        r = self.height
        while r >= 0:
            while u.next[r] != None and u.next[r].key < x:# checks whether next element is greater or not
                u = u.next[r]#if greater then move down a lower level
            if u.next[r] != None and u.next[r].key == x:
                return False
            self.stack[r] = u
            r -= 1
        w = self.new_node(x, self.pick_height())#picking the height of incoming new node
        while self.height < w.height():# increasing the sentinel/stacks max height
            # if the incoming elements height becomes greater
            self.height += 1
            self.stack[self.height] = self.sentinel  # height increased
        for i in range(len(w.next)):
            w.next[i] = self.stack[i].next[i]
            self.stack[i].next[i] = w
        self.n += 1
        return True
    def remove(self, x):#remove is done in similar manner
        removed = False
        u = self.sentinel
        r = self.height
        while r >= 0:
            while u.next[r] != None and u.next[r].key < x:
                u = u.next[r]
            if u.next[r] !=  None and u.next[r].key == x:# u.next[r].key ==x then we splice the element
                removed = True
                u.next[r] = u.next[r].next[r]
                if u == self.sentinel and u.next[r] == None:
                    self.height -= 1  # height has decreased
            r -= 1
        if removed:
            self.n -= 1
        return removed
    def displayList(self):# this function prints the skip list and its levels
        print("\n*****Skip List******")
        u = self.sentinel
        for i in range(self.height + 1):
            print("Level {}: ".format(i), end=" ")
            node = u.next[i]
            while (node != None):
                print(node.key, end=" ")
                node = node.next[i]
            print("")
lst = SkiplistSSet()
lst.add(3)
lst.add(4)
lst.add(5)
lst.add(99)
lst.add(66)
lst.add(7)
lst.add(8)
lst.add(9)
lst.add(99)
lst.add(101)
lst.remove(8)
lst.displayList()