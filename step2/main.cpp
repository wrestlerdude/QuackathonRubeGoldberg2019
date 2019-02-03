#include <iostream>
#include <string>
#include <algorithm>
#include <cstdint>
#include <fstream>
#include "cpp-base64/base64.h"
#include "pattern.h"
#include "CImg/CImg.h"

using namespace std;
using namespace cimg_library;

int main()
{
	string encoded;
	cout << "Enter encoded rube goldberg string:\n";
	getline(cin, encoded);
	string decoded = base64_decode(encoded);
	reverse(decoded.begin(), decoded.end());

	size_t seed = 0;

	for(auto &c : decoded)
		seed += c;

	cout << "Seed: " << seed << endl;
	#ifdef DEBUG
	cout << "Decoded: " << decoded << endl;
	#endif
	//word split in half, swapped, and encoded in b64
	decoded = base64_encode(reinterpret_cast<const unsigned char*>(decoded.c_str()), decoded.length());
	decoded = base64_encode(reinterpret_cast<const unsigned char*>(decoded.c_str()), decoded.length());

	#ifdef DEBUG
    cout << "Output: " + decoded << endl;
    #endif

	ofstream file("output.txt");
	if (file)
	{
		file << decoded << endl;
		file.close();
		cout << "Output written to file!" << endl;
	}
	else 
		cout << "Unable to open the file." << endl;

	render_pattern(seed, 1280, 720, decoded);
    return 0;
}
