import os

def get_files_info(working_directory, direcotry=None):
    try:
        if directory is None:
            directory = "."

        full_path = os.path.join(working_directory, directory)

        working_dir_abs = os.path.abspath(working_directory)
        target_dir_abs = os.path.abspath(full_path)

        working_dir_abs = os.path.normpath(working_dir_abs)
        target_dir_abs = os.path.normpath(target_dir_abs)

        if not (target_dir_abs.startswith(working_dir_abs) and (target_dir_abs == working_dir_abs or target_dir_abs.startwith(working_dir_abs + os.sep))):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.exists(target_dir_abs):
            return f'Error: "{directory}" does not exist'

        if not os.path.isdir(target_dir_abs):
            return f'Error: "{directory}" is not a directory'

        contents = os.listdir(target_dir_abs)

        result_lines = []
        for item in contents:
            item_path = os.path.join(target_dir_abs, item)
            try:
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                result_lines.append(f" - {item}: file_size={file_size} bytes, is_dir={is_dir}")
            except OSError as e:
                result_lines.append(f" - {item}: Error getting info - {str(e)}")

        return "\n".join(result_lines)

    except Exception as e:
        return f'Error: {str(e)}'
