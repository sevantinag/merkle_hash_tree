# merkle_hash_tree
Merkle hash tree and proofs of inclusion and consistency

Design Document of programs:
The merkle tree programming assignment consists of following files: 
  1. buildmtree.py
  2. checkinclusion.py
  3. checkconsitency.py
  4. merkle.trees.txt

It is to be noted that no external code/library was used to implement merkle tree functionality.

1. buildmtree.py
  This python file is to create merkle tree. It accepts input from user through command prompt. The input would be a list of strings that are to be used to create merkle tree and converted to sha256 hashes by using the encode_blocks() function. A constructor class MerkleTree() is created to define the parameters of the merkle tree. There are other functions such
  as createTree() to create the tree using the given list items, list_tree() to create a list of the encoded tree values.
  The other elements are added in main() where the tree values are passed to merkle.trees.txt file.
2. checkinclusion.py
  This python file is to check inclusion in merkle tree. It accepts input from user through command prompt. The input would be a string that will be converted to sha256 hashes. This encoded value is then checked against the merkle tree to check if the element exists in the tree or not. If it does, then the output should include its hash and the subsequent and root hashes.
3. checkconsitency.py
  This python file is to verify consistency in merkle tree. It accepts input from user through command prompt. The input would be 2 lists of strings that are to be used encoded to sha256. A constructor class MerkleConsistencyNode () is created to define the parameters of the merkle tree. The functions like createTree(), listTree() is used to create tree for each list item and generate a flat list of the trees.
  The function createmerklefile() is used to generate merkle.trees.txt which will have the merkle tree information of both the lists.
  Finally, there is a function to verify if that the old merkle tree hash is a subset of the new merkle tree hash, and verify that the new merkle tree hash is the concatenation of the old merkle tree hash
