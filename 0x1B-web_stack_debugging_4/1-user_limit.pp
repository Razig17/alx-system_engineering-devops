exec { 'Change the hard limit':
  command => "sed -i '/^holberton hard nofile/s/5/4096/' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}


exec { 'Change the soft limit':
  command => "sed -i '/^holberton soft nofile/s/4/4096/' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
