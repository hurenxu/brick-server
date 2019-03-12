# high-level interface for interacting with Brick graphs using rdflib
# setup our query environment
from rdflib import RDFS, RDF, Namespace, Graph, URIRef
from common import *

g = Graph()
g.parse('sample_data/ebu3b_brick.ttl', format='turtle')
PREFIX = """
    PREFIX brick: <http://brickschema.org/schema/1.0.2/Brick#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX bf: <http://brickschema.org/schema/1.0.2/BrickFrame#>
"""

def get_all_rooms():
    q = PREFIX + """
    select ?s where {
        ?s rdf:type brick:Room .
    }
    """
    return g.query(q)

def get_all_points():
    q = PREFIX + """
    select ?s where {
        ?s bf:isLocatedIn ?r .
        ?s bf:isPointOf ?r .
        ?r rdf:type brick:Room .
    }
    """
    return g.query(q)

def get_thermal_power_sensors():
    q = PREFIX + """
    select ?s where {
        ?s rdf:type brick:Thermostat_Adjust_Sensor .
    }
    """
    return g.query(q)

def get_zone_temperature_sensors():
    q = PREFIX + """
    select ?s where {
        ?s rdf:type brick:Zone_Temperature_Sensor .
    }
    """
    return g.query(q)

def get_occupied_commands():
    q = PREFIX + """
    select ?s where {
        ?s rdf:type brick:Occupancy_Command .
    }
    """
    return g.query(q)

def get_temperature_setpoints():
    q = PREFIX + """
    select ?s where {
        ?s rdf:type brick:Temperature_Setpoint .
    }
    """
    return g.query(q)

def print_result(key):
    print('Get ' + key)
    funcDict = {
        "all rooms": get_all_rooms,
        "all points": get_all_points,
        "thermal power sensors": get_thermal_power_sensors,
        "zone temperature sensors": get_zone_temperature_sensors,
        "occupied commands": get_occupied_commands,
        "temperature setpoints": get_temperature_setpoints
    }
    for index,element in enumerate(funcDict[key]()):
        print('{}: {}'.format(index + 1, element))

if __name__ == '__main__':
    # Can change key to make function call
    keys = {"zone temperature sensors"}
    # "all rooms", "all points", "thermal power sensors",
    # "zone temperature sensors", "occupied commands", 
    # "temperature setpoints"
    for key in keys:
        print_result(key)
