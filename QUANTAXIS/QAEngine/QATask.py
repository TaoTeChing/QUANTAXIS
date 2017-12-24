#
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import queue
import threading
import time

from QUANTAXIS.QAUtil import QA_Setting, QA_util_log_info
from QUANTAXIS.QAUtil.QARandom import QA_util_random_with_topic

"""
标准的QUANTAXIS事件方法,具有QA_Thread,QA_Event等特性,以及一些日志和外部接口
"""


class QA_Task():
    def __init__(self, job, event, callback=False):
        self.job = job
        self.event = event
        self.res = None
        self.callback = callback
        self.task_id = QA_util_random_with_topic('Task')
    
    def do(self):
        self.res = self.job.run(self.event)
        if self.callback:
            self.callback(self.res)

    @property
    def result(self):
        # return {
        #     'task_id': self.task_id,
        #     'result': self.res,
        #     'job': self.job,
        #     'event': self.event
        # }
        return {
            'task_id': self.task_id,
            'result': self.res
        }


if __name__ == '__main__':
    pass