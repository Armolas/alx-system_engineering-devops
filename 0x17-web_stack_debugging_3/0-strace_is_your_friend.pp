# Define a resource to manage the specific file
file { '/path/to/your/file':

  # Replace a specific line based on a pattern
  replace => 'require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );',
  # Content to replace the matched line with
  with    => 'require_once( ABSPATH . WPINC . '/class-wp-locale.php' );',

  # Ensure the file is present before making changes
  ensure  => present,
}
