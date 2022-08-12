from starknet_py.contract import Contract
from  starknet_py.net.gateway_client import GatewayClient
import asyncio

async def main():
	CONTRACT_ADDRESS = '0x0178a8866ef77a01df365b49d03fe46b8a90703e9fa1e10518277d12153b93d7'
	ASSET = 'ETH/USD' # starknet.py automatically encodes the string
	client_instance = GatewayClient("testnet")
	contract = await Contract.from_address_sync(CONTRACT_ADDRESS, client_instance)
	result = await contract.functions["get_value"].call_sync(ASSET)
	print(result)

asyncio.run(main())