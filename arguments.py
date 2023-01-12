import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-db", "--hostname", help="Cluster hostname")
parser.add_argument("-u", "--username", help="ADmin user name")
parser.add_argument("-p", "--password", help="Password")
parser.add_argument("-t", "--token", help="JWT Token")
parser.add_argument("-r", "--refreshJWT", help="Refresh Token JWT")

global arguments

arguments = parser.parse_args()