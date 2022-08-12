from starknet_py.contract import Contract
from  starknet_py.net.gateway_client import GatewayClient

CONTRACT_ADDRESS = '0x0178a8866ef77a01df365b49d03fe46b8a90703e9fa1e10518277d12153b93d7'
ASSET = 'ETH/USD' # starknet.py automatically encodes the string
contract = Contract.from_address_sync(CONTRACT_ADDRESS, GatewayClient("testnet"))
result = contract.functions["get_value"].call_sync(ASSET)
print(result)
# to get the int value of ticker
print("int: ", int(("ETH/USD".encode('ascii').hex()),16)) #19514442401534788