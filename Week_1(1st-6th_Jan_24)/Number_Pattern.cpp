//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution
{   
    public:
        string printMinNumberForPattern(string S)
        {
            int l = S.length();
            string res;
            stack<int> sarabhai;
            
            for ( int i = 0 ; i <= l ; i++ )
            {
                sarabhai.push ( i + 1 );
                
                if ( i == l || S[i] == 'I' )
                {
                    while ( !sarabhai.empty() )
                    {
                        res += to_string(sarabhai.top());
                        sarabhai.pop();
                    }
                }
            }
            return res;
        }
};


//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string S;
        cin >> S;
        Solution ob;
        cout << ob.printMinNumberForPattern(S) << endl;
    }
    return 0; 
} 

// } Driver Code Ends
