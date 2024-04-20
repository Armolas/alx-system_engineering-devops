#changes the ulimit of holberton
exec{ 'replace':
    provider => shell,
    command  => 'sed -i s/5/100/g /etc/security/limits.conf && sed -i s/4/100/g /etc/security/limits.conf'
}
