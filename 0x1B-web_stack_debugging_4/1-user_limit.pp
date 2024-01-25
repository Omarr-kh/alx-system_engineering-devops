# increase limits for holberton user

# increase hard limit
exec { 'increase-hard-limit':
  command => "sed -i '/^holberton hard/s/5/4096/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

# increase soft limit
exec { 'increase-soft-limit':
  command => "sed -i '/^holberton soft/s/4/4096/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}
