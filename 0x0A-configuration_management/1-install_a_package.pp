# Install flask V(2.1.0)

package{'flask':
  ensure   => 'installed',
  provider => 'pip3',
  version  => '2.1.0',
}
