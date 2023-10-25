#include <bits/stdc++.h>
using namespace std;
// swap function can be used 
int find_pivot(vector<int>&v , int beg, int end)
{
    int i =beg, j=end, pivot = v[beg];
    
    while(i<j)
    {
        do{ i++; }while(v[i]<=pivot && i<end);
        
        do{ j--; }while(v[j]>pivot);
        
        if(i<j)
        {
            int temp = v[j];
            v[j] = v[i];
            v[i] = temp;
        }
        
    }
    
    v[beg] = v[j];
    v[j]= pivot;
    return j;
    
}

void quick_sort(vector<int>&v, int beg, int end)
{
    if(beg<end)
    {
        int p;
        p = find_pivot(v, beg, end);
        quick_sort(v, beg, p);
        quick_sort(v, p+1, end);
    }
}




int main()
{
    int n;
    cout<<"Enter the number of elements "<<endl;
    cin>>n;
    vector<int> arr;
    
    cout<<"Enter the elements one by one "<<endl;
    for( int i =0;i<n;i++)
    {
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }
    
    quick_sort(arr, 0, n);
    for(auto &it: arr){ cout<<it<<" "; }

    return 0;
}
