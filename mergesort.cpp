#include <iostream>
#define MAX 11

using namespace std;

void merge_sort (int arr[], int beg, int end);
void merge (int arr[], int beg, int mid, int end);

int
main ()
{
  int n;
  cout << "Enter the number of elements " << endl;
  cin >> n;
  int arr[n] = { 0 };
  for (int i = 0; i < n; i++)
    {
      cin >> arr[i];
    }
// for (int i = 0; i < n; i++)
//     {
//       cout << arr[i] << " ";
//     }
//     cout<<arr[0]<<endl;
//     cout<<2<<endl;
//   for (int i = 0; i < n; i++)
//     {
//       cout << arr[i] << endl;;
//     }
  // sort the array 
  merge_sort (arr, 0, n - 1);

  for (int i = 0; i < n; i++)
    {
      cout << arr[i] << " ";
    }
  return 0;
}



void
merge (int arr[], int beg, int mid, int end)
{
  int temp[MAX] = { 0 };
  int j = mid + 1;
  int i = beg;
  int index = beg;

  while ((i <= mid) && (j <= end))
    {
      if (arr[i] < arr[j])
	{
	  temp[index] = arr[i];
	  i++;
	}
      else
	{
	  temp[index] = arr[j];
	  j++;
	}
      index++;
    }

  while (j <= end)
    {
      temp[index] = arr[j];
      j++;
      index++;
    }

  while (i <= mid)
    {
      temp[index] = arr[i];
      i++;
      index++;
    }

  for (int i = beg; i <= end; i++)
    {
      arr[i] = temp[i];
    }

}

void
merge_sort (int arr[], int beg, int end)
{
  int mid;
  if (beg < end)
    {
      mid = (beg + end) / 2;
      merge_sort (arr, beg, mid);
      merge_sort (arr, mid + 1, end);
      merge (arr, beg, mid, end);
    }
}
