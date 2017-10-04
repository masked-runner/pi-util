class Util():

  info = "utility :v.0.0.0"

  def __init__(self):
    self.init = True

  def is_empty(self, data):
     if self.is_string(data) or self.is_dictionary(data) or self.is_list(data):
      return self.is_shared_empty(data)
     else:
      return "unsupported_type"
  def is_float(self, data):
     return isinstance(data, float)
  def is_int(self, data):
     return isinstance(data, int)
  def is_string(self, data):
     return isinstance(data, str)
  def is_dictionary(self, data):
     return isinstance(data, dict)
  def is_list(self, data):
     return isinstance(data, list)
  def length(self, data):
     return len(data)

  def is_shared_empty(self, data):
    if self.length(data) < 1:
      return True
    else:
      return False