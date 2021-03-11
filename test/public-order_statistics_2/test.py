import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import OrderStatistics


array = [99,81,71,68,55,45,34,22,11,0];
index0 = OrderStatistics(array, 0, len(array) - 1, 0);
index1 = OrderStatistics(array, 0, len(array) - 1, 1);
index2 = OrderStatistics(array, 0, len(array) - 1, 2);
index3 = OrderStatistics(array, 0, len(array) - 1, 3);
index4 = OrderStatistics(array, 0, len(array) - 1, 4);
index5 = OrderStatistics(array, 0, len(array) - 1, 5);
index6 = OrderStatistics(array, 0, len(array) - 1, 6);
index7 = OrderStatistics(array, 0, len(array) - 1, 7);
index8 = OrderStatistics(array, 0, len(array) - 1, 8);
index9 = OrderStatistics(array, 0, len(array) - 1, 9);


ofile = open('output', 'w')
ofile.write(str(index0) + " ")
ofile.write(str(index1) + " ")
ofile.write(str(index2) + " ")
ofile.write(str(index3) + " ")
ofile.write(str(index4) + " ")
ofile.write(str(index5) + " ")
ofile.write(str(index6) + " ")
ofile.write(str(index7) + " ")
ofile.write(str(index8) + " ")
ofile.write(str(index9) + " ")
ofile.close()
