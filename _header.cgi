#!/usr/bin/perl

use strict;
use CGI;
use LWP::UserAgent;

my $q = new CGI;
print $q->header(-type=>'text/plain');

my $ua = LWP::UserAgent->new;
$ua->agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:20.0) Gecko/20100101 Firefox/20.0");

my $req = HTTP::Request->new(GET => $q->param('url'));
my $res = $ua->simple_request($req);

my @body = split(/\n/, $res->as_string);
foreach my $line (@body) {
  last if ($line =~ m/^$/);
  print $line, "\n";
}

