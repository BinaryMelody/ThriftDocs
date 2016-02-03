#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

import sys, glob
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('../../lib/py/build/lib.*')[0])

from tutorial import Calculator
from tutorial.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from datetime import datetime, timedelta

try:

  # Make socket
  transport = TSocket.TSocket('localhost', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = Calculator.Client(protocol)

  # Connect!
  transport.open()

  client.ping()
  print 'ping()'

  sum = client.add(1,1)
  print '1+1=%d' % (sum)

  work = Work()

  work.op = Operation.DIVIDE
  work.num1 = 1
  work.num2 = 0

  try:
    quotient = client.calculate(1, work)
    print 'Whoa? You know how to divide by zero?'
  except InvalidOperation, io:
    print 'InvalidOperation: %r' % io

  work.op = Operation.SUBTRACT
  work.num1 = 15
  work.num2 = 10

  diff = client.calculate(1, work)
  print '15-10=%d' % (diff)

  log = client.getStruct(1)
  print 'Check log: %s' % (log.value)

  arr = []

  for i in range(1000000):
    past = datetime.now()
    client.add(100, 100)
    now = datetime.now()
    timespan = now - past
    micro = timespan.microseconds + timespan.seconds * 1000000
    print micro
    arr.append(micro)

  # Close!
  transport.close()

  f = open("out.txt", "w")
  for item in arr:
    print >> f, item
  f.close()

  print "min"
  print min(arr)
  print "max"
  print max(arr)

except Thrift.TException, tx:
  print '%s' % (tx.message)
