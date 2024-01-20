# install flask from pip3

package {'flask':
    ensure   => 'flask',
    provider => 'pip3',
}
