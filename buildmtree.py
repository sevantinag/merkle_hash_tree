#Importing sys for command line inputs
#Importing hashlib for sha256 hash
import sys
import hashlib



#Merkle Hash Tree Class
class MerkleTree(object):
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
            node = MerkleTree(left_child=k[0],right_child=k[1],data=newdata)
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

def encode_blocks(blocks):
  #Encoding entered list and adding nodes
    nodes = []
    for element in blocks:    
        sha256 = hashlib.sha256()
        sha256.update(element.encode())
        data_val=sha256.hexdigest()
        nodes.append(MerkleTree(data=data_val))
    return nodes
     

def main():
    #Opening txt file to contain merkle tree
    file = open("merkle.trees.txt", "w")
    
    #Taking value from command prompt and converting to list
    raw_blocks = sys.argv[1:]
    string_raw_block = "" 
    for ele in raw_blocks:  
        string_raw_block += ele
    
    new_block=string_raw_block.strip('[]')
    blocks = list(new_block.split(","))
    block_length = len(blocks)
    
    nodes = encode_blocks(blocks)
    root = createTree(nodes)
    Hashed_List=list_tree(root)
    
    #Data for merkle.tree.txt
    file.write("List of Strings:\n")
    file.write(str(blocks)+"\n")
    
    #Checking block length and dividing into levels
    level2_blocklength = int(block_length/2)
    level1_hashes= Hashed_List[-block_length:]
    Hashed_List = Hashed_List[:len(Hashed_List)-block_length]
    level2_hashes= Hashed_List[-level2_blocklength:]
    Hashed_List = Hashed_List[:len(Hashed_List)-level2_blocklength]
    
    counter = 1
    file.write("Level 1 Hashes of lists\n")
    for item in level1_hashes:
        file.write(str(counter)+": "+ item+"\n\n")
        counter += 1
    file.write("\n\n\nLevel 2 Hashes of lists\n")
    for item in level2_hashes:
        file.write(str(counter)+": "+ item+"\n\n")
        counter += 1
    file.write("\n\n\nRoot Hash \n")
    file.write(str(counter)+": "+str(Hashed_List[0])+"\n")
    
if __name__ == "__main__":
    main()