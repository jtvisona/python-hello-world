"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 8
arrival_time.py
"""

from datetime import datetime as DT_datetime, timedelta as DT_timedelta
from sys import exit as SYS_exit

def get_trip_info_da( info: dict = {} ) -> dict:
    info[ 'departure_date'] = departure_date = "2024-11-12"
    info[ 'departure_time'] = departure_time = "08:00"
    info[ 'departure_dts'] = departure_date + " " + departure_time
    info[ 'arrival_date']  = arrival_date = "2024-11-12"
    info[ 'arrival_time'] = arrival_time = "12:30"
    info[ 'arrival_dts'] = arrival_date + " " + arrival_time
    return info

def calculate_and_display_trip_duration_from_depart_and_arrive( info: dict ) -> None:
    departure_stripd = DT_datetime.strptime( info[ 'departure_dts' ], "%Y-%m-%d %H:%M" )
    arrival_stripd = DT_datetime.strptime( info[ 'arrival_dts' ], "%Y-%m-%d %H:%M" )
    duration = arrival_stripd - departure_stripd
    hours, remainder = divmod( duration.total_seconds(), 3600)
    minutes = remainder // 60
    print( f"Estimated Departure: {departure_stripd}" )
    print( f"Estimated Arrival: {arrival_stripd}" )
    print( f"Estimated Trip Duration: {int( hours )} hours and {int( minutes )} minutes" )

def get_trip_info_dmr( info_dmr: dict = {} ) -> dict:
    info_dmr[ 'departure_date'] = departure_date = input( "Enter departure date (YYYY-MM-DD): ")
    #info_dmr[ 'departure_date'] = departure_date = "2024-11-12"
    info_dmr[ 'departure_time'] = departure_time = input( "Enter departure time (HH-MM): ")
    #info_dmr[ 'departure_time'] = departure_time = "08:00"
    info_dmr[ 'departure_dts'] = departure_date + " " + departure_time
    info_dmr[ 'distance']  = distance = int( input( "Distance in integerr miles: " ) )
    #info_dmr[ 'distance']  = distance = 200
    info_dmr[ 'rate'] = rate = int( input( "Enter rate in integer mph: " ) )
    #info_dmr[ 'rate'] = rate = 65
    info_dmr[ 'hours' ] = hours = distance // rate
    info_dmr[ 'minutes' ] = minutes = int( ( (distance / rate) - hours ) * 60 )
    str_hours = str( hours )
    if minutes < 10:
        str_minutes = "0" + str( minutes )
    else:
        str_minutes = str( minutes )
    info_dmr[ 'time' ] = str_hours + ":" + str_minutes
    return info_dmr

def calculate_and_display_trip_duration_from_depart_miles_and_rate( info_dmr: dict = {} ) -> None:
    departure_stripd = DT_datetime.strptime( info_dmr[ 'departure_dts' ], "%Y-%m-%d %H:%M" )
    time_to_add = DT_timedelta( hours=info_dmr[ 'hours' ], minutes=info_dmr[ 'minutes' ] )
    arrival = departure_stripd + time_to_add
    print( f"Estimated Departure: {departure_stripd}" )
    print( f"Distance: {info_dmr[ 'hours' ]}" )
    print( f"Time: {info_dmr[ 'time' ]}" )
    print( f"Arrival: {arrival}" )
    print( f"Estimated Trip Duration: {int( info_dmr[ 'hours' ] )} hours and {int( info_dmr[ 'minutes' ])} minutes" )

def main():
    #calculate_and_display_trip_duration_from_depart_and_arrive( get_trip_info_da() )
    choice = "y"
    while choice.lower() == "y":
        calculate_and_display_trip_duration_from_depart_miles_and_rate( get_trip_info_dmr() )
        choice = input( "Again? (y/n): ")

if __name__ == "__main__":
    main()