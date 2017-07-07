# Nginx proxy Plugin for inetprocess/marina
Plugin made by Inet Process to setup any webservice behind a nginx proxy with certbot encryption

__WARNING: The plugin directory must be named `nginx_proxy`__ (complete path: plugins/nginx_proxy`)

# Installation
Clone the repository in the plugins/ directory of your docker-lamp

You also need to add to your compose.ini:
```ini
; nginx-proxy virtual host name
virtual_host=test.inetprocess.fr
admin_email=admin@inetprocess.com
acme_ca_uri=https://acme-staging.api.letsencrypt.org/directory
```

# nginx-proxy command
Use `maarina nginx-proxy` to add a second instance to the master nginx setup.
