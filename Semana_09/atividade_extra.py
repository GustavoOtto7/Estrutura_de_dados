from Binary_Search_Trees import BST as bst

root = bst.CreateBST()
bst.GetLeftChild(root)
bst.GetRightChild(root)
bst.Insert(root,[10, 7, 17, 2, 9, 14, 19, 8, 15])
print(root.data)