# recusively make node left subtree , right subtree
#  nth root 
# prelist preorder list
# es, en range of nodes left, root, right for nth node
# d inorder dict
def make_tree(n, pre_list,es, en, d):
    if n>=len(pre_list) or es>en:
        return None
    node = TreeNode(pre_list[n])
    i = d[pre_list[n]]

    if i!=0: 
        node.left = make_tree( n+1, pre_list,es, i-1, d)
    if i<=en:
        node.right = make_tree(n+(i-es)+1,pre_list,i+1, en, d )
    return node
return make_tree(0,preorder, 0, len(inorder),d )