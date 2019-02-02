#include <CImg/CImg.h>
#include <cmath>
#include <vector>
#include <tuple>

using namespace std;
using namespace cimg_library;

vector<tuple<int, int, int, int>> fractal_tree(int &i, int &ox, int &oy, int &t, int &r, double &theta, double &dtheta)
{
	if (i == 0)
		return {};
	int x0 = ox;
	int y0 = oy;
	int x = x0 + (t * cos(theta));
	int y = y0 + (t * sin(theta));

	vector<tuple<int, int, int, int>> lines;
	vector<tuple<int, int, int, int>> lineA;
	vector<tuple<int, int, int, int>> lineB;
	lines.push_back(make_tuple(x0, y0, x, y));
	lineA = fractal_tree(i-1, x, y, t * r, r, theta + dtheta, dtheta);
	lines.insert(lines.end(), lineA.begin(), lineA.end());
	lineB = fractal_tree(i-1, x, y, t * r, theta - dtheta, dtheta);
	lines.insert(lines.end(), lineB.begin(), lineB.end());

	return lines;
}

void render_fractal(int seed, int width, int height)
{
	seedf = (double)seed;
	while (seedf >= 1.0)
		seedf /= 10.0;
	double seedt = seed % ((120 + 1 - 80) + 80);
	vector<tuple<int, int, int, int>> tree_lines = fractal_tree(16, width/2, 0, seedt, seedf, 1.579708, 1.0472);

	CImg<unsigned char> image(width, height, 1, 3, 0);
	unsigned char colors[3];
	colors[0] = 0xff;
	colors[1] = 0xff;
	colors[2] = 0xff;

	CImgDisplay display(image, "Tree Fractal");

	for(auto &v : tree_lines)
		image.draw_line(get<0>(v), get<1>(v), get<2>(v), get<3>(v), colors);

	while (!display.is_closed())
		image.display(display);

}
