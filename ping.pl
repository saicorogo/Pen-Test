#!perl 
use warnings;
use strict;
use Net::Ping;

my @ping = qx(ping -c5 www.google.com); # ping
my $pingt = $ping[1];  # linea
my @pingt = split(/\s+/, $pingt); #ttl
my $ttl = $pingt[6];
my @ttl = split(/\=/, $ttl); #valor
my $vttl = $ttl[1];
#print $vttl;

if (($vttl > 64) && ($vttl < 129)) {
	print "\nsistema operativo:\n... Linux";
	print "\n";
}

if (($vttl > 0) && ($vttl < 65)) {
        print "\nsistema operativo:\n... Windows";
        print "\n";
}

##nota:Los rangos posiblemente sean erroneos, en las pruebas realizadas dichos rangos concuerdan, con el so. 
