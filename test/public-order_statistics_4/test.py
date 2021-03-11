import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import OrderStatistics




array = [28,813,299,119,634,80,742,606,211,448,429,58,794,377,428,399,844,874,236,65,990,424,65,425,82,310,657,865,419,757,554,448,643,497,791,331,882,306,971,995,127,235,183,14,462,80,417,195,659,257,286,170,872,299,486,691,317,448,377,464,395,526,566,287,658,475,380,768,84,571,327,667,721,594,244,74,168,171,864,968,992,664,815,490,523,933,495,235,75,183,292,803,694,589,576,93,450,300,2,479,872,611,955,215,338,234,110,684,812,246,151,907,951,551,173,276,656,657,501,477,694,650,8,165,733,218,69,797,86,465,12,469,685,530,842,134,65,11,217,899,838,575,167,467,26,202,36,949,346,517,236,290,75,424,291,168,800,385,480,967,616,639,380,78,617,351,2,746,541,894,780,997,423,845,959,227,703,594,495,23,989,448,672,480,689,701,890,398,539,889,989,274,26,437,485,347,32,19,745,174,979,885,155,12,948,19,447,679,336,176,562,263,495,149,146,975,489,860,260,21,917,922,147,672,492,732,164,827,895,951,479,782,574,829,35,877,295,592,89,980,62,994,341,211,674,419,643,864,538,710,45,448,959,994,142,530,650,740,2,984,591,197,104,141,474,151,799,903,509,705,639,532,385,771,617,815,189,777,91,35,128,733,817,369,513,359,992,705,754,835,574,15,284,673,67,712,706,763,138,709,105,646,484,846,722,986,114,179,945,439,103,457,362,212,157,362,948,738,612,968,887,191,35,956,316,418,112,792,330,344,165,291,342,61,490,550,130,546,471,843,61,657,157,978,443,238,753,533,573,977,864,305,435,563,57,513,715,726,630,423,545,127,489,76,614,543,219,658,897,559,131,78,333,500,468,257,699,133,754,598,243,178,551,506,287,301,841,341,487,880,567,578,235,908,391,23,65,312,702,121,1000,706,794,332,97,845,100,356,204,478,765,514,355,942,887,451,85,140,821,622,293,632,235,238,405,213,842,92,195,147,564,270,984,454,79,346,528,365,464,365,431,767,668,978,404,44,754,495,590,402,347,832,270,409,594,372,27,376,120,841,5,672,360,680,596,65,788,120,146,173,784,914,196,536,6,729,64,456,723,108,525,120,84,934,7,139,378,850,903,393,495,755,481,385,524,800,284,878,114,271];
index0 = OrderStatistics(array, 0, len(array) - 1, 0);
index1 = OrderStatistics(array, 0, len(array) - 1, 50);
index2 = OrderStatistics(array, 0, len(array) - 1, 100);
index3 = OrderStatistics(array, 0, len(array) - 1, 150);
index4 = OrderStatistics(array, 0, len(array) - 1, 200);
index5 = OrderStatistics(array, 0, len(array) - 1, 250);
index6 = OrderStatistics(array, 0, len(array) - 1, 300);
index7 = OrderStatistics(array, 0, len(array) - 1, 350);
index8 = OrderStatistics(array, 0, len(array) - 1, 400);
index9 = OrderStatistics(array, 0, len(array) - 1, 450);
index10 = OrderStatistics(array, 0, len(array) - 1, 490);
index11 = OrderStatistics(array, 0, len(array) - 1, 491);
index12 = OrderStatistics(array, 0, len(array) - 1, 492);
index13 = OrderStatistics(array, 0, len(array) - 1, 493);
index14 = OrderStatistics(array, 0, len(array) - 1, 494);
index15 = OrderStatistics(array, 0, len(array) - 1, 495);
index16 = OrderStatistics(array, 0, len(array) - 1, 496);
index17 = OrderStatistics(array, 0, len(array) - 1, 497);
index18 = OrderStatistics(array, 0, len(array) - 1, 498);
index19 = OrderStatistics(array, 0, len(array) - 1, 499);
index20 = OrderStatistics(array, 0, len(array) - 1, 1);
index21 = OrderStatistics(array, 0, len(array) - 1, 2);
index22 = OrderStatistics(array, 0, len(array) - 1, 3);
index23 = OrderStatistics(array, 0, len(array) - 1, 4);


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
ofile.write(str(index10) + " ")
ofile.write(str(index11) + " ")
ofile.write(str(index12) + " ")
ofile.write(str(index13) + " ")
ofile.write(str(index14) + " ")
ofile.write(str(index15) + " ")
ofile.write(str(index16) + " ")
ofile.write(str(index17) + " ")
ofile.write(str(index18) + " ")
ofile.write(str(index19) + " ")
ofile.write(str(index20) + " ")
ofile.write(str(index21) + " ")
ofile.write(str(index22) + " ")
ofile.write(str(index23) + " ")
ofile.close()
