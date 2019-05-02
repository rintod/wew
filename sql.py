#!/usr/bin/python
# Created By Con7ext
# CSE API KEY : Teguh Aprianto
from urllib.request import Request as ntodReq, urlopen as ntodOpen
import re
import urllib.error

errorSql = []
try:
  f = open("error.txt", "r")
  for name in f.readlines():
    if len(name.strip())>0: 
      errorSql.append(name.strip())
  f.close()
except (FileNotFound, IOError):
  print("File Error.txt Not Found :|")

OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
OKBLUE = '\033[94m'

def ntodRequest(url):
  httpReq = ntodReq(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"})
  httpResp = ntodOpen(httpReq, timeout=10)
  httpBody = httpResp.read().decode("utf8")
  return httpBody
def checkSql(url):
  try:
    httpReq = ntodRequest(url+"'")
    for errors in errorSql:
      if errors in httpReq:
        return OKGREEN + url + " >> OK" + ENDC
      return FAIL + url + " >> BAD" + ENDC
  except urllib.error.HTTPError as e:
    return WARNING + url + " >> {} {}".format(e.code, e.reason)  + OKBLUE + " [!] Try Open By Your Self :D" + ENDC
  except urllib.error.URLError:
    return FAIL + url + " >> URL ERROR" + ENDC
  except:
    return FAIL + url + " >> Unknow ERROR" + ENDC
def googleSearch(args, page):
  if " " in args:
    search = args.replace(" ", "%20")
  else:
    search = args
  httpReq = ntodRequest("https://cse.google.com/cse.js?cx=partner-pub-2698861478625135:3033704849")
  cse_token = re.findall(r"\"cse_token\": \"(.*?)\"", str(httpReq))
  httpReqs = ntodRequest("https://cse.google.com/cse/element/v1?num=10&hl=en&cx=partner-pub-2698861478625135:3033704849&safe=off&cse_tok=%s&start=%d&q=%s&callback=x" % (cse_token[0], page, search))
  result = re.findall(r"\"unescapedUrl\": \"(.*?)\"", str(httpReqs))
  print("=== Page %d ===" % (page))
  for url in result:
    if url is None:return
    print(checkSql(url))
  
print("Author : Con7ext")
print("Tools  : Sql Scanner")
try:
  ugh = int(input("1. Scan Your List\n2. Scan By Search\n>> "))
except ValueError:
  print(OKBLUE + "Please Only Enter 1-2 :|" + ENDC)
if ugh == 1:
  liss = input("Enter Your List(FILE): ")
  try:
    f = open(liss, "r")
    ngenx = f.read().split("\n")
    for cok in ngenx:
      print(checkSql(cok))
  except (FileNotFoundError, IOError):
    print(OKBLUE + "Your File Entered Not Found!!" + ENDC)
elif ugh == 2:
  dork = input("Enter Dork: ")
  rangee = int(input("From Page 1 To?: "))
  rangee += 1
  for i in range(1, rangee):
    googleSearch(dork, i)
