import sys

def make_value(val, proc):
  match val:
    case str():
      return proc.make_string_value(val)
    case int():
      return proc.make_integer_value(val)
    case float():
      return proc.make_double_value(val)
    case bool():
      return proc.make_boolean_value(val)
    case list():
      return proc.make_array_value([make_value(v, proc) for v in val])
    case _:
      raise TypeError(f'Unsupported parameter type: {type(val)}')


sys.modules[__name__] = make_value
