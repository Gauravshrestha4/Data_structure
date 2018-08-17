
#include <stdio.h>

int main()
{
    int i,j,n,d,ar[100000],b[100000];
    scanf("%d%d\n",&n,&d);
    for(i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    
    for(i=d;i<n;i++)
    {
        b[j++]=ar[i];
    }
    for(i=0;i<d;i++)
    {
        b[j++]=ar[i];   
    }
    for(i=0;i<n;i++)
    {
        printf("%d ",b[i]);
    }
    return 0;
}