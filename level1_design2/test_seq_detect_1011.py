# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.binary import BinaryValue


@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    # Create a 10us period clock on port clk
    clock = Clock(dut.clk, 5, units="us")
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    # vec=BinaryValue(30)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)

    cocotb.log.info(
        f"Actually it should be 1 but showing {dut.seq_seen.value}")
    cocotb.log.info('#### CTB: Develop your test here! ######')

    assert dut.seq_seen.value == 1, f"Actual seq=1 Result ={dut.seq_seen.value}"


@cocotb.test()
async def test_seq_bug1_1(dut):
    """Test for seq detection """

    # Create a 10us period clock on port clk
    clock = Clock(dut.clk, 5, units="us")
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)

    cocotb.log.info(
        f"Actually it should be 1 but showing {dut.seq_seen.value}")
    cocotb.log.info('#### CTB: Develop your test here! ######')

    assert dut.seq_seen.value == 1, f"Actual seq=1 Result ={dut.seq_seen.value}"
