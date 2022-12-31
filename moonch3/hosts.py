from django_hosts import patterns, host

host_patterns = patterns(
    '',
    
    host(r'', 'moonweb.urls', name=' '),
    host(r'api', 'moonch3api.urls', name='api'),
    host(r'admin' , 'moonch3.admin_url' , name='admin') ,
    host(r'blog', 'moonblog.urls' , name='blog'),
)