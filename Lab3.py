# CS2302
# Elijah Pele
# Lab 3
# Instructor: Diego Aguirre
# TA: Manoj Pravaka Saha
# Date last modified 11-11-2018
#
# This labs' function is to read through a file that contains numerous words and their emebdeings, then
# read a second file containg pairs of words, and calculating their similarity.

from Node import Node
from avl_tree import AVLTree
from rbt_node import RBTNode
from rb_tree import RedBlackTree

# First, each line from the file is stored in to a single element in an array.    
def read_file(file1):    
    array = []
    file = open(file1, encoding = 'utf-8')
    
    # Each word and  its emebeddings are stored in an array as a single string.
    for line in file:         
        array.append(line)
    head = create_Linked_List_from_File(array)
    return head


# Auxiliary method to read_file, the array is turned in to a linked list.
def create_Linked_List_from_File(array):    
    head = Node("")
    node = Node("")
    head = node
    
    # This array will be used to make sure we are only considering groups of alphabetic symbols that create words.
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range((len(array))):
        # The string is split among white spaces
        temp = array[i].split()
        
        # This boolean will turn to True if the given sybols create a word. 
        is_a_word = False
        
        # The element in the 0th position should represent a valid word. If it is not, we ignore it.        
        word = temp[0]
        for i in range(len(alphabet)):
            letter = word[0]
            if(letter == alphabet[i]):
                is_a_word = True
        
        # Since 'is_a_word' equals True, we assign it to a node and add it to the linked list. 
        if(is_a_word == True):
            node.word = temp[0]
            
            # The embeddings are then assigned to the nodes embedding array.
            for i in range(1, 51):
                node.embeddings[i-1] = float(temp[i])
            
            node.next = Node("")
            node = node.next 
    return head


# This recursive implementation will return the total nodes in a given tree.
def total_nodes(node):
    if(node is None):
        return 0
    left_total = total_nodes(node.left)
    right_total = total_nodes(node.right)
    return 1 + left_total + right_total 

# This recursive implementation will return the height of a given tree.
def height(node):
    if(node.left is not None and node.right is not None):   
        return 1 + max(height(node.left), height(node.right))
    elif(node.right is not None):
        return 1 + height(node.right)
    elif(node.left is not None):
        return 1 + height(node.left)
    else:
        return 1
    
# This recursive implementation will sort all the elements in a given tree
# in ascending order and then transfer 
def print_ascending_order(file, node):
    if(node is None):
        return 
    print_ascending_order(file, node.left)
    file.write(node.word)
    file.write("\n")
    print_ascending_order(file, node.right)
    
# This recursive implementation will look for all nodes at depth 'k' and write them to a file.   
def find_words_at_depth(file, node, k):
    if(node is None):
        return
    if(k == 0):
        file.write(node.word)
        file.write("\n")
    else:
        find_words_at_depth(file, node.left, k-1)
        find_words_at_depth(file, node.right, k-1)
        
# This method will calculate the similarity between two given words using their array of embeddings.        
def cosine_distance(w1, w2):
    
    dot_product = 0
    w1_magnitude = 0
    w2_magnitude = 0
   
    for i in range(50):
       
        w1_magnitude = w1_magnitude + (w1.embeddings[i]*w1.embeddings[i])
        w2_magnitude = w2_magnitude + (w2.embeddings[i]*w2.embeddings[i])
        dot_product = dot_product + (w1.embeddings[i] *w2.embeddings[i])
    
    cos_distance = dot_product/(w1_magnitude * w2_magnitude)
    return cos_distance

#This method will search an  tree for a node that matches a given input.
def find(node, word):
    if(node is None):
        return
    if(word == node.word):
        return node
    if(word > node.word):
        return find(node.right, word)
    elif(word<node.word):
        return find(node.left, word)
    
# This method will be used if the user wants to find the word similarity using an AVLTree.   
def find_similarity(node, file):
    temp1 = node
    temp2 = node
    file2 = open("smilarities_chart.txt", "w")
    
    # Will read through a file that has two words pers line.
    file = open(file, "r")
    
    # For each line, the word similarity between the two words will be calculated using the cosine distance formula.
    for line in file:
        words = line.split()
        w1 = words[0]
        w2 = words[1]
        node1 = Node("")
        node2 = Node("")
        node1 = find(temp1, w1)
        node2 = find(temp2, w2)
        
        # Cosine Distance formula.
        cos_distance = cosine_distance(node1, node2)
        
        # Once their similarities are calculated it will write the information to the file "similaritites_chart.txt"
        write_this = node1.word +" " +node2.word +" " +str(cos_distance) +"\n"
        file2.write(write_this)
    file2.close()
        
    
# This method will be used if the user wants to find the word similarity using an RedBlackTree.      
def find_similarity_RBT(node, file):
    temp1 = node
    temp2 = node
    file2 = open("similarities_chart.txt", "w")
    
    # Will read through a file that has two words pers line.
    file = open(file, "r")
    
    # For each line, the word similarity between the two words will be calculated using the cosine distance formula.
    for line in file:
        words = line.split()
        w1 = words[0]
        w2 = words[1]
        node1 = RBTNode("", None)
        node2 = RBTNode("", None)        
        node1 = find(temp1, w1)
        node2 = find(temp2, w2)
         
        # Cosine Distance formula.
        cos_distance = cosine_distance(node1, node2)
        
        # Once their similarities are calculated it will write the information to the file "similaritites_chart.txt"
        write_this = node1.word +" " +node2.word +" " +str(cos_distance) +"\n"
        file2.write(write_this)
    file2.close()
        
    
#The file is read and a linked list is created.
timeit.timeit(read_file("lab3test.txt"))
head = read_file("lab3test.txt")
choose_tree = input("If you want to use an AVL Tree, press 1. If you want to use a Red-Black Tree, press 2." +"\n")
depth = input("At what depth would you like to inspect the contents of the tree?")
depth = int(depth)

temp = head

avl_tree = AVLTree()
rb_tree = RedBlackTree()

file1 = open("ascendingOrder.txt", "w")
file2 = open("atDepth.txt", "w")
file3 = "testsimilarities.txt"

# AVL Tree implementation.
if(int(choose_tree) == 1):
    while(temp is not None):
        avl_tree.insert(temp)
        temp = temp.next
    temp = avl_tree.root
    print()
    print("Total nodes in tree = " +str(total_nodes(avl_tree.root)))
    print("Height of tree = " +str(height(avl_tree.root)))
    print_ascending_order(file1, avl_tree.root)
    find_words_at_depth(file2, avl_tree.root, depth)
    find_similarity(temp, file3)
    
    
# Red Black Tree implementation
if(int(choose_tree)==2):
    while(temp is not None):
        rb_tree.insert(temp)
        temp = temp.next
    temp = rb_tree.root
    print()
    print("Total nodes in tree = " +str(total_nodes(rb_tree.root)))    
    print("Height of tree = " +str(height(rb_tree.root)))
    print_ascending_order(file1, rb_tree.root)    
    find_words_at_depth(file2, rb_tree.root, depth)
    find_similarity_RBT(temp, file3)
    
file1.close()
file2.close()   

