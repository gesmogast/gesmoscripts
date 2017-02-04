#!/usr/bin/perl
use strict;
use warnings;
use Getopt::Std;
use Data::Dumper;
use Sys::Syslog qw(:standard :macros);
 
my %options=();
getopts('c:d:e:i:j:l:n:r:s:t:MDO',\%options);
