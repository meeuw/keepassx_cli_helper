import subprocess

def show(secret_tool_attribute, secret_tool_value, keepassx_cli_database, keepassx_cli_entry):
    keypass = subprocess.check_output(['secret-tool', 'lookup', secret_tool_attribute, secret_tool_value])
    p = subprocess.Popen(['keepassxc-cli', 'show', keepassx_cli_database, keepassx_cli_entry, '-a', 'Password'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate(keypass)[0].split(b'\n')[1]

def extract(secret_tool_attribute, secret_tool_value, keepassx_cli_database):
    keypass = subprocess.check_output(['secret-tool', 'lookup', secret_tool_attribute, secret_tool_value])
    p = subprocess.Popen(['keepassxc-cli', 'extract', keepassx_cli_database], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate(keypass)[0]
    return output[output.find(b"<?xml"):]
