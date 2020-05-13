<p align="middle">
    <img src="https://www.rifos.org/assets/img/logo.svg" alt="logo" height="100" >
</p>
<h3 align="middle"><code>rns-python-lib</code></h3>
<p align="middle">
    RNS Python SDK
</p>
<p align="middle">
    <a href="https://developers.rsk.co/rif/rns/libs/Python/">
      <img src="https://img.shields.io/badge/-docs-brightgreen" alt="docs" />
    </a>
</p>

Implementation for resolvers for the RIF Name Service, available for Python.

```py
from rns_sdk.resolver_contract import ResolverContract
resolver = ResolverContract()
resolver.addr("foo.rsk")
```

## Requirements

- Python Version: 3.7
- Pip Version: lastest
- VirtualEnv Version: lastest

## Testing

To run unit tests, clone this repository.

Run Rsk Node and deploy resolver contracts.
Check constants folder to specify, RPC_CLIENT_URL in client_constants.py file and RNS_RESOLVER_ADDRESS in
rns_constants.py file.

Add the PYTHONPATH environment variable of your operating system to the path of the folder where you cloned the project, this will allow the tests to directly invoke the file by console.

Run:

```
pip install virtualenv
virtualenv -p /yourLocalPythonPath/python3.7 rns_sdk_py_env
source rns_sdk_py_env/bin/activate
pip install -r requirements.txt
python setup.py develop
python3.7 tests/units/test_resolver_contract.py -v
```

The result that you should see if everything went well is

```
test_addr (__main__.TestResolverConctract) ... ok
test_addr_not_set (__main__.TestResolverConctract) ... ok
test_has_other_kind (__main__.TestResolverConctract) ... ok
test_set_addr (__main__.TestResolverConctract) ... ok
test_set_content (__main__.TestResolverConctract) ... ok
test_supports_interface (__main__.TestResolverConctract) ... ok
test_unsupports_interface (__main__.TestResolverConctract) ... ok

----------------------------------------------------------------------
Ran 7 tests in 1.043s

OK
```

## Build Source

To generate a compiled package you must use

```
python3.7 setup.py sdist bdist_wheel
```

## Contracts

### RNS.sol

Implementation of the RNS Registry, the central contract used to look up resolvers and owners for domains.

### PublicResolver.sol

Simple resolver implementation that allows the owner of any domain to configure how its name should resolve. One deployment of this contract allows any number of people to use it, by setting it as their resolver in the registry.
