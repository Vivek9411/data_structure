// max heap
// may contain sum bugs
// heap sort added 

// max heap
// may contain sum bugs
#include<bits/stdc++.h>
using namespace std;

void insertion (vector < int >&v, int &n);
int deletion (vector < int >&v);
void arrang_heap(vector<int> &v);

int
main ()
{
  vector < int >v;
  v.push_back (-1);
  int option;
  do
    {

      cout << "main menu" << endl;
      cout << "1. inserting an new element" << endl;
      cout << "2. deletion a element" << endl;
      cout << "3. print current " << endl;
      cout << "4. sort all the current elements"<< endl; //decending order just delete all the elemets one by one and save them
      cin >> option;
      switch (option)
	{
	case 1:
	{
	  cout << "enter the number you want to insert" << endl;
	  int n;
	  cin >> n;
	  insertion (v, n);
	}
	  break;
	case 2:
	{
	  int d;
	  if(v.size()<2)
	  {
	      cout<<"heap is empty"<<endl;
	      break;
	  }
	  d = deletion (v);
	  cout << "number deleted from heap is" << d << endl;
	}
	  break;
	case 3:
	{
	  for(auto &it: v)
	  {
	      cout<<it<<" ";
	  }
	  cout<<endl;
	}
	  break;
	 case 4:
	 {
	    vector<int> temp;
	    int del =0;
	    int k = v.size();
	    for(int i =1; i<k; i++)
	    {
	        del= deletion(v);
	        temp.push_back(del);
	    }
	    cout<<"sorted array is"<<endl;
	    for(int i =0;i<temp.size();i++)
	        {
	            v.push_back(temp[i]);
	            cout<<temp[i]<<" ";
	        }
	        cout<<endl;
	        temp.clear();
	 }
	   break;
	default:
	{
	  cout << "invalid input" << endl;
	}
	  break;
	}
    }while (option != 5);
  return 0;
}


void
insertion (vector < int >&v, int &n)
{
  v.push_back (n);
  int i = v.size () - 1;
  // i is the last index
  // this i stars from 0
  // but our indexing stars from 1 so instertd -1 at oth position

  int p = i / 2;
  while (p>=1)
    {
      if (v[i] > v[p])
	{
	  swap (v[i], v[p]);
	}else
	{
	    break;
	}
      i = p;
      p=i/2;
    }
}

int
deletion (vector < int >&v)
{
  // always top element is deleted form the array
  int i = v.size () - 1;
  int deleted_element = v[1];
  v[1] = v[i]; 
  v.pop_back ();
  arrang_heap(v);
  return deleted_element;
}

void arrang_heap(vector<int> &v)
{
    if (v.size () <= 2)
    {
      return;
    }
    
    int i =1;
    
    while(2*i<=v.size()-1)
    {
        if(v[i]<v[2*i+1]|| v[i]<v[2*i])
        {
            if(v[2*i+1]>v[2*i])
            {
                swap(v[2*i+1], v[i]);
                i = 2*i+1;
            }
            else
            {
                swap(v[2*i], v[i]);
                i=2*i;
            }
        }
        else
        {
            return;
        }
    }
}
