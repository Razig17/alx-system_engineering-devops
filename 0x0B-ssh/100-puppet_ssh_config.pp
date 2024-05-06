# Client configuration file
include stdlib


file_line { 'PasswordAuthentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^\s*PasswordAuthentication',
}

file_line { 'private key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^\s*IdentityFile',
}
