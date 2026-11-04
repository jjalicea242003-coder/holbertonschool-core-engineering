#!/usr/bin/env python3

print("{}".format("".join([chr(i) for i in range(97, 123) if cjr(i) not in "qe"])))
