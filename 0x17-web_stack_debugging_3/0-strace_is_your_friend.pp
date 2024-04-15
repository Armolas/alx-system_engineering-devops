# Define a resource to manage the specific file
exec{ 'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
