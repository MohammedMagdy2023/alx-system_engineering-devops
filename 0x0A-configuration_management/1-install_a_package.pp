# install flask from pip3 using  Puppet

package { 'Flask':
  ensure   => 'installed',
  provider => 'pip3'
}