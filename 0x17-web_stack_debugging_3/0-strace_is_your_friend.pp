# writing puppet to fix a bug in wordpress file wp-setings.php
# fixed bad ''phpp extention to 'php'

$edited_file = 'var/www/html/wp-settings.php'

exec { 'fix the php extention prob':
  command => "sed -i 's/phpp/php/g' ${edited_file}",
  path    => ['/bin','/usr/bin']
}
