#!/usr/bin/env python
import xmostest
import os

def run(arch):
    test_name = os.path.splitext(os.path.basename(__file__).replace("test_", "", 1))[0]

    resources = xmostest.request_resource("xsim")

    binary = '{}/bin/{}/{}_{}.xe'.format(test_name, arch, test_name, arch)

    tester = xmostest.ComparisonTester(open('{}.expect'.format(test_name)),
                                     'lib_trycatch', 'trycatch_tests',
                                     "{}_{}".format(test_name, arch))

    tester.set_min_testlevel("smoke")

    xmostest.run_on_simulator(resources['xsim'], binary,
                              simthreads=[],
                              tester=tester,
                              simargs=['--xscope', '-offline xscope.xmt'])

def runtest():
    run("XS1")
    run("XS2")
