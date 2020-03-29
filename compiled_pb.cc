#include <Python.h>

#include <google/protobuf/message.h>
#include <google/protobuf/pyext/message.h>
#include <google/protobuf/pyext/message_factory.h>

#include "test_message.pb.h"

static PyObject* getAProtobuf(PyObject* self, PyObject* args);

static PyMethodDef sCompiledPbMethods[] = {
  {"get_a_protobuf", getAProtobuf, METH_VARARGS, "Get a protobuf"},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef sCompiledPbModule = {
  PyModuleDef_HEAD_INIT,
  "compiled_pb",
  NULL,
  -1,
  sCompiledPbMethods
};

extern "C"
PyObject* PyInit_compiled_pb(void) {
  return PyModule_Create(&sCompiledPbModule);
}

PyObject* PyMessage_NewMessageTakeOwnership(google::protobuf::Message* message) {
  using namespace google::protobuf;
  using namespace google::protobuf::python;
  if (message->GetReflection()->GetMessageFactory() !=
      MessageFactory::generated_factory()) {
    PyErr_SetString(PyExc_TypeError,
                    "Message pointer was not created from the default factory");
    return nullptr;
  }

  CMessageClass* message_class = message_factory::GetOrCreateMessageClass(
      GetDefaultDescriptorPool()->py_message_factory, message->GetDescriptor());

  CMessage* self = cmessage::NewEmptyMessage(message_class);
  if (self == nullptr) {
    return nullptr;
  }
  Py_DECREF(message_class);
  self->message = message;
  self->parent = nullptr;
  return self->AsPyObject();
}

static PyObject* getAProtobuf(PyObject* self, PyObject* args) {
  TestMessage* msg = new TestMessage();
  msg->set_a(5);
  msg->set_b("asdf");

  TestRepeatedA* ma = msg->add_c();
  ma->add_d()->set_e(1);
  ma->add_d()->set_f(2);

  ma = msg->add_c();
  ma->add_d()->set_f(5);
  ma->add_d()->set_e(6);

  PyObject* ret = PyMessage_NewMessageTakeOwnership(msg);
  return ret;
}
