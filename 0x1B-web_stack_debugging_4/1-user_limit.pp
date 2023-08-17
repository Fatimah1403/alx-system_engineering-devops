# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

# we increased the hard file limit for the user "holberton"

exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
