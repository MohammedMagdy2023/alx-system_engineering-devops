# Install flask V(2.1.0)

class { 'python':
  version => '3',
  pip     => 'present',
}

python::pip3 { 'flask':
  ensure  => '2.1.0',
  pkgname => 'Flask',
}
