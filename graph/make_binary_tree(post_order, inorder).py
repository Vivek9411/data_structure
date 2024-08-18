#n keeps the count of nth node
# post_list is post order
# ns start of left range(inorder index)
# ne end of right range (inorder index)
def make_tree(n:int, post_list:list, ns:int, ne:int,d:dict):
    if n<0 or ns>ne:
        # if all nodes are covered or no node remainng in tree 
        return None
    
    node = TreeNode(post_list[n])
    # create nth root 
    i = d[post_list[n]]
    # find position if nth root in inorder
    # as node in left of nth node form left subtree and nodes in right of nth node form right sub tree
    if i<=ne:
        # if there are uncovered node in right of nth node form right sub tree
        node.right = make_tree(n-1, post_list, i+1, ne, d)
    if i>=ns:
        # if there are uncovered node in left of nth node form left sub tree
        node.left = make_tree(n-(ne-i)-1, post_list, ns, i-1, d)
    # return nth node
    return node