#include "CImg/CImg.h"
#include <cmath>
#include <cstdlib>
#include <string>

using namespace cimg_library;
using namespace std;

void pattern(CImg<unsigned char> &image, double seed)
{
	srand(time(NULL));
	for (int i = 0; i < image.width(); i++)
		for (int j = 0; j < image.height(); j++)
		{ 

			double x = i*seed/image.width();
			double y = j*seed/image.height();
			int c = (int)trunc(x*x + y*y);
			if (c % 2 == 0)
				image(i, j, 0) = 0xff;
			else if (c % 3 == 0)
				image(i, j, 1) = 0xff;
			else if (c % 5 == 2)
				image(i, j, 2) = 0xff;
		}
}

void render_pattern(int seed, int width, int height, string output)
{
	CImg<unsigned char> image(width, height, 1, 3, 0);
	CImgDisplay display(image, "Pattern");
	pattern(image, (double)seed);

	unsigned char black[3] = {0};
	unsigned char white[3] = {255};

	image.draw_text(15, 670, output.c_str(), white, black, 1, 40);
	while(!display.is_closed())
		image.display(display);
}
