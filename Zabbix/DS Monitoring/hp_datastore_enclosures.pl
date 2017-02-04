use LWP::UserAgent;
use Digest::MD5 qw(md5_hex);
use XML::LibXML;
# generate MD5 hash using default username/password
my $md5_data = "manage_!manage";
my $md5_hash = md5_hex( $md5_data );
print "$md5_hash\n";
# create the URL and send an http GET request
$ua = LWP::UserAgent->new;
$url = 'http://ip/api/login/' . $md5_hash;
print ("Sending to $url\n");
$req = HTTP::Request->new(GET => $url);
$res = $ua->request($req);
# Parse the XML content using LibXML to obtain the session key
print $res->content;
my $parser = XML::LibXML->new();
my $doc = $parser->parse_string( $res->content );
my $root = $doc->getDocumentElement;
my @objects = $root->getElementsByTagName('OBJECT');
my @props = $objects[0]->getElementsByTagName('PROPERTY');
my $sessionKey;
foreach my $prop ( @props ) {
 my $name = $prop->getAttribute('name');
 print "Property = " . $name . "\n";
 if( $name eq 'response' ) {
 $sessionKey = $prop->textContent;
 }
}
print "Session Key = $sessionKey\n";
# Run a sample command to obtain the disks in the system.
$url = 'http://ip/api/show/enclosures';
$req = HTTP::Request->new(GET => $url);
$req->header('sessionKey' => $sessionKey );
$req->header('dataType' => 'ipa' );
$res = $ua->request($req);
$url2 = 'http://ip/api/exit';
$req2 = HTTP::Request->new(GET => $url3);
$req2->header('sessionKey' => $sessionKey );
$req2->header('dataType' => 'api' );
$res2 = $ua->request($req2);
print $res->content;

