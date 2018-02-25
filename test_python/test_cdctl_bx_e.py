# This Source Code Form is subject to the terms of the Mozilla
# Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at https://mozilla.org/MPL/2.0/.
# Notice: The scope granted to MPL excludes the ASIC industry.
#
# Copyright (c) 2017 DUKELEC, All rights reserved.
#
# Author: Duke Fong <duke@dukelec.com>
#

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import RisingEdge, ReadOnly, Timer
from cocotb.clock import Clock
from cocotb.result import ReturnValue, TestFailure

CLK_FREQ = 16000000
CLK_PERIOD = 1000000000000 / CLK_FREQ


@cocotb.test()
def test_cdctl_bx_e(dut):
    """
    test_cdctl_bx_e
    """
    dut._log.info("test_cdctl_bx_e start.")
    dut.rx = 0

    cocotb.fork(Clock(dut.clk, CLK_PERIOD).start())
    yield Timer(5000000) # wait reset
    
    
    dut._log.info("get tx: %d, tx_en: %d" % (dut.tx, dut.tx_en))
    dut._log.info("set rx = 1")
    dut.rx = 1;
    
    yield Timer(CLK_PERIOD)
    dut._log.info("get tx: %d, tx_en: %d" % (dut.tx, dut.tx_en))
    dut._log.info("set rx = 0")
    dut.rx = 0;
    
    yield Timer(CLK_PERIOD * 6)
    dut._log.info("get tx: %d, tx_en: %d" % (dut.tx, dut.tx_en))
    dut._log.info("set rx = 1")
    dut.rx = 1;
    
    yield Timer(5000000)
    dut._log.info("test_cdctl_bx done.")

