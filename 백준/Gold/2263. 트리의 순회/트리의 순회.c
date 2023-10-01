#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100000

typedef int element;
typedef struct TreeNode
{
    element key;
    struct TreeNode *left, *right;
} TreeNode;

element n, pRoot, in_order[MAX_SIZE], post_order[MAX_SIZE];

TreeNode *new_node(element item)
{
    TreeNode *node = (TreeNode *)malloc(sizeof(TreeNode));
    node->key = item;
    node->left = node->right = NULL;
    return node;
}

int find_idx(int key)
{
    for (int i = 0; i < n; i++)
        if (in_order[i] == key)
            return i;
    return -1;
}

TreeNode *make_tree(int start, int end)
{
    if (start > end)
        return NULL;
    int root_value = post_order[pRoot];  // root 값
    int root_idx = find_idx(root_value); // root index 찾기

    TreeNode *root = new_node(root_value);
    pRoot--;
    root->right = make_tree(root_idx + 1, end);
    root->left = make_tree(start, root_idx - 1);

    return root;
}

void preorder(TreeNode *root)
{
    if (root != NULL)
    {
        printf("%d ", root->key);
        preorder(root->left);
        preorder(root->right);
    }
}

int main(void)
{
    TreeNode *root = NULL;

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &in_order[i]);
    for (int i = 0; i < n; i++)
        scanf("%d", &post_order[i]);

    pRoot = n - 1;
    root = make_tree(0, n - 1);
    preorder(root);

    return 0;
}