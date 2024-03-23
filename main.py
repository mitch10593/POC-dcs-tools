import sys
import ast
from lupa import LuaRuntime
from collections import OrderedDict
import yaml
import argparse
import time

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"exec of {func.__name__} in {execution_time:.2f} seconds")
        return result
    return wrapper
    

def lua_to_python(lua_table):
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
    elif isinstance(lua_table, dict) or True:
        return {k: lua_to_python(v) for k, v in lua_table.items()}
    else:
        return lua_table

@calculate_execution_time
def convert_file_lua_to_yaml(lua_file_path:str, yaml_file_path:str):
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
            
            data = lua_to_python(lua_dict)
            yaml.dump(data, yaml_file, sort_keys=True)
            print("done")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Lua mission to YAML format')
    parser.add_argument('mission_lua', type=str, help='Path to the original mission file (lua)')
    parser.add_argument('mission_yaml', type=str, help='Path to the destination mission file (yaml)')
    args = parser.parse_args()
    
    convert_file_lua_to_yaml(args.mission_lua, args.mission_yaml)