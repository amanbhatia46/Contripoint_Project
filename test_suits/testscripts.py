from unittest import TestLoader, TestSuite, TextTestRunner, loader, runner, suite, TestCase
import sys
sys.path.append("/home/am.bhatia/Desktop/contripoint")

import test_cases_files

#importing all class from their file

from test_cases_files.login import Authentication
from test_cases_files.certifications import CAuth
from test_cases_files.clientfeedback import CFAuth
from test_cases_files.InterviewTaken import ITAuth
from test_cases_files.TrainingSession import TSAuth
from test_cases_files.mentorship import MAuth
from test_cases_files.projects import PAuth
from test_cases_files.teambuildingactivity import TBAuth
from test_cases_files.selfdevelopment import SDAuth


#testtools is a set of extensions to the Python standard library’s unit testing framework. 
import testtools as testtools 

if __name__ == "main":

    loader = TestLoader()  #TestLoader class is used to create test suites from classes and modules

#run test sequentially using simple TextTestRunner
runner = TextTestRunner(verbosity=2)
runner.run(TestSuite((
        TestLoader().loadTestsFromTestCase(Authentication),
        TestLoader().loadTestsFromTestCase(CAuth),
        TestLoader().loadTestsFromTestCase(ITAuth),
        TestLoader().loadTestsFromTestCase(TSAuth),
        TestLoader().loadTestsFromTestCase(MAuth),
        TestLoader().loadTestsFromTestCase(PAuth),
        TestLoader().loadTestsFromTestCase(CFAuth),
        TestLoader().loadTestsFromTestCase(TBAuth),
        TestLoader().loadTestsFromTestCase(SDAuth),
        )))

#run parallel testing using concurrent_suite
concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
concurrent_suite.run(testtools.StreamResult())
