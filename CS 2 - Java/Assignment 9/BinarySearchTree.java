
public class BinarySearchTree<E extends Comparable> {
    private TreeNode<E> root;

    private class TreeNode<E> {
        public E value;
        public TreeNode<E> left;
        public TreeNode<E> right;

        public TreeNode(E value) {
            this.value = value;
        }
    }


    // inserts a value into the tree (doesn't allow duplicates)
    // True if added, false if not added
    public boolean insert(E value) {
        TreeNode<E> node = new TreeNode<>(value);

        if (root == null) {
            root = node;
            return true;
        }

        TreeNode<E> parent = null;
        TreeNode<E> current = root;
        while (current != null) {
            parent = current;
            if (value.compareTo(current.value) < 0) {
                current = current.left;
            }
            else if (value.compareTo(current.value) == 0){
                return false;
            }
            else {
                current = current.right;
            }
        }
        if (value.compareTo(parent.value) < 0) {
            parent.left = node;
        }
        if (value.compareTo(parent.value) > 0) {
            parent.right = node;
        }

        return true;
    }

    // deletes a value from the tree
    // return true if deleted. if not there and not deleted return false
    public boolean remove(E value) {
        TreeNode<E> parent = null;
        TreeNode<E> node = root;

        boolean done = false;
        while (!done) {
            if (node == null) {
                return false;
            }
            if (value.compareTo(node.value) < 0) {
                parent = node;
                node = node.left;
            }
            else if (value.compareTo(node.value) > 0) {
                parent = node;
                node = node.right;
            }
            else {
                done = true;
            }
        }

        // Case for no left child
        if (node.left == null) {
            // Special case for root node
            if (parent == null) {
                root = node.right;

            }
            else { // General case for no left child
                if (value.compareTo(parent.value) < 0) {
                    parent.left = node.right;
                }
                else {
                    parent.right = node.right;
                }
            }
        }
        else { // Case for there IS a left child
            TreeNode<E> parentOfRightMost = node;
            TreeNode<E> rightMost = node.left;
            while (rightMost.right != null) {
                parentOfRightMost = rightMost;
                rightMost = rightMost.right;
            }
            node.value = rightMost.value;
            if (parentOfRightMost.right == rightMost) {
                parentOfRightMost.right = rightMost.left;
            }
            else {
                parentOfRightMost.left = rightMost.left;
            }
        }
        return true;
    }


    // true if value exists in tree
    public boolean search(E value) {
        TreeNode<E> node = root;

        while (node != null) {
            if (value.compareTo(node.value) == 0) {
                return true;
            }
            if (value.compareTo(node.value) < 0) {
                node = node.left;
            }
            else {
                node = node.right;
            }
        }
        return false;
    }


    // in-order traversal of tree, display value of each node
    //use message parameter as header/title for the traversal
    public void display(String message) {
        System.out.println(message);
        reportTree(root);
    }

    public void reportTree(TreeNode<E> node) {
        if (node == null) return;

        reportTree(node.left);
        System.out.println(node.value);
        reportTree(node.right);
    }

    // returns count of all nodes
    public int numberNodes() {
        TreeNode<E> node = root;
        return numberOfNodes(node);

    }

    public int numberOfNodes(TreeNode<E> node) {
        if (node == null) { return 0; }
        if (node.left == null && node.right == null) { return 1; }

        return 1 + numberOfNodes(node.left) + numberOfNodes(node.right);
    }

    public int numberLeafNodes() {
        return numberLeafNodes(root);
    }

    // returns number of leaf nodes
    public int numberLeafNodes(TreeNode<E> node) {
        if (node == null) { return 0; }
        if (node.left == null && node.right == null) {
            return 1;
        }


        return numberLeafNodes(node.left) + numberLeafNodes(node.right);
    }

    // Height wrapper
    public int height() {
        TreeNode<E> node = root;
        return height(node);
    }

    //return height of tree (longest path from base node)
    public int height(TreeNode<E> node) {
        if (node == null) { return -1; }

        else {

            int heightLeft = height(node.left);
            int heightRight = height(node.right);

            if (heightLeft > heightRight) { return heightLeft + 1; }
            else { return heightRight + 1; }
        }
    }

}