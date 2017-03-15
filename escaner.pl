#!perl
use strict;
use warnings;
use IO::Socket;

my ( $host,  $pi, $pf ) = @ARGV; #entrada de ip, puerto inicial, puerto final 
$| = 1; # autoflush
my $pa =0;
for($pa = $pi; $pa < $pf; $pa++){
  my $sockets = IO::Socket::INET->new(PeerAddr => "$host", #se crea el socket para verificar si esta el puerto activo
		                      PeerPort => "$pa", 
			              Proto => 'tcp');
  if($sockets) {
    print "El puerto $pa esta abierto\n";
  }
}


