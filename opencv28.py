# hough transform is a popular technique to detect any shape,
# if you can represent that shape in a mathematical form.
# it can detect the shape even if it is broken or distorted a little bit
# a line in image space can be expressed with two variables(cartesian and polar co-ordinate)
# y=mx+c mc space(hough space) {vice versa space}
# r=xcos0+ysin0  r vs 0
# r is distance of line from origin
# hough algorithm
#1 edge detection
#2 mapping of edge points on hough space
#3 interpretation to yeild lines(by thresholding)
#4 conversion of infinite lines
# two methods -1 standard hough transform (hough lines method)
# -2 probabilistic hough line transform(hough lines p method)