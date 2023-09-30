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

TreeNode *insert_node(TreeNode *node, element key, char left_key, char right_key)
{
    TreeNode *root = search_node(node, key);
    if (root == NULL)
        root = new_node(key);
    TreeNode *left_node = NULL, *right_node = NULL;

    if (left_key != '.')
        left_node = new_node(left_key);
    if (right_key != '.')
        right_node = new_node(right_key);

    root->left = left_node;
    root->right = right_node;

    return root;
}

void preorder(TreeNode *root)
{
    if (root != NULL)
    {
        printf("%c", root->key);
        preorder(root->left);
        preorder(root->right);
    }
}

void inorder(TreeNode *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        printf("%c", root->key);
        inorder(root->right);
    }
}

void postorder(TreeNode *root)
{
    if (root != NULL)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%c", root->key);
    }
}

int main(void)
{
    int n;
    TreeNode *root = NULL;
    char keys[3];

    scanf("%d", &n);

    scanf(" %c %c %c", &keys[0], &keys[1], &keys[2]);
    root = insert_node(root, keys[0], keys[1], keys[2]);

    while (--n)
    {
        scanf(" %c %c %c", &keys[0], &keys[1], &keys[2]);
        insert_node(root, keys[0], keys[1], keys[2]);
    }

    preorder(root);
    printf("\n");
    inorder(root);
    printf("\n");
    postorder(root);
    printf("\n");

    return 0;
}