#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

typedef struct node
{
    int data;
    struct node *left;
    struct node *right;
}sn;

struct node * root=NULL;
void insertelement (struct node *r, struct node * newnode);

int main ()
{
    int option;

    do
    {
        printf("\n\t\t main menu");
        printf("\n 1:insert an element");
        printf("\n 2:display ");
        printf("\n 3: delete ");
        printf("\n enter the option ");

        scanf("%d",&option);

        if(option ==1)
        {
            printf("\n press -1 to exit ");
            int value;
            printf("\n enter the value want to insert ");
            scanf("%d",&value);
            while(value!=-1)
            {
                struct node * newnode;
                newnode = (struct node *)malloc(sizeof(struct node));
                newnode->data=value;
                newnode->left=NULL;
                newnode->right=NULL;
                insertelement(root,newnode);
                printf("\n enter the value want to insert ");
                scanf("%d",&value);
            }
        }
        else if(option==2)
        {
            printf("\nINORDER : ");
           displayIN(root);
           printf("\nPREORDER : ");
           displayPRE(root);
           printf("\nPOSTORDER : ");
           displayPOST(root);
        }

    }while(option != 4);
}

void insertelement(struct node *r,struct node *newnode)
{
    if(root==NULL)
    {
        root=newnode;
    }
    else if(newnode->data>=r->data)
    {
        if(r->right!=NULL)
        {
            r=r->right;
            insertelement(r,newnode);
        }
        else
        {
            r->right=newnode;
        }
    }
    else if(newnode ->data<= r->data)
    {
        if(r->left!=NULL)
        {
            r=r->left;
            insertelement(r,newnode);
        }
        else
        {
            r->left=newnode;
        }
    }
}
void displayIN(struct node *node){
     if(node){
            displayIN(node->left);
            printf("%d  ",node->data);
            displayIN(node->right);
     }
}
void displayPRE(struct node *node){
     if(node!=NULL)
     {
       printf("%d  ",node->data);
       displayPRE(node->left);
       displayPRE(node->right);

     }
}
void displayPOST(struct node *node){
     if(node){
        displayPOST(node->left);
        displayPOST(node->right);
        printf("%d  ",node->data);
     }
}
