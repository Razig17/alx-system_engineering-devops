# Fix the typo in the file name

exec {'Change php to phpp':
  command => 'mv class-wp-locale.php class-wp-locale.phpp',
  cwd     => '/var/www/html/wp-includes',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
