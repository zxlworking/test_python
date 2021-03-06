import cgi, cgitb
import json
import sys
import time
from com_zxl_common.DBUtil import *
from com_zxl_common.PrintUtil import *

reload(sys)
sys.setdefaultencoding("utf8")

form = cgi.FieldStorage()
page = form.getvalue("page")
count = form.getvalue("count")

mDBUtil = DBUtil()
mPrintUtil = PrintUtil()
result = {}

if page is None or count is None:
    result["code"] = -1
    result["desc"] = "param error"
else:
    if not result is None:
        total_count = mDBUtil.query_to_calculate_total_count()
        total_page = int(total_count) / int(count) + 1

        total_count = mDBUtil.query_to_calculate_total_count()
        total_count = int(total_count) / int(count) + 1

        result_element_list = mDBUtil.query_to_calculate(page, count)

        result["code"] = 0
        result["desc"] = "success"
        result["total_page"] = total_page
        result["page_count"] = count
        result["current_page"] = page
        result["result"] = result_element_list
    else:
        result["code"] = -2
        result["desc"] = "no data"

print "Content-type:text/html"
print ""
print json.dumps(result, encoding="utf-8", ensure_ascii=False)