#Importing sys for command line inputs
#Importing hashlib for sha256 hash
import hashlib
import sys


#Receiving input from command lines and splitting them into 2 lists
raw_blocks = sys.argv[1:]
list1=[]
list2=[]

for ele in range(len(raw_blocks)):
    if '[' in raw_blocks[ele]:
        if ele == 0:
            list1.append(raw_blocks[ele].strip('[').strip(','))
        else:
            list2.append(raw_blocks[ele].strip('[').strip(','))
    
    elif ']' in raw_blocks[ele]:
        if raw_blocks[ele] != raw_blocks[-1]:
            list1.append(raw_blocks[ele].strip(']').strip(','))
        else:
            list2.append(raw_blocks[ele].strip(']').strip(','))
    
    elif ele<4:
        list1.append(raw_blocks[ele].strip(','))   
    
    else:
        list2.append(raw_blocks[ele].strip(','))



#Merkle Hash Tree Class
class MerkleConsistencyNode(object):
    def __init__(self,left_child=None,right_child=None,data=None):
        self.left_child = left_child
        self.right_child = right_child
        self.data = data

#Function to Create Tree using Node value
def createTree(nodes):
    list_length = len(nodes)
    if list_length == 0:
        return 0
    else:
        while list_length %2 != 0:
            nodes.extend(nodes[-1:])
            list_length = len(nodes)
            
        child_node = []
        for k in [nodes[x:x+2] for x in range(0,list_length,2)]:
            data1 = k[0].data.encode()
            data2 = k[1].data.encode()
            sha256 = hashlib.sha256()
            sha256.update(data1+data2)
            newdata = sha256.hexdigest()
            node = MerkleConsistencyNode(left_child=k[0],right_child=k[1],data=newdata)
            child_node.append(node)                  
                               
        if len(child_node) == 1:
            return child_node[0]
        else:
            return createTree(child_node)
    

#Search Tree and List Items
def list_tree(root):
    queue = []
    queue.append(root)
    hash_list_tree = []
    while(len(queue)>0):
        e = queue.pop(0)
        hash_list_tree.append(e.data)
        if e.left_child != None:
            queue.append(e.left_child)
        if e.right_child != None:
            queue.append(e.right_child)
    return hash_list_tree

#Encoding entered list1 and adding nodes
nodes_1 = []

for element in list1:    
    sha256 = hashlib.sha256()
    sha256.update(element.encode())
    data=sha256.hexdigest()
    nodes_1.append(MerkleConsistencyNode(data=data))
    
root_1 = createTree(nodes_1)
Hashed_List_1=list_tree(root_1)


#Encoding entered list2 and adding nodes
nodes_2 = []
for element in list2:    
    sha256 = hashlib.sha256()
    sha256.update(element.encode())
    data=sha256.hexdigest()
    nodes_2.append(MerkleConsistencyNode(data=data))
    
root_2 = createTree(nodes_2)
Hashed_List_2raw=list_tree(root_2)
Hashed_List_2=[]


#Removing repetitive values
for i in Hashed_List_2raw:
  if i not in Hashed_List_2:
    Hashed_List_2.append(i)


file = open("merkle.trees.txt", "w")

#Data for merkle.tree.txt
def createmerklefile(list_item, block_length, Hashed_List):
    file.write("\n\nList of Strings:\n")
    file.write(str(list_item)+"\n")
    
    #Checking block length and dividing into levels
    list_block_length = block_length % 2
    list_block_length_mod = block_length/2
    level2_blockmod = list_block_length_mod % 2

    #If blocklength gives even results    
    if ((list_block_length) == 0) and (level2_blockmod == 0):
        level2_blocklength = int(block_length/2)
        level1_hashes= Hashed_List[-block_length:]
        Hashed_List = Hashed_List[:len(Hashed_List)-block_length]
        level2_hashes= Hashed_List[-level2_blocklength:]
        Hashed_List = Hashed_List[:len(Hashed_List)-level2_blocklength]
        
        counter = 1
        file.write("\nLevel 1 Hashes of lists\n")
        for item in level1_hashes:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
        file.write("\n\nLevel 2 Hashes of lists\n")
        for item in level2_hashes:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
        file.write("\n\nRoot Hash \n")
        for item in Hashed_List:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
    
    #If blocklength gives odd results     
    elif ((list_block_length) == 0) and (level2_blockmod != 0):
        level2_blocklength = int(block_length/2)
        level1_hashes= Hashed_List[-block_length:]
        Hashed_List = Hashed_List[:len(Hashed_List)-block_length]
        level2_hashes= Hashed_List[-level2_blocklength:]
        Hashed_List = Hashed_List[:len(Hashed_List)-level2_blocklength]
        level3_hashes= Hashed_List[-2:]
        Hashed_List = Hashed_List[:len(Hashed_List)-2]
        counter = 1
        file.write("\nLevel 1 Hashes of lists\n")
        for item in level1_hashes:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
        file.write("\n\nLevel 2 Hashes of lists\n")
        for item in level2_hashes:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
        file.write("\n\nLevel 3 Hashes of lists\n")
        for item in level3_hashes:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
        file.write("\n\nRoot Hash \n")
        for item in Hashed_List:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
    else:
        level2_blocklength = int(block_length/2)+1
        level1_hashes= Hashed_List[-block_length:]
        Hashed_List = Hashed_List[:len(Hashed_List)-block_length]
        level2_hashes= Hashed_List[-level2_blocklength:]
        Hashed_List = Hashed_List[:len(Hashed_List)-level2_blocklength]
        level3_hashes= Hashed_List[-2:]
        Hashed_List = Hashed_List[:len(Hashed_List)-2]
        
        counter = 1
        file.write("\nLevel 1 Hashes of lists\n")
        for item in level1_hashes:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
        file.write("\n\nLevel 2 Hashes of lists\n")
        for item in level2_hashes:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
        file.write("\n\nLevel 3 Hashes of lists\n")
        for item in level3_hashes:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1
        file.write("\n\nRoot Hash \n")
        for item in Hashed_List:
            file.write(str(counter)+": "+ item+"\n\n")
            counter += 1

#Finding block lengths of the lists    
block_length1 = len(list1)
block_length2 = len(list2)
            
createmerklefile(list1, block_length1, Hashed_List_1)
createmerklefile(list2, block_length2, Hashed_List_2)

#Checking if first list is a subset of second list
if Hashed_List_1[0] in Hashed_List_2:
    result_tuple = (Hashed_List_1[0],Hashed_List_2[2],Hashed_List_2[0])
    result = list(result_tuple)
    print(f"Yes {result}")
else:
    print("No")
