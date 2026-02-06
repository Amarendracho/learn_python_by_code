# Python doesn’t care what an object is. It only cares what an object can do.
# No inheritance No interface No type checking Same method name → works

class FileLogger:
    def log(self, msg):
        print("File:", msg)

class DBLogger:
    def log(self, msg):
        print("DB:", msg)

def write_log(logger):
    logger.log("Something happened")

write_log(FileLogger())
write_log(DBLogger())

