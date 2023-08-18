 UNITTEST — Unit testing framework
(If you are already familiar with the basic concepts of testing,
you might want to skip to the list of assert methods.)

The unittest unit testing framework was originally inspired by JUnit
and has a similar flavor as major unit testing frameworks in other languages.
It supports test automation, sharing of setup and shutdown code for tests, 
aggregation of tests into collections, and independence of the tests from the reporting framework.

To achieve this, unittest supports some important concepts in an object-oriented way:

TEST FIXTURE
A test fixture represents the preparation needed to perform one or more tests, 
and any associate cleanup actions. This may involve, for example,
creating temporary or proxy databases, directories, or starting a server process.

TEST CASE
A test case is the individual unit of testing.
It checks for a specific response to a particular set of inputs.
Unittest provides a base class, TestCase, which may be used to create new test cases.

TEST SUITE
A test suite is a collection of test cases, test suites, or both. 

It is used to aggregate tests that should be executed together.

TEST RUNNER
A test runner is a component which orchestrates the execution of tests and
provides the outcome to the user. The runner may use a graphical interface, 
a textual interface, or return a special value to indicate the results of executing the tests.
