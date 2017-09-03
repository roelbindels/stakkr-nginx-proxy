# Nginx proxy Plugin for https://github.com/edyan/stakkr/
Plugin made by Roel Bindels (iNet Process) to setup any webservice behind a nginx proxy with certbot encryption. Original setup is inspired by the nginx proxy setup from Jason Wilder. (https://github.com/jwilder/nginx-proxy)

__WARNING: The plugin directory must be named `nginx_proxy`__ (complete path: plugins/nginx_proxy`)

# Setup Stakkr
To use the plugin, a stakkr environment has to setup prior to using the plugin. Please check the manual for full installation notes. http://stakkr.readthedocs.io/en/latest/pages/installation.html

```
mkdir stakkr
cd stakkr/
virtualenv -p /usr/bin/python3 prod_stakkr
source prod_stakkr/bin/activate
pip --no-cache-dir install stakkr
```

# Installation
Now the plugin can be installed by cloning the repository in the plugins/ directory of your stakkr setup. Important is to call the plugin **nginx_proxy**.
 ```
 cd plugins/
git clone https://github.com/inetprocess/stakkr-nginx-proxy.git nginx_proxy
cd ..
```

You also need to add the following settings to your conf/compose.ini:
```
# nginx-proxy virtual host name
virtual_host=test.inetprocess.fr
admin_email=admin@inetprocess.com

# Directory URI for the CA ACME API endpoint. If you set it's value to staging letsencrypt will use test servers that don't have the 5 certs/week/domain limits.
# STAGING
# acme_ca_uri=https://acme-staging.api.letsencrypt.org/directory
# DEFAULT
acme_ca_uri=https://acme-v01.api.letsencrypt.org/directory
```
Now run;
```
stakkr refresh-plugins
```

# Multiple stakkr environment on a single host.
There can only be a single nginx-proxy listening to port 80. Therefore the proxy is setup with it's own network layer, the proxy-tier. We can add multiple containers to this network, so they can be proxied.

Use `stakkr nginx-proxy` to add a second instance to the master nginx setup.
