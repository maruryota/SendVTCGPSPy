#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file SendVTCGpsPy.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")
import logging

# Import RTM module
import RTC
import OpenRTM_aist
import GPS
from send_zmq import req


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
sendvtcgpspy_spec = ["implementation_id", "SendVTCGpsPy",
		 "type_name",         "SendVTCGpsPy",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "maruryota",
		 "category",          "Category",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 "conf.default.host", "localhost",
		 "conf.default.port", "54321",
		 "conf.default.endpoint", "PuffinBP_2",

		 "conf.__widget__.host", "text",
		 "conf.__widget__.port", "text",
		 "conf.__widget__.endpoint", "text",

         "conf.__type__.host", "string",
         "conf.__type__.port", "string",
         "conf.__type__.endpoint", "string",

		 ""]
# </rtc-template>

##
# @class SendVTCGpsPy
# @brief ModuleDescription
#
#
class SendVTCGpsPy(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_GpsData = OpenRTM_aist.instantiateDataType(GPS.TimedGPSData)
		"""
		"""
		self._GpsDataOut = OpenRTM_aist.OutPort("GpsData", self._d_GpsData)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  host
		 - DefaultValue: localhost
		"""
		self._host = ['localhost']
		"""
		
		 - Name:  port
		 - DefaultValue: 54321
		"""
		self._port = ['54321']
		"""
		
		 - Name:  endpoint
		 - DefaultValue: PuffinBP_2
		"""
		self._endpoint = ['PuffinBP_2']

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("host", self._host, "localhost")
		self.bindParameter("port", self._port, "54321")
		self.bindParameter("endpoint", self._endpoint, "PuffinBP_2")

		# Set InPort buffers

		# Set OutPort buffers
		self.addOutPort("GpsData",self._GpsDataOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports
		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	##
	#
	# The activated action (Active state entry action)
	# former rtc_active_entry()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onActivated(self, ec_id):
		
		self.send_zmq_req = req.SendZMQRequest(
			host = self._host[0],
			port = self._port[0]
		)

		return RTC.RTC_OK

	###
	##
	## The deactivated action (Active state exit action)
	## former rtc_active_exit()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK

	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onExecute(self, ec_id):
		# output position information [m]
		print("execute")
		logging.info("execute")
		data = self.send_zmq_req.receive_data()
		self._d_GpsData.Data.lungitude = 139.7 + float(data["Report"]["Data"]["position"]["x"]) / 1000 / 110959.0097  # 緯度36度として計算
		self._d_GpsData.Data.latitude = 36 + float(data["Report"]["Data"]["position"]["y"]) / 1000 / 90163.2924  # 緯度36度として計算
		self._d_GpsData.Data.variance = None
		self._d_GpsData.Data.satellite = 4
		self._d_GpsData.Data.receivedTimestamp = int(time.time())  # should fix to get correct timestamp. This is lazy.
		print(data)
		logging.info(data)

		self._GpsDataOut.write()
		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def SendVTCGpsPyInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=sendvtcgpspy_spec)
    manager.registerFactory(profile,
                            SendVTCGpsPy,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SendVTCGpsPyInit(manager)

    # Create a component
    comp = manager.createComponent("SendVTCGpsPy")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

