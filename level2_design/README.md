# Adder Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![gitpod](gitpod_screenshot.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux here) which takes in CLK,RST_N,
mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3,EN_mav_putvalue,and out mav_putvalue,RDY_mav_putvalue,
mv_scopbusy,RDY_mv_scopbusy

The values are assigned to the input port using 
```
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x101010B3

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
```

The assert statement is used for comparing the mux
 outut to the expected value.

The following error is seen:
```
                  assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0xa does not match MODEL = 0x0
                     assert 000000000000000000000000000001010 == 0
```
## Test Scenario **(Important)**
- Test Inputs:     mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x1
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x101010B3

- Expected Output: sum=0
- Observed Output in the DUT dut.sum=000000000000000000000000000001010

Output mismatches for the above inputs proving that there is a design bug


## Verification Environment - 2

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux here) which takes in CLK,RST_N,
mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3,EN_mav_putvalue,and out mav_putvalue,RDY_mav_putvalue,
mv_scopbusy,RDY_mv_scopbusy

The values are assigned to the input port using 
```
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x1
    mav_putvalue_instr = 0x101010B3

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
```

The assert statement is used for comparing the mux
 outut to the expected value.

The following error is seen:
```
                  assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0xa does not match MODEL = 0x0
                     assert 000000000000000000000000000000010 == 0
```
## Test Scenario **(Important)**
- Test Inputs:     mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x1
    mav_putvalue_instr = 0x101010B3

- Expected Output: sum=0
- Observed Output in the DUT dut.sum=000000000000000000000000000000010

Output mismatches for the above inputs proving that there is a design bug


## Is the verification complete ?

- The verification is complete.