class { 'stdlib': }

package { 'nginx':
  ensure  => 'installed',
}

file { 'index.html':
  ensure  => 'present',
  path    => '/var/www/html/',
  content => 'Hello World!',
}

file_line {'configure redirection':
  path    =>  '/etc/nginx/sites-available/default',
  after   =>  'server_name _;',
  line    =>  "\n\tlocation /redirect_me {\n\t\treturn 301 https://egytech.me;\n\t}\n",
  require => Class['stdlib'],
}

file { '404error.html':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  content => "Ceci n'est pas une page",
}

file_line { 'error404':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name_;',
  line  => "\n\terror_page 404 /404error.html;\n\tlocation = /404error.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}\n",
}
