import cocotb
import random
from cocotb.triggers import Timer
from cocotb.clock import Clock
@cocotb.test()
async def test_parity_calc(dut):
    # dut has inputs stream,clk and output out
    # create clock
    cocotb.fork(Clock(dut.clk, 10, units='ns').start())
    times=10000
    while True:
        # covert i to hex and send to dut
        num = random.randint(0,1023)
        dut.stream.value= num
        await Timer(10, units='ns')
        dut._log.info(f"Sending {num} to dut")
        # check if dut.out is equal to parity of i
        assert dut.out.value == bin(num)[2:].count('1') % 2; f"{dut.out.value} is not equal to parity of {bin(num)[2:].count('1') % 2}"
        #     dut._log.info("PASS")
        # else:
        #     dut._log.info("FAIL")
        #     dut._log.info(f"from dut = {dut.out.value} required = {bin(num)[2:].count('1')%2}")
        times-=1
        if times==0:
            break
        
