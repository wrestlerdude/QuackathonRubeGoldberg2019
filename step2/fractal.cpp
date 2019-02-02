#include "CImg/CImg.h"
#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <tuple>

using namespace std;
using namespace cimg_library;

void fractal_tree(CImg<unsigned char> &image, int order, double theta, double height, int px, int py, double angle)
{
	double trunk_r = 0.29;
	double trunk = height * trunk_r;
	double dx = trunk * cos(angle);
	double dy = trunk * sin(angle);
	double newx = px + dy;
	double newy = py + dy;

	static const unsigned char colors[3] = {0xff};
	image.draw_line(px, py, newx, newy, colors);

	if (order > 0)
	{
		double new_height = height * (1 - trunk_r);
		fractal_tree(image, order-1, theta, new_height, newx, newy, heading - theta);
		fractal_tree(image, order-1, theta, new_height, newx, newy, heading + theta);
	}
}

void render_fractal(int seed, int width, int height)
{

	CImg<unsigned char> image(width, height, 1, 3, 0);
	CImgDisplay display(image, "Tree Fractal");
	
	
	double theta = 0;
	while (!display.is_closed())
	{
		theta += 0.1;

		fractal_tree(image, theta, height * 0.9, width / 2, -(M_PI / 2));
		image.display(display);
	}
}
