#! /usr/bin/env python

while True:
	print "Dimension (mm):",
	metric = float(raw_input())
	print "metric=", metric
	imp10k = (metric * 10000) / 25.4
	print "imperial: %s * 1/10000 inch" % int(imp10k)
