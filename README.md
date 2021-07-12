# trequests
A lazy, minimalist, but fast HTTP request module for Python 3.4+

```python
import trequests

session = trequests.Session(proxies={}, timeout=5)

resp = session.get("https://api.ipify.org/?format=json")
print(resp.json())
```

Popular modules such as [requests](https://github.com/psf/requests) don't perform well in multi-threaded scenarios, xrequests aims to be the solution to this problem.

![Graph](https://github.com/tututuana/trequests/blob/main/graph.png)

Some quirks:
- `Session` instances are NOT thread-safe
- Unlike psf/requests, this module does NOT support cookiejars, redirects, uploading files and streaming.
- No retry attempts will be made, unless a connection is established from a previous request
- All raised exceptions are wrapped under `RequestException`

Supports:
- HTTP, SOCKS4 and SOCKS5 proxies
- Brotli, gzip and deflate compression algorithms
- Unverified SSL

# Installation
```bash
pip install -U git+https://github.com/tututuana/trequests.git
```
