#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct TreeNode
{
    element key;
    struct TreeNode *left, *right;
} TreeNode;

TreeNode *new_node(element item)
{
    TreeNode *node = (TreeNode *)malloc(sizeof(TreeNode));
    node->key = item;
    node->left = node->right = NULL;
    return node;
}

TreeNode *search_node(TreeNode *node, element key)
{
    if (node == NULL)
        return NULL;
    if (node->key == key)
        return node;

    TreeNode *temp = search_node(node->left, key);
    if (temp != NULL)
        return temp;
    else
        return search_node(node->right, key);
}

TreeNode *insert_node(TreeNode *node, element key)
{
    if (node == NULL)
        return new_node(key);
    if (key < node->key)
        node->left = insert_node(node->left, key);
    else
        node->right = insert_node(node->right, key);

    return node;
}

void postorder(TreeNode *root)
{
    if (root != NULL)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d\n", root->key);
    }
}

int main(void)
{
    TreeNode *root = NULL;
    element key;

    while (scanf("%d", &key) != EOF)
        root = insert_node(root, key);

    postorder(root);

    return 0;
}