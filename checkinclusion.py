#Importing sys for command line inputs
#Importing hashlib for sha256 hash
#Importing buildmtree.py 
import hashlib
import sys
from buildmtree import encode_blocks,createTree,list_tree


file = open("merkle.trees.txt", "r")

file_lines = file.readlines()
file_line_block = file_lines[1].replace("'", "")
block = file_line_block.strip("[").strip('\n').strip(']').split(', ') 

nodes = []
nodes = encode_blocks(block)
root = createTree(nodes)
Hashed_List=list_tree(root)

#Checking block length and dividing into levels
block_length = len(block)
level2_blocklength = int(block_length/2)
level1_hashes= Hashed_List[-block_length:]
Hashed_List = Hashed_List[:len(Hashed_List)-block_length]
level2_hashes= Hashed_List[-level2_blocklength:]
Hashed_List = Hashed_List[:len(Hashed_List)-level2_blocklength]

##Taking input from command prompt
raw_blocks = sys.argv[1:]
string_raw_block = ''.join(raw_blocks)

#Encoding enetered string    
sha256 = hashlib.sha256()
sha256.update(string_raw_block.encode())
name = sha256.hexdigest()

#Checking if encoded hash matches any in the levels
if name in level1_hashes:
    hash_index = level1_hashes.index(name)
    if hash_index <= level2_blocklength:
        result_tuple = (name,level2_hashes[0],Hashed_List[0])
        result = list(result_tuple)
        print("Yes",result)
    else:
        result_tuple = (name,level2_hashes[1],Hashed_List[0])
        result = list(result_tuple)
        print("Yes",result)
        
elif name in level2_hashes:
    result_tuple = (name,Hashed_List[0])
    result = list(result_tuple)
    print("Yes",result)
    
elif name in Hashed_List:
    print("Yes",name)
else:
    print("No")


