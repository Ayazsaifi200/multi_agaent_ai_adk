from utils.api_helpers import get_spacex_next_launch

class SpaceXAgent:
    def __init__(self):
        pass
        
    def process(self, input_data=None):
        """Get information about the next SpaceX launch"""
        try:
            launch_data = get_spacex_next_launch()
            
            # Extract relevant information
            launch_info = {
                "mission_name": launch_data.get("name", "Unknown"),
                "launch_date": launch_data.get("date_utc", "Unknown"),
                "launch_site": launch_data.get("launchpad"),
                "details": launch_data.get("details", "No details available"),
                "rocket": launch_data.get("rocket", "Unknown")
            }
            
            # Try to get location information from launchpad
            if "launchpad" in launch_data and isinstance(launch_data["launchpad"], str):
                launchpad_id = launch_data["launchpad"]
                # Hardcoded launchpad information for common SpaceX launchpads
                launchpads = {
                    "5e9e4501f509094ba4566f84": {  # Cape Canaveral SLC-40
                        "name": "Cape Canaveral Space Force Station",
                        "location": "Cape Canaveral, FL",
                        "latitude": 28.5618571,
                        "longitude": -80.577366
                    },
                    "5e9e4502f509092b78566f87": {  # KSC LC-39A
                        "name": "Kennedy Space Center",
                        "location": "Merritt Island, FL",
                        "latitude": 28.6080585,
                        "longitude": -80.6039558
                    },
                    "5e9e4502f509094188566f88": {  # Vandenberg SLC-4E
                        "name": "Vandenberg Space Force Base",
                        "location": "Lompoc, CA",
                        "latitude": 34.632093,
                        "longitude": -120.610829
                    },
                    "5e9e4502f5090927f8566f85": {  # Starbase
                        "name": "Starbase",
                        "location": "Boca Chica, TX",
                        "latitude": 25.9972,
                        "longitude": -97.1566
                    }
                }
                
                if launchpad_id in launchpads:
                    launch_info["launch_location"] = launchpads[launchpad_id]
                else:
                    # Default to Kennedy Space Center if launchpad is unknown
                    launch_info["launch_location"] = {
                        "name": "Kennedy Space Center (default)",
                        "location": "Merritt Island, FL",
                        "latitude": 28.6080585,
                        "longitude": -80.6039558
                    }
            else:
                # Default to Kennedy Space Center if launchpad info is missing
                launch_info["launch_location"] = {
                    "name": "Kennedy Space Center (default)",
                    "location": "Merritt Island, FL",
                    "latitude": 28.6080585,
                    "longitude": -80.6039558
                }
                
            return launch_info
            
        except Exception as e:
            print(f"Error in SpaceX Agent: {e}")
            # Return fallback data in case of an error
            return {
                "mission_name": "Unknown Launch",
                "launch_date": "Unknown",
                "details": "Could not retrieve launch details",
                "launch_location": {
                    "name": "Kennedy Space Center (default)",
                    "location": "Merritt Island, FL",
                    "latitude": 28.6080585,
                    "longitude": -80.6039558
                }
            }