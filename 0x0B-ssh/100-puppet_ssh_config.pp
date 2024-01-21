# puppet_ssh_config.pp

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/etc/.ssh/ssh_config',
  line   => "IdentityFile ~/.ssh/school",
  match  => '^#?IdentityFile',
}

# You may need to restart the SSH service for changes to take effect
service { 'ssh':
  ensure => 'running',
  enable => true,
  require => [File_line['Turn off passwd auth'], File_line['Declare identity file']],
}