#!/usr/bin/python
codes={}
esc_seq="test";
codes["reset"]     = esc_seq + "39;49;00m"
codes["bold"]      = esc_seq + "01m"
codes["blue"]      = esc_seq + "34;01m"
codes["green"]     = esc_seq + "32;01m"
codes["yellow"]    = esc_seq + "33;01m"
codes["red"]       = esc_seq + "31;01m"

print  codes;
print "########################################";
print  codes["red"];
