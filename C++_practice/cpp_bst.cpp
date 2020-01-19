#include<iostream>
using namespace std;

class Node
{
	int data;
	Node* left;
	Node* right;
	public:
	friend class LinkedBST;
};



class LinkedBST
{
private:
    Node* root;
public:
	LinkedBST(){root =NULL;}
	~LinkedBST(){}

	void preorderTraversal(Node *root)
	{
        if (root == NULL)
        {
            return;
        }

        cout << root->data;
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }

	void inorderTraversal(Node *root)
	{
        if (root == NULL)
        {
            return;
        }
        inorderTraversal(root->left);
        cout << root->data;
        inorderTraversal(root->right);
    }

	void postorderTraversal(Node *root)
	{
        if (root == NULL)
        {
            return;
        }
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        cout << root->data;
    }

	void addBST(Node *root,int data)
	{
    	if (data < root->data)
        {
    		if (root->left!=NULL)
    		{

    			addBST(root->left,data);
    		}
    		else
            {
    			Node *newNode=new Node();
    			newNode->data=data;
    			root->left=newNode;
    		}
    	}
    	else if (data > root->data)
        {
    		if (root->right!=NULL)
    		{

    			addBST(root->right,data);
    		}
    		else
            {
    			Node *newNode=new Node();
    			newNode->data=data;
    			root->right=newNode;
    		}
    	}
    	/*
    	else
        {
            addBST(root,data);
        }
        */
    }
    Node* returnaddress(LinkedBST t1)
    {
        return t1.root;
    }

};


int main()
{
	LinkedBST tree1;
	Node* a;
	a = tree1.returnaddress(tree1);
	//cout<<a;
	tree1.addBST(a,5);
	tree1.addBST(a,1);
    tree1.addBST(a,10);
	tree1.addBST(a,7);
	tree1.postorderTraversal(a);
}

