//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
class Solution{
public:
    vector<int> findTwoElement(vector<int> arr, int n) {
        int temp[n] = {}, res[2] = {0 , 0};
        int r = -1, i , m = -1;
        
        for ( i = 0 ; i < n ; i++ )
        {
            temp[ arr[i] - 1 ]++;
            if ( temp[arr[i] - 1] > 1 )
            {
                r = arr[i];
            }
        }
        res[0] = r;
        
        for (i = 0 ; i < n ; i++)
        {
            if (temp[i] == 0)
            {
                m = i + 1;
                break;
            }
        }
        res[1] = m;
        vector<int> result( res , res + 2 );
        return result;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findTwoElement(a, n);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}
// } Driver Code Ends
