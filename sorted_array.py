#!python3
"""
A program that converts a linear array of parrent child
relationships to a single sorted array
Assumes the data is valid in that there is only one root
"""
import SortedCollection
from operator import itemgetter
def print_tree( collection,  root, tab_count):
    """
    recursive function to print tree
    """
    item = collection[root]
    (id,name,parent) = item 
    
    for _ in range(tab_count):
        print(" ", end="")
    print(name)
    lb = collection.lower_bound(id)
    ub = collection.upper_bound(id)
    for sub in range(lb,ub):
        print_tree(collection,sub, tab_count+1)


if __name__ == "__main__": 
 
  #test_main()  
  def test_main2(file_name):
    import csv
    subs = SortedCollection.SortedCollection([],itemgetter(2))
    with open(file_name, newline='') as csvfile:
      hreader = csv.reader(csvfile)
      for row in hreader:
        id = int(row[0])
        name = str(row[1])
        name = name.strip()
        parent = int(row[2])
        subs.insert((id,name,parent))
    print_tree(subs, subs.lower_bound(0), 0)
    
  
  test_main2("../heirarchy.dat")        
