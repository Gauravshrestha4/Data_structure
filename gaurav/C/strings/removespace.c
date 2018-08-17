#include <stdio.h>

int main(void) {
	// your code goes here
	char str[100];
	int i,count=0;
	scanf("%[^\n]s",str);
	printf("input string is :%s\n",str);
	for(i=0;str[i];i++)
	{
		if(str[i]!=' ') 
		{
			str[count++]=str[i];
		}
	}
	str[count]='\0';
	printf("output strings is:%s",str);
	return 0;
}
