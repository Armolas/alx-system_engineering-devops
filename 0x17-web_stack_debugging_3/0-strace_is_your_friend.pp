# Define a resource to manage the specific file
file { '/var/www/html/wp-settings.php':

  ensure  => present,

  # Replace a specific line based on a pattern
  replace => 'require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );',
  # Content to replace the matched line with
  with    => 'require_once( ABSPATH . WPINC . '/class-wp-locale.php' );'
}
