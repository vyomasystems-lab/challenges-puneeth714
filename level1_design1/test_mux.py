# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

def get_value(each):
    # return value based on each
    # if each is divisible by 4, return 0 else return remainder
    return each % 4
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    # dut has sel,inp0,inpt1...inp30,out
    # create a test for this dut
    # create test bench
    dut.inp0.value = 0
    dut.inp1.value = 1
    dut.inp2.value = 2
    dut.inp3.value = 3
    dut.inp4.value = 0
    dut.inp5.value = 1
    dut.inp6.value = 2
    dut.inp7.value = 3
    dut.inp8.value = 0
    dut.inp9.value = 1
    dut.inp10.value = 2
    dut.inp11.value = 3
    dut.inp12.value = 0
    dut.inp13.value = 1
    dut.inp14.value = 2
    dut.inp15.value = 3
    dut.inp16.value = 0
    dut.inp17.value = 1
    dut.inp18.value = 2
    dut.inp19.value = 3
    dut.inp20.value = 0
    dut.inp21.value = 1
    dut.inp22.value = 2
    dut.inp23.value = 3
    dut.inp24.value = 0
    dut.inp25.value = 1
    dut.inp26.value = 2
    dut.inp27.value = 3
    dut.inp28.value = 0
    dut.inp29.value = 1
    # vals=[]
    # for each in range(30):
    #     sets = random.randint(0, 3)
    #     locals()[f"dut.inp{each}.value"]=sets
    #     cocotb.log.info(str(locals()[f"dut.inp{each}.value"])+f" {each}")
    #     vals.append(sets)
    for each in range(31):
        dut.sel.value = each
        # set sel = each
        if each == 30:
            await Timer(10, "ns")
            cocotb.log.info(
                f"Given input : output : {dut.out.value} at {each}")

            assert dut.out.value == 0
            "out should be 0"
        else:
            # wait for 10 ns
            await Timer(10, units='ns')
            cocotb.log.info(
                f"Given input : {get_value(each=each)} output : {dut.out.value} at {each}")
            # check if value at out is equal to each
            assert dut.out.value == get_value(each=each) ,f"Value at out: {dut.out.value} is not matching with {get_value(each=each)}"

    cocotb.log.info('##### CTB: Develop your test here ########')
