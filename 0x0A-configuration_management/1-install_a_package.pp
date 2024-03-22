# Install Flask using pip3
exec { 'install flask':
    command => 'pip3 install flask==2.1.0',
    path    => '/usr/bin/',
    logoutput => true,
    unless  => 'pip3 show flask | grep -q "Version: 2.1.0"',
    provider => shell,
}