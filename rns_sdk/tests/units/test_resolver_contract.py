import unittest

from rns_sdk.contracts.resolver_contract import ResolverContract


class TestResolverConctract(unittest.TestCase):
    """
    Test methods of interface to the RSK Name Service.
    """

    def test_addr_not_set(self):
        result = resolver.addr(foo_domain)
        self.assertEqual(result, "0x0000000000000000000000000000000000000000")

    def test_has_other_kind(self):
        result = resolver.has(foo_domain, "other")
        self.assertFalse(result)

    def test_supports_interface(self):
        result = resolver.supports_interface("0x3b3b57de")
        self.assertTrue(result)

    def test_unsupports_interface(self):
        result = resolver.supports_interface("0x3b3b57d1")
        self.assertFalse(result)

    def test_set_addr(self):
        result = resolver.set_addr("rsk.co", "0x6be2285f7F097FE23aE27e392cDac8dcDaAbf36C", accounts[0])
        self.assertIsNotNone(result)

    def test_addr(self):
        result = resolver.addr("rsk.co")
        self.assertNotEqual(result, "0x0000000000000000000000000000000000000000")

    def test_set_content(self):
        response = resolver.set_content(foo_domain, a_hash,  accounts[0])
        self.assertIsNotNone(response)


if __name__ == '__main__':
    resolver = ResolverContract()
    foo_domain = "foo.rsk"
    a_hash = "0x89ad40fcd44690fb5aa90e0fa51637c1b2d388f8056d68430d41c8284a6a7d5e";

    accounts = resolver.web3.eth.accounts

    unittest.main()
