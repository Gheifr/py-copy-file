from os.path import exists


def copy_file(command: str) -> None:
    args = command.split(" ")
    if len(args) != 3:
        return
    if args[0] != "cp":
        return

    source_file = args[1]
    target_file = args[2]

    if not source_file == target_file and exists(source_file):
        with (open(target_file, "w") as target,
              open(source_file, "r") as source):
            try:
                target.writelines(source.readlines())
            except FileNotFoundError:
                raise
