import gdb

class pnext(gdb.Command):
    def __init__(self):
        super(self.__class__, self).__init__("pnext", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        
        try:
            variable = gdb.parse_and_eval(argv[0])
        except gdb.error as e:
            print(e)
            return

        point = variable

        if len(argv) > 3:
            raise gdb.GdbError('Usage: pnext [head] [next] [length]')

        next_p = 'next'
        if len(argv) > 1:
            next_p = argv[1]
            try:
                check = point[next_p].dereference()
            except gdb.error as e:
                print("Oops! ", e)
                return

        count = 50
        if len(argv) > 2:
            try:
                count = int(argv[2])
            except ValueError:
                print("Oops!  That was no valid number", argv[2])
                return

        while point:
            if count == 0:
                break
            print(point.dereference())
            point = point[next_p]
            count -= 1
pnext()
