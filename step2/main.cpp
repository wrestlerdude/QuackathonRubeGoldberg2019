#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstdint>
#include "cpp-base64/base64.h"
#include "fractal.h"

using namespace std;

int main()
{
	string encoded;
	cout << "Enter encoded rube goldberg string:\n";
	getline(cin, encoded);
	string decoded = base64_decode(encoded);
	reverse(decoded.begin(), decoded.end());
	cout << decoded << "\n";

	size_t seed = 0;

	for(auto &c : decoded)
		seed += c;

	cout << seed << endl;

    return 0;
}
