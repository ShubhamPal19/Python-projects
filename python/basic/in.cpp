#include<iostream>
using namespace std;


 
void swap(long long int *xp, long long int *yp)
{
   long long  int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void sortt(long long int arr[], int n)
{
    int i, j, maxin;
 
    
    for (i = 0; i < n-1; i++)
    {
      
        maxin = i;
        for (j = i+1; j < n; j++)
        if (arr[j] > arr[maxin])
            maxin = j;
 
        swap(&arr[maxin], &arr[i]);
    }
}
 

int main() {


	int k,n;
	long long int * ar;

	cin>>k;
	cin>>n;
	ar=new long long int[n];
	for(int i=0; i<n; i++)
	{
		cin>>ar[i];

	}

	sortt(ar,n);

	for(int i=0; i<n; i++)
	{
		cout<<ar[i]<<" ";

	}
	long long int time=0;


	for(int i=0 ; i<n ; i+= k)
	{
		time += ar[i];
	}
	cout<<time;

	return 0;
}