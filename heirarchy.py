#!python3
"""
A program that converts a linear array of parrent child
relationships to a single m-ary tree.
Assumes the data is valid in that there is only one root
"""


def print_tree(root, tab_count):
    """
    recursive function to print tree
    """
    item, subs = root
    _,name,_ = item
    for _ in range(tab_count):
        print(" ", end="")
    print(name)
    for sub in subs:
        print_tree(sub, tab_count+1)

def gen_tree(root, child_map):
    """
    recursive function to generate tree
    given map
    """
    item_id, name, parent_id = root
    my_subs = []
    if item_id in child_map:
        subs = child_map[item_id]
        for sub in subs:
            new_sub = gen_tree(sub, child_map)
            my_subs.append(new_sub)
    return (root, my_subs)

def gen_map(subs):
    """
    Generate Map
    """
    child_map = {}
    for sub in subs:
        _, _, parent_id = sub
        if parent_id in child_map:
            child_map[parent_id].append(sub)
        else:
            child_map[parent_id] = [sub]
    return child_map

count =0

if __name__ == "__main__": 
  import time
  def test_main():
    subs_ = []
    root_ = 0
    t0 = time.time()
    subs_.append((1, "AJack", 3))
    subs_.append((2, "BJack", 3))
    subs_.append((3, "Jack", 10))
    subs_.append((4, "CJack", 3))
    subs_.append((5, "Jill", 10))
    subs_.append((6, "AJill", 5))
    subs_.append((7, "BJill", 5))
    subs_.append((8, "Jose", 10))
    subs_.append((9, "Jim", 8))
    subs_.append((11, "Mary", 8))
    t2 = time.time()
    child_map = gen_map(subs_)
    #for _ in range(1000):
    tree = gen_tree((10,"John",0),child_map)
    #print_tree(tree, 0)
    t1 = time.time()
    total = t1-t0
    print("t1 = ", t2-t0)
    print("t1 = ", t1-t2)

  def gen_data(root, level):
    if (level >=5):
      return root
    (name, subs) = root
    for j in range (4):
      children = []
      new_name = name + str(j)
      subs.append(gen_data((new_name, children ), level +1))
    return root

  def out_data(root, parent):
    global count
    name,subs = root
    count = count +1
    id = count
    for sub in subs:
      out_data(sub,id )
    print(id, ",", name, ",", parent)  


  #out_data(gen_data(("Jack", []), 0),0)

  #test_main()  
  def test_main2(file_name):
    import csv
    subs_ = []
    t0 = time.time()
    with open(file_name, newline='') as csvfile:
      hreader = csv.reader(csvfile)
      for row in hreader:
        id = int(row[0])
        name = str(row[1])
        name = name.strip()
        parent = int(row[2])
        subs_.append((id,name,parent))
    t2 = time.time()
    child_map = gen_map(subs_)
    tree = gen_tree(child_map[0][0], child_map)
    t1 = time.time()

    print("t2 = ", 1000000*(t2-t0))
    print("t1 = ", 1000000*(t1-t2)) 
  test_main2("heirarchy.dat")        