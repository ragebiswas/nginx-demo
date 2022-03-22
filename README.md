# nginx-demo
Basic tutorial of nginx that demonstrates primary nginx capabilities

## Capabilities

| Capability            | Demo  
| -----------           | -----------
| Basic                 | 0-base.conf
| Static Serving        | 1-static.conf
| Rewrite / redirect    | 2-redir.conf
| Reverse proxy         | 3-proxy.conf
| Load balance          | 4-lb.conf
| Compress              | 5-compress.conf
| Cache                 | 6-cache.conf


## Running 

- Install nginx to a folder using `nginx-src/build.sh`
-  Execute the driver script:
```shell
$> python3 -m venv venv
$> source venv/bin/activate
$> pip install -r requirements.txt
$> python driver.py
```

## Demo of each capability

### 0. Basic 

```sh
curl -v localhost:8080
curl -v localhost:8080/specific/url?someparam=123
curl -v -H 'Host: foo.local' localhost:8080
curl -v -H 'Host: bar.local' localhost:8080
curl -v -H 'Host: example.com' localhost:8080
```

### 1. Static Serving

```sh
curl -I localhost:8080/tslogo.png
curl -i localhost:8080/gpl.txt | less
```

### 2. Rewrite & redirect

```sh
curl -v -H 'Host: foo.local'  localhost:8080/some/path?someparam=123
curl -v -H 'Host: foo2.local' localhost:8080/somepath
curl -v -H 'Host: foo2.local' localhost:8080/search?someparam=123
curl -v -H 'Host: bar.local'  localhost:8080/user/123
curl -v -H 'Host: bar2.local' localhost:8080/user/123
```

### 3. Proxy

```sh
# start nodejs server from backends directory
backends/run-backends.sh
curl -v localhost:8080/login
curl -v localhost:8080/someotherpath
```

### 4. Load Balancing

```sh
curl -v localhost:8080/path
```

### 5. Compress

```sh
curl -s -v -H 'Host: foo.local' localhost:8080/gpl.txt --output /dev/null
curl -s -v -H 'Host: bar.local' localhost:8080/gpl.txt --output /dev/null
curl -s -v -H 'Host: bar.local' -H 'Accept-Encoding: gzip' localhost:8080/gpl.txt --output /dev/null
```

### 6. Cache

```sh
curl -s -v localhost:8080/gpl.txt --output /dev/null
curl -s -v localhost:8080/tslogo.png --output /dev/null
```

## Maintainers

- [raj](mailto:ragebiswas@gmail.com)