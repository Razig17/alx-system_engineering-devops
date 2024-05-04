# Creates a file in /tmp named school

file {'/tmp/school':
      ensure  => 'file',
      content => 'I love Puppet',
      owner   => 'www-data',
      group   => 'www-data',
      mode    => '0644',
}
