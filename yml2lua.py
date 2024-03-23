import yaml
import argparse
from app.timer import timer
    

def yaml_to_lua(yaml_data:list|tuple|dict, indent:int=0) -> str:
    """Convert yaml array to lua string

    Args:
        yaml_data (list | tuple | dict): _description_
    """
    lua_code = ""
    indentation = " " * (indent+4)
    indentation_term = " " * indent
    
    if isinstance(yaml_data, dict):
        lua_code += "{\r\n"
        for key, value in yaml_data.items():
            if isinstance(key, int):
                lua_code += f"{indentation}[{key}] = "
            else:
                lua_code += f"{indentation}[\"{key}\"] = "
            lua_code += yaml_to_lua(value, indent + 4)
            lua_code += ",\r\n"
        lua_code += indentation_term + "}"
    elif isinstance(yaml_data, list):
        lua_code += "{\r\n"
        for item in yaml_data:
            lua_code += indentation + yaml_to_lua(item, indent + 4) + ",\r\n"
        lua_code += indentation_term + "}"
    elif isinstance(yaml_data, str):
        lua_code += '"' + yaml_data.replace("\\","\\\\").replace('"','\\"').replace("\n", "\\\r\n") + '"'
    elif isinstance(yaml_data, bool):
        if yaml_data:
            lua_code += "true"
        else:
            lua_code += "false"
    else:
        lua_code += str(yaml_data)

    return lua_code

@timer
def convert_mission_yaml_to_lua(yaml_file_path:str, lua_file_path:str):
    """Convert a YAML file to LUA

    Args:
        yaml_file_path (str):
        lua_file_path (str): 
    """
    print(f"converting {yaml_file_path} to {lua_file_path}: ",end="")

    with open(yaml_file_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        
        with open(lua_file_path, 'w') as lua_file:

            lua_code = yaml_to_lua(yaml_data)       

            lua_file.write("mission = " + lua_code)
            print("done")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert mission from YAML format to DCS LUA")
    parser.add_argument("mission_yaml", type=str, help="Path to the source mission file (yml)")
    parser.add_argument("mission_lua", type=str, help="Path to the destination mission file (lua)")
    args = parser.parse_args()
    
    convert_mission_yaml_to_lua(args.mission_yaml, args.mission_lua)