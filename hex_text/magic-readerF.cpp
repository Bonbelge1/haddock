#include <iostream>
#include <fstream>
using namespace std; 

char FromHex(const string &hex) 
{ 
	return strtoul(hex.c_str(), NULL, 16); 
}

int main ()
{

fstream inputStream; 
string hexNumber; 

inputStream.open("mysterious_text.txt"); 


while (inputStream >> hexNumber)
{
cout << FromHex(hexNumber);
}

cout << endl;
inputStream.close();

return 0;
}