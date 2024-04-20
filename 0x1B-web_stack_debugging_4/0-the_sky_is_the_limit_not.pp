#changes the ulimit of nginx
exec{ 'replace':
    provider => shell,
    command  => 'sed -i s/15/5000/g /etc/default/nginx && service nginx restart'
}
