import multiprocessing
import sys
import time

import lib.debug as debug
import lib.io as io
import processor

commands = processor.COMMAND_LIST


def display_general_usage():
    io.kindness_message("Usage:")
    io.command_message("    d++ command [command option]")
    io.blank()
    io.kindness_message("These are d++ commands used in various situations:")
    for option in commands.keys():
        io.command_message("    %-10s\t%s" % (option, commands[option]["help"]))
    io.blank()


def main_driver():
    if len(sys.argv) > 1:
        if sys.argv[1] in commands.keys():
            return commands[sys.argv[1]]["function"]()
        else:
            io.error_message("'%s' is not a valid command" % sys.argv[1])
    else:
        io.kindness_message("Defects4C++: Defect Taxonomies for Automated-Debugging")
        io.kindness_message("MIT Licensed, Suresoft Technologies Inc.")
        io.blank()
        display_general_usage()
        return False


if __name__ == "__main__":
    multiprocessing.freeze_support()
    start_time = time.time()
    try:
        main_driver()
    except:
        traceback_msg = debug.get_trace_back()
        io.error_message(traceback_msg)
        pass
    finally:
        sys.exit(0)