# Python stubs generated by omniidl from idl/GPSData.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


# #include "BasicDataType.idl"
import BasicDataType_idl
_0_RTC = omniORB.openModule("RTC")
_0_RTC__POA = omniORB.openModule("RTC__POA")

# #include "ExtendedDataTypes.idl"
import ExtendedDataTypes_idl
_0_RTC = omniORB.openModule("RTC")
_0_RTC__POA = omniORB.openModule("RTC__POA")

# #include "InterfaceDataTypes.idl"
import InterfaceDataTypes_idl
_0_RTC = omniORB.openModule("RTC")
_0_RTC__POA = omniORB.openModule("RTC__POA")

#
# Start of module "GPS"
#
__name__ = "GPS"
_0_GPS = omniORB.openModule("GPS", r"idl/GPSData.idl")
_0_GPS__POA = omniORB.openModule("GPS__POA", r"idl/GPSData.idl")


# struct GPSData
_0_GPS.GPSData = omniORB.newEmptyClass()
class GPSData (omniORB.StructBase):
    _NP_RepositoryId = "IDL:GPS/GPSData:1.0"

    def __init__(self, longitude, latitude, variance, satellite, receivedTimestamp):
        self.longitude = longitude
        self.latitude = latitude
        self.variance = variance
        self.satellite = satellite
        self.receivedTimestamp = receivedTimestamp

_0_GPS.GPSData = GPSData
_0_GPS._d_GPSData  = (omniORB.tcInternal.tv_struct, GPSData, GPSData._NP_RepositoryId, "GPSData", "longitude", omniORB.tcInternal.tv_double, "latitude", omniORB.tcInternal.tv_double, "variance", omniORB.tcInternal.tv_double, "satellite", omniORB.tcInternal.tv_ushort, "receivedTimestamp", omniORB.tcInternal.tv_ulong)
_0_GPS._tc_GPSData = omniORB.tcInternal.createTypeCode(_0_GPS._d_GPSData)
omniORB.registerType(GPSData._NP_RepositoryId, _0_GPS._d_GPSData, _0_GPS._tc_GPSData)
del GPSData

# struct TimedGPSData
_0_GPS.TimedGPSData = omniORB.newEmptyClass()
class TimedGPSData (omniORB.StructBase):
    _NP_RepositoryId = "IDL:GPS/TimedGPSData:1.0"

    def __init__(self, tm, Data):
        self.tm = tm
        self.Data = Data

_0_GPS.TimedGPSData = TimedGPSData
_0_GPS._d_TimedGPSData  = (omniORB.tcInternal.tv_struct, TimedGPSData, TimedGPSData._NP_RepositoryId, "TimedGPSData", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "Data", omniORB.typeMapping["IDL:GPS/GPSData:1.0"])
_0_GPS._tc_TimedGPSData = omniORB.tcInternal.createTypeCode(_0_GPS._d_TimedGPSData)
omniORB.registerType(TimedGPSData._NP_RepositoryId, _0_GPS._d_TimedGPSData, _0_GPS._tc_TimedGPSData)
del TimedGPSData

#
# End of module "GPS"
#
__name__ = "GPSData_idl"

_exported_modules = ( "GPS", )

# The end.