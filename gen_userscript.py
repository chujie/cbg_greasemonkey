import re
import glob
import jsbeautifier
import json

manifest = json.load(open("cbg_chrome/src/manifest.json"))
START_SYM = "//chrome-only{"
END_SYM = "//}chrome-only-ends"
START = re.escape(START_SYM)
END = re.escape(END_SYM)
pattern = re.compile(f"{START}.*?{END}", flags=re.S)
path_to_js = 'cbg_chrome/src/js/*.js'
package_version = manifest['version']
META_INFO = """
// ==UserScript==
// @name         CBG Helper
// @namespace    https://yys.zhebu.work/
// @version      {VER}
// @description  A helper tool for Onmyoji player to look for good account.
// @author       CJ
// @match        https://yys.cbg.163.com/*
// @grant        none
// @run-at       document-start
// ==/UserScript==
""".format(VER=package_version)


with open("src/addon.js") as fd:
    addon = fd.read(None)

output = ""
for file in glob.glob(path_to_js):
    with open(file, 'r') as fd:
        buffer = "".join(fd.readlines())
        output += pattern.sub('', buffer)

output = jsbeautifier.beautify("(function(){\n'use strict';\n"+output+addon+"})()")

with open('src/main.js', 'w') as of:
    of.write(META_INFO)
    of.write(re.sub(r"([ \t]*\n){3,}", "\n", output, flags=re.S))








