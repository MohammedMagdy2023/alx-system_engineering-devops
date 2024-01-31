# Install flask V(2.1.0)

class { 'python':
  version    => '3',
  pip        => 'present',
}

python::pip { 'flask':
  pkgname => 'Flask',
  ensure  => '2.1.0',
}
