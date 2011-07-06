"""autogenerated by genmsg_py from LinearMovementGoal.msg. Do not edit."""
import roslib.message
import struct

import geometry_msgs.msg
import std_msgs.msg

class LinearMovementGoal(roslib.message.Message):
  _md5sum = "3eceff484681a8278d5e078b51a65c24"
  _type = "ptp_arm_action/LinearMovementGoal"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
bool relative
float64 trans_vel
float64 rot_vel
geometry_msgs/PoseStamped goal

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['relative','trans_vel','rot_vel','goal']
  _slot_types = ['bool','float64','float64','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       relative,trans_vel,rot_vel,goal
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(LinearMovementGoal, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.relative is None:
        self.relative = False
      if self.trans_vel is None:
        self.trans_vel = 0.
      if self.rot_vel is None:
        self.rot_vel = 0.
      if self.goal is None:
        self.goal = geometry_msgs.msg.PoseStamped()
    else:
      self.relative = False
      self.trans_vel = 0.
      self.rot_vel = 0.
      self.goal = geometry_msgs.msg.PoseStamped()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_B2d3I.pack(_x.relative, _x.trans_vel, _x.rot_vel, _x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs))
      _x = self.goal.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.goal.pose.position.x, _x.goal.pose.position.y, _x.goal.pose.position.z, _x.goal.pose.orientation.x, _x.goal.pose.orientation.y, _x.goal.pose.orientation.z, _x.goal.pose.orientation.w))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.goal is None:
        self.goal = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 29
      (_x.relative, _x.trans_vel, _x.rot_vel, _x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs,) = _struct_B2d3I.unpack(str[start:end])
      self.relative = bool(self.relative)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.goal.pose.position.x, _x.goal.pose.position.y, _x.goal.pose.position.z, _x.goal.pose.orientation.x, _x.goal.pose.orientation.y, _x.goal.pose.orientation.z, _x.goal.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_B2d3I.pack(_x.relative, _x.trans_vel, _x.rot_vel, _x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs))
      _x = self.goal.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.goal.pose.position.x, _x.goal.pose.position.y, _x.goal.pose.position.z, _x.goal.pose.orientation.x, _x.goal.pose.orientation.y, _x.goal.pose.orientation.z, _x.goal.pose.orientation.w))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.goal is None:
        self.goal = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 29
      (_x.relative, _x.trans_vel, _x.rot_vel, _x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs,) = _struct_B2d3I.unpack(str[start:end])
      self.relative = bool(self.relative)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.goal.pose.position.x, _x.goal.pose.position.y, _x.goal.pose.position.z, _x.goal.pose.orientation.x, _x.goal.pose.orientation.y, _x.goal.pose.orientation.z, _x.goal.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_7d = struct.Struct("<7d")
_struct_B2d3I = struct.Struct("<B2d3I")
