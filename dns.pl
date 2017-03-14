#!perl
use strict;
use warnings;

my $dn=<>; # recibe el nombre de dominio
chomp $dn;  #elimina el espacio 
my $dns = `dig $dn | egrep 'ns'| cut  -f 1 |tail -1 | sed -e 's/.$//g'`; #optencion del ns*.*
#print $dns;
my $d = `dig "@.$dns"  $dn `; #tranferencia
print $d;
