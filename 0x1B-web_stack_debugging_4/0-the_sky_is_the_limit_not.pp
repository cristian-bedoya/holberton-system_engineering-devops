# Fixing the number of failed requests to 0
exec { 'fix--for-nginx':
  command => "sed -i 's/15/4096/g' /etc/default/nginx; service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
