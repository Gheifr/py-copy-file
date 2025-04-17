from os.path import exists


def copy_file(command: str) -> None:
    args = command.split(" ")
    if len(args) != 3:
        return
    if args[0] != "cp":
        return

    source_file = args[1]
    target_file = args[2]

    if exists(source_file):
        if exists(target_file):
            with (open(target_file, "r") as target,
                  open(source_file, "r") as source):
                if source.read() == target.read():
                    return

        with (open(source_file, "r") as source,
              open(target_file, "w") as target):
            try:
                target.writelines(source.readlines())
            except FileNotFoundError:
                raise
