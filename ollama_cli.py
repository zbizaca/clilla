import argparse
import subprocess
import sys


def execute_ollama_command(command: list[str]) -> tuple[int, str]:
    '''
        Executes `ollama` CLI command and streams the output to `stdout` as it is created.


    Args:
        command (list[str]): non-empty, contains command, optionally followed by any required parameter 

    Returns:
        tuple[int, str]: return code, error_output or `None`
    '''

    process = subprocess.Popen(
        ['ollama'] + command,  # NOTE: hardcode the sys command here for security
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1  # Line-buffered
    )

    # Read output line by line as it's generated
    for line in process.stdout:
        print(line, end='', flush=True)

    process.stdout.close()
    process.wait()

    return_code = process.returncode
    error_output = 0
    if return_code != 0:
        error_output = process.stderr.read()
    return error_output, return_code


def main():
    parser = argparse.ArgumentParser(
        prog='python ollama_cli.py',
        description='Python CLI wrapper for Ollama')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # list command
    list_parser = subparsers.add_parser(
        'list', help='List available Ollama models')

    # run command
    run_parser = subparsers.add_parser(
        'run', help='Run an Ollama model with a prompt')
    run_parser.add_argument('model', help='Model name to run (e.g., llama2)')
    run_parser.add_argument('prompt', help='Prompt to send to the model')

    try:
        args = parser.parse_args()

        if args.command == 'list':
            command = ['list']
        elif args.command == 'run':
            command = ['run', args.model, args.prompt]
        else:
            parser.print_help()
            sys.exit(1)

        code, error_message = execute_ollama_command(command)
        if code != 0:
            print(
                f'\nError running "ollama {command[0]}": {error_message}', file=sys.stderr)
            sys.exit(code)

    except Exception as e:
        print(e)
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
