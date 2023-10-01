#include<stdio.h>
#include<string.h>

void flag(char *li[],int val){
       	for(int i=0;i<10;i++){
		printf("%d\n",val);	
	}
}
int main(){
	char buffer[6];
	int val = 0;
	printf("Spells won't allow you to go further !!");
	gets(buffer);
	printf("%d\n",val);
	char *li[] = [redacted];
	if(val!=0){
		flag(li,val);
	}
	else{
		printf("\nMay be broken boundaries can help you to get in!");
	}
	return 0;
	
}
