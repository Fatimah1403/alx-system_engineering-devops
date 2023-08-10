# writing puppet to fix a bug in wordpress file wp-setings.php

$edited_file = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'replace_line_with_correct':
  command => "sed -i 's/phpp/php/g' ${edited_file}",
  path    => ['/bin','/usr/bin']
}
