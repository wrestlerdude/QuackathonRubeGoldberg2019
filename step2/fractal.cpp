#include "CImg/CImg.h"
#include <cmath>
#include <cstdlib>

using namespace std;
using namespace cimg_library;

typedef pair<int,int> pos;

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
			if (c % 3 == 0)
				image(i, j , 1) = 0xff;
		}
}

void render_fractal(int seed, int width, int height)
{
	CImg<unsigned char> image(width, height, 1, 3, 0);
	CImgDisplay display(image, "Fractal");
	pattern(image, (double)seed);
	while (!display.is_closed())
		image.display(display);
}
