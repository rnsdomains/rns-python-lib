<img src="/logo.png" alt="logo" height="200" />

# `RNS-SDK-py`


Implementations for local resolvers for the RIF Name Service, available for python backends.


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
```

```
virtualenv -p /yourLocalPythonPath/python3.7 rns_sdk_py_env
```

```
source rns_sdk_py_env/bin/activate
```

```
pip install -r requirements.txt
```

```
python setup.py develop

```

```
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


## Usage and Getting Started
In a Python console:

```
from rns_sdk.resolver_contract import ResolverContract

resolver = ResolverContract()

resolver.addr("foo.rsk")

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


## Documentation

For more information, see [RNS Docs](https://docs.rns.rifos.org).

## Related links

- [RSK](https://rsk.co)
    - [Docs](https://docs.rsk.co)
- [RIF](https://rifos.org)
    - [Docs](https://www.rifos.org/documentation/)
    - [Whitepaper](https://docs.rifos.org/rif-whitepaper-en.pdf)
    - [Testnet faucet](https://faucet.rifos.org)
- RNS
    - [Docs](https://docs.rns.rifos.org)
    - [Manager](https://rns.rifos.org)
    - [Testnet registrar](https://testnet.rns.rifos.org)

