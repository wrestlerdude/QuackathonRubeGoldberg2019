#include <iostream>
#include <string>
#include <algorithm>
#include <cstdint>
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
	cout << decoded << "\n";

	size_t seed = 0;

	for(auto &c : decoded)
		seed += c;

	cout << seed << endl;
	
	render_fractal(seed, 640, 480);

    return 0;
}
