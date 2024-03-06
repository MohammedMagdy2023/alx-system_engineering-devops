file { '/var/www/html/index.php':
  ensure => file,
  mode   => '0644',
}
