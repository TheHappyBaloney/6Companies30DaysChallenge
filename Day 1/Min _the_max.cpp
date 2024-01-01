// 2513. Maximize the minimum of two arrays

#include <algorithm>
#include <climits>
#include <numeric>

using namespace std;

#define ll long long 
class Solution {
public:
    bool satisfy(ll d1, ll d2, ll c1, ll c2, ll mid)
    {
        ll divby01 = mid / d1 , divby02 = mid / d2;
        ll notdivby01 = mid - divby01 , notdivby02 = mid - divby02;
        ll notdivboth = mid - mid/__gcd(d1,d2);

        if (notdivby01 >= c1 && notdivby02 >= c2 && notdivboth >= c1 + c2)
        {
            return true;

        }
        return false;
    }
    int minimizeSet(int divisor1, int divisor2, int c1, int c2) 
    {
        ll ans = INT_MAX, l = 1 , h = INT_MAX;
        while (l <= h )
        {
            ll mid = l + (h-l) /2;
            if (satisfy(divisor1, divisor2, c1, c2, mid))
            {
                ans = min(ans,mid);
                h = mid - 1 ;
            }
            else
            {
                l = mid + 1;
            }
        }
        return ans;
    }
};