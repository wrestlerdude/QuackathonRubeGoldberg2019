#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
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
	CImg<unsigned char> image(640, 480, 1, 3, 0);
	unsigned char colors[3];

	colors[0] = 0xff;
	colors[1] = 0;
	colors[2] = 0;
	CImgDisplay display(image, "Window");
	image.draw_line(0, 0, 100, 100, colors);
	while (!display.is_closed())
	{
		image.display(display);
	}

    return 0;
}
