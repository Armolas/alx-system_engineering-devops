# installs flask version 2.1.0
package { 'python3-pip':
  ensure     => installed,
}

package{ 'flask':
    name     => 'flask'
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip']
}