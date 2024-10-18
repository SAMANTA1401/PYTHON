import asyncio
import time

async def main():
    print("heolo")
    await asyncio.sleep(1)
    print("world")
# asyncio.run(main()) 
# The asyncio.run() function to run the top-level entry point “main()” 
# function see the above example.) 

# Awaiting on a co-routine. (see the example given belo

async def tell_after(delay_time,what_to_tell):
    await asyncio.sleep(delay_time)
    print(what_to_tell)

async def main():
    print(f"started at {time.strftime('%X')}")
    await tell_after(1, "hello")
    await tell_after(2, "world")
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
