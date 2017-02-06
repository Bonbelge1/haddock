#include <iostream>
#include <fstream>
using namespace std;

char convHex(string a) 
{
    return strtoul(a.c_str(), NULL, 16);
}

int main()
{
    ifstream file("mysterious_text.txt");
    string confuseList[1];

    if (file)
    {
        string line;
        int n = 0;
        while (file)
        {
            getline(file, line);
            confuseList[n] = line;
            n++;
        }
    }
    file.close();
    
    for(int i = 0; i < confuseList[0].length(); i += 3)
    {   
        cout << convHex({confuseList[0][i], confuseList[0][i+1]});
    }
    cout << endl;
    return 0;
}

//  31 37 2f 30 31 2f 32 32 20 31 33 3a 31 30 3a 30
//  17/01/22 13:10:0