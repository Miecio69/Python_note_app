# Self-made class that's supposed to replicate the 'argparse' module.
# Just a side project to see how  hard it is, not an inherent part of program.

# def menu(input_value):
#     parts = input_value.split()
#     if parts and parts[0].lower() == "help":
#         new_input = input_value.replace('help', '').strip()
#         match new_input:
#             case "/":  # Info about all functions
#                 print("List of available commands:\n"
#                       "add\n"
#                       "delete")
#             case "add":  # Info about add
#                 print("*Info about add*")
#             case "delete":  # Info about delete
#                 print("Info about delete")
#             case _:
#                 print(f"Unknown command for '{input_value}'.\n"
#                       f"For a list of all commands type 'help /'\n"
#                       f"or type 'help *command name here*' for more info about specific command'")
#         return False
#     elif parts and parts[0].lower() == "exit":  # Exit program, breaks the loop
#         print("See you next time!")
#         return True
#
#     print(f"Unknown command for '{input_value}'.\n"
#           f"For a list of all commands type 'help /'\n"
#           f"or type 'help *command name here*' for more info about specific command'")
#     return False
