# install flask from pip3 using  Puppet

package { 'flask':
  ensure   => 'installed',
  provider => 'python3',
}