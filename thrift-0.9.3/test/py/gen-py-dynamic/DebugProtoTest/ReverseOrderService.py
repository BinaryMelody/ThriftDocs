#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:dynamic
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.protocol.TBase import TBase, TExceptionBase, TTransport


class Iface(object):
  def myMethod(self, first, second, third, fourth):
    """
    Parameters:
     - first
     - second
     - third
     - fourth
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def myMethod(self, first, second, third, fourth):
    """
    Parameters:
     - first
     - second
     - third
     - fourth
    """
    self.send_myMethod(first, second, third, fourth)
    self.recv_myMethod()

  def send_myMethod(self, first, second, third, fourth):
    self._oprot.writeMessageBegin('myMethod', TMessageType.CALL, self._seqid)
    args = myMethod_args()
    args.first = first
    args.second = second
    args.third = third
    args.fourth = fourth
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_myMethod(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = myMethod_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["myMethod"] = Processor.process_myMethod

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_myMethod(self, seqid, iprot, oprot):
    args = myMethod_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = myMethod_result()
    try:
      self._handler.myMethod(args.first, args.second, args.third, args.fourth)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("myMethod", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class myMethod_args(TBase):
  """
  Attributes:
   - first
   - second
   - third
   - fourth
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'fourth', None, None, ), # 1
    (2, TType.I32, 'third', None, None, ), # 2
    (3, TType.I16, 'second', None, None, ), # 3
    (4, TType.STRING, 'first', None, None, ), # 4
  )

  def __init__(self, first=None, second=None, third=None, fourth=None,):
    self.first = first
    self.second = second
    self.third = third
    self.fourth = fourth

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.first)
    value = (value * 31) ^ hash(self.second)
    value = (value * 31) ^ hash(self.third)
    value = (value * 31) ^ hash(self.fourth)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class myMethod_result(TBase):

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
