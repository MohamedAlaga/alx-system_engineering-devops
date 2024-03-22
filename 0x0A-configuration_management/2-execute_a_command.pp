#kill process name killmenow
exec { 'kill process':
    command => 'pkill -KILL killmenow',
    path    =>'/usr/bin/'
}
