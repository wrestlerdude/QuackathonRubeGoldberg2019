#include <CImg/CImg.h>
#include <cmath>
#include <vector>

using namespace std;
using namespace cimg_library;

vector<tuple<int, int, int, int>> fractal_tree(CImg<unsigned char> &image, int &i, int &ox, int &oy, int &t, int &r, double &theta, double &dtheta)
{
	if (i == 0)
		return nullptr;
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