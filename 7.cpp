#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;

long long t[1000];
vector<long long> nums[1000];


long long do_op(long long a, long long b, int op)
{
    if(op == 0)
        return a + b;
    if(op == 1)
        return a * b;
    if(op == 2)
    {
        long long mul = 1;
        while(mul <= b)
            mul *= 10;
        return a*mul + b;
    }
    else
        return -1;
}

int main()
{
    int i = 0;
    string s;
    char tmp;
    fstream in("in");
    while(getline(in,s))
    {
        if(s.size() == 0)
            break;
        stringstream ss(s);
        nums[i].clear();
        long long a;
        ss >> a;
        nums[i].push_back(a);
        ss >> tmp;
        while(ss >> a)
        {
            nums[i].push_back(a);   
        }
        i++;
    }
    int n = i;
    long long res = 0;
    for(int i = 0; i < n; i++)
    {
        long long t = nums[i][0];
        int nops = nums[i].size() - 2;
        if(nops == 0 and t == nums[i][1])
        {
            res += t;
        }
        if(nops == -1)
            continue;
        for(int msk = 0; msk < (1<<nops); msk++)
        {
            long long val = nums[i][1];
            for(int j = 0; j < nops; j++)
            {
                int op = msk / (1<<j) % 2;
                val = do_op(val, nums[i][j+2], op);
            }
            if(val == t)
            {
                res += t;
                break;
            }
        }
    }
    cout << res << '\n';
    vector<long long> powers3;
    long long a = 1;
    while(a > 0)
    {
        powers3.push_back(a);
        a *= 3;
    }
    res = 0;
    for(int i = 0; i < n; i++)
    {
        long long t = nums[i][0];
        int nops = nums[i].size() - 2;
        if(nops == 0 and t == nums[i][1])
        {
            res += t;
        }
        if(nops == -1)
            continue;
        for(int msk = 0; msk < powers3[nops]; msk++)
        {
            long long val = nums[i][1];
            for(int j = 0; j < nops; j++)
            {
                int op = msk / powers3[j] % 3;
                val = do_op(val, nums[i][j+2], op);
            }
            if(val == t)
            {
                res += t;
                break;
            }
        }
    }
    cout << res;


}