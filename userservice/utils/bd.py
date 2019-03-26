'''
userservice.utils.bd
---------------

bd service layer

@copyright:(c) 2013 SynergyLabs
@license:UCSD License. See License file for details.
'''
from building_depot import CenterService, SensorService

center_service = CenterService(base_url="https://bd-central.ucsd.edu",
                               api_key="d81459cb-fbd3-479c-9070-8906427e0c45",
                               username="genie@bdapps.ucsd.edu")
sensor_service = SensorService(data_service_url="https://bd-datas1.ucsd.edu",
                               api_key="d81459cb-fbd3-479c-9070-8906427e0c45",
                               username="genie@bdapps.ucsd.edu")
