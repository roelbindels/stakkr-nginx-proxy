# Nginx proxy Plugin for https://github.com/edyan/stakkr/
Plugin made by Roel Bindels (iNet Process) to setup any webservice behind a nginx proxy with certbot encryption. Original setup is inspired by the nginx proxy setup from Jason Wilder. (https://github.com/jwilder/nginx-proxy)

__WARNING: The plugin directory must be named `nginx_proxy`__ (complete path: plugins/nginx_proxy`)

# Installation
Clone the repository in the plugins/ directory of your stakkr setup.

You also need to add to your compose.ini:
```ini
; nginx-proxy virtual host name
virtual_host=test.inetprocess.fr
admin_email=admin@inetprocess.com
acme_ca_uri=https://acme-staging.api.letsencrypt.org/directory
```

# nginx-proxy command
Use `stakkr nginx-proxy` to add a second instance to the master nginx setup.
