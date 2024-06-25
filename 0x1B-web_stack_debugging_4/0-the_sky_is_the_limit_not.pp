# Update ulimit value
  exec { 'update_ulimit':
    command => "/bin/sed -i 's/15/4096/' /etc/default/nginx"
  }

# Restart nginx service
  exec { 'restart_nginx':
    command  => "/etc/init.d/nginx restart"
  }
