#!/usr/bin/env python

from ncclient import manager


def connect(host, port, user, password):
    conn = manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
            hostkey_verify=False)

    print 'show system users'
    print '*' * 30
    result = conn.command(command='show system users', format='text')
    print result.tostring

    print 'show version'
    print '*' * 30
    result = conn.command('show version', format='text')
    print result.tostring

    print 'bgp summary'
    print '*' * 30
    result = conn.command('show bgp summary')
    print result.tostring

if __name__ == '__main__':
    connect('router', '22', 'netconf', 'Juniper!')
