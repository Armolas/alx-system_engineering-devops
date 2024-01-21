# executes a command that kills a process
exec { 'killmenow':
    command  => 'pkill killmenow',
    provider => 'shell'
}