# Create file with puppet
file{'/tmp/school':
  ensure => 'present'
  mode => '0744',
  owner => 'www-data',
  content =>'I love Puppet',
}
