//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

string encode(string src);    
 
int main() {
	
	int T;
	cin>>T;
	while(T--)
	{
		string str;
		cin>>str;
		
		cout<<encode(str)<<endl;
	}
	return 0;
}
// } Driver Code Ends


/*You are required to complete this function */

string encode(string src)
{     
  int length = src.length();
  
  char temp = src[0];
  string result = "";
  int count = 1 , i;
  
  for ( i = 1 ; i <= length ; i++)
  {
    if (src[i] == temp)
    {
        count++;
    }
    else
    {
        result += temp + to_string(count);
        
        count = 1;
        temp = src[i];
    }
  }
  return result; 
}     
 
