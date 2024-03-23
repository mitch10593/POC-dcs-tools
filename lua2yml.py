from lupa import LuaRuntime
from app.timer import timer
import yaml
import argparse

def lua_to_python(lua_table):
    """Convert Lua Table to Python objects

    Args:
        lua_table (LuaTable):

    Returns:
        list|dict|tuple:
    """
    if isinstance(lua_table, list):
        return [lua_to_python(v) for v in lua_table]
    elif isinstance(lua_table, str):
        return lua_table
    elif isinstance(lua_table, int):
        return lua_table
    elif isinstance(lua_table, float):
        return lua_table
    elif isinstance(lua_table, bool):
        return lua_table
    else:
        return {k: lua_to_python(v) for k, v in lua_table.items()}

def sort_by_field(data: list|tuple|dict, field:str):
    """sort items by field
    
    Sort items by field value (default: ASC) and rewrite indexes

    Args:
        data (list | tuple | dict): collection to be ordered

    Returns:
        list | tuple | dict: ordered items
    """
    
    sorted_items = sorted(data.items(), key=lambda x: x[1][field])
    sorted_data = {index + 1: item[1] for index, item in enumerate(sorted_items)}

    return sorted_data

def sort_groups_by_name(data):
    """_summary_

    Args:
        data (_type_): _description_
    """

def sort_mission(mission):
    """Sort mission data
    
    Sort all mission sortable data by name

    Args:
        mission (_type_): _description_
    """
    
    # on each coalition
    for coalition in ("blue", "red", "neutral"):
        if coalition in mission["coalition"]:
            mission["coalition"][coalition]["country"] = sort_by_field(mission["coalition"][coalition]["country"], "name")
            
            # on each coalition's country
            for country_key,country in mission["coalition"][coalition]["country"].items():

                # on each asset category in a coalition's country
                for category in ("helicopter", "plane", "ship", "static", "vehicle"):
                    if category in country:
                         country[category]["group"] = sort_by_field(country[category]["group"], "name")
                

@timer
def convert_mission_lua_to_yaml(lua_file_path:str, yaml_file_path:str):
    """Convert a LUA file (array) to Yaml

    Args:
        lua_file_path (str): 
        yaml_file_path (str):
    """
    print(f"converting {lua_file_path} to {yaml_file_path}: ",end="")
    with open(lua_file_path, 'r') as lua_file:
        with open(yaml_file_path, 'w') as yaml_file:
            lua_code = lua_file.read()

            lua = LuaRuntime(unpack_returned_tuples=True)
            lua.execute(lua_code)
            lua_dict = lua.globals().mission
            
            mission = lua_to_python(lua_dict)
            sort_mission(mission)
            yaml.dump(mission, yaml_file, sort_keys=True)
            print("done")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Lua mission to YAML format')
    parser.add_argument('mission_lua', type=str, help='Path to the original mission file (lua)')
    parser.add_argument('mission_yaml', type=str, help='Path to the destination mission file (yaml)')
    args = parser.parse_args()
    
    convert_mission_lua_to_yaml(args.mission_lua, args.mission_yaml)