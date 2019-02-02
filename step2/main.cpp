#include <iostream>
#include <string>
#include <algorithm>
#include <cstdint>
#include <fstream>
#include "cpp-base64/base64.h"
#include "fractal.h"
#include "CImg/CImg.h"
#include "fractal.h"

using namespace std;
using namespace cimg_library;

int main()
{
	string encoded;
	cout << "Enter encoded rube goldberg string:\n";
	getline(cin, encoded);
	string decoded = base64_decode(encoded);
	reverse(decoded.begin(), decoded.end());
	cout << "Decoded: " + decoded << endl;

	size_t seed = 0;

	for(auto &c : decoded)
		seed += c;

	cout << "Seed: " << seed << endl;

	//word split in half, swapped, and encoded in b64
	int length = decoded.length();
	string output1 = decoded.substr(0, (length/2));
	string output, output2;
	if (decoded.length() & 1)
	{
		output2 = decoded.substr((length/2)+1, length-1);
		output = output2 + decoded.at(length/2) + output1;
	}
	else
	{
		output2 = decoded.substr(length/2, length-1);
		output = output2 + output1;
	}

	output = base64_encode(reinterpret_cast<const unsigned char*>(output.c_str()), output.length());

	ofstream file("output.txt");
	if (file)
	{
		file << output << endl;
		file.close();
		cout << "Output written to file!" << endl;
	}
	else 
	{
		cout << "Unable to open the file." << endl;
    	return 1;
    }

	render_fractal(seed, 1280, 720, output);
    return 0;
}
