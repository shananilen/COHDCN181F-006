tclsh
foreach ip {
8.8.8.8
192.168.1.1

} { ping -c 4 $ip 
}
