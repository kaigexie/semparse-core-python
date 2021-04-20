from jpype import *
import os


def parse_in_batch(sentences):

    startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (os.getcwd() + "/semparse-core.jar"))
    JDClass = JClass("VerbNetParserPython")
    jd = JDClass()

    args = java.util.ArrayList()
    for s in sentences:
        args.add(s)
    parsed_predicates = list(jd.parse(args))

    # shutdownJVM()

    return parsed_predicates


if __name__ == "__main__":

    sentences = ["They stole the painting from the museum", "Brown presented a plaque to Jones"]
    parsed_predicates = parse_in_batch(sentences)
    print(parsed_predicates)