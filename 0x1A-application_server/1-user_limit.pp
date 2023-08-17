# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

# we increased the hard file limit for the user "holberton"

exec { 'increase_hard_limit_for_holberton':
  command => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase_soft_limit_for_holberton':
  command => 'sed -i "/holberton hard/s/4/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

