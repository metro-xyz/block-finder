import { createPublicClient, http } from "viem";
import { mainnet } from "viem/chains";
import * as dotenv from "dotenv";
dotenv.config();

const client = createPublicClient({
  chain: mainnet,
  transport: http(`https://eth-mainnet.g.alchemy.com/v2/${process.env.ALCHEMY_API_KEY}`),
});

const EthMainnetBlockTime = 12; // seconds

const run = async () => {
  const latestBlock = await client.getBlock({
    blockTag: "latest",
  });

  const latestBlockTimestamp = latestBlock.timestamp; // bigInt

  console.log(latestBlockTimestamp);


};

run().catch(console.error);
