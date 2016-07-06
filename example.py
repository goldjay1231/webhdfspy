#!/usr/bin/env python
import time
import json
import webhdfspy

c = webhdfspy.WebHDFSClient('1.1.1.1', 8443, 'USER', 'PASS')

print '\n## list dir ##'
print json.dumps(c.listdir('/tmp'), indent=4)
time.sleep(1)

print '\n## mkdir: /tmp/test_webhdfs ##'
c.mkdir('/tmp/test_webhdfs')
time.sleep(1)

print '\n## create file: /tmp/test_webhdfs/text ##'
c.create('/tmp/test_webhdfs/text', 'text', True)
print json.dumps(c.listdir('/tmp/test_webhdfs'))
time.sleep(1)

print '\n## copyfromlocal: /etc/hosts to /tmp/test_webhdfs/test_hosts ##'
c.copyfromlocal('/etc/hosts', '/tmp/test_webhdfs/test_hosts', True)
time.sleep(1)

print '\n## rename to /tmp/test_webhdfs/test_hosts_rename ##'
c.rename('/tmp/test_webhdfs/test_hosts', '/tmp/test_webhdfs/test_hosts_rename')
time.sleep(1)

print '\n## open: /tmp/test_webhdfs/test_hosts_rename ##'
print c.open('/tmp/test_webhdfs/test_hosts_rename')
time.sleep(1)

print '\n## remove dir: /tmp/test_webhdfs ##'
c.remove('/tmp/test_webhdfs', True)

