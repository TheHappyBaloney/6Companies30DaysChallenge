class Solution {
public:
    int findTheWinner(int n, int k) 
    {
        vector<int> circle( n , 0 );
        int i , current = 0;
        for ( i = 0 ; i < n ; ++i )
        {
            circle[i] = i + 1;
        }
        while (circle.size() > 1)
        {
            current = (current + k - 1) % circle.size() ;
            circle.erase(circle.begin() + current );
        }
        return circle[0];
    }
};
