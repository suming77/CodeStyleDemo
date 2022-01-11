#-- coding: utf-8 --
import sys

template = """
{Type}:{Subject}

{Body}

{Footer}

-------参数说明------
{Type}, {Subject} 不能为空
{Body}, {Footer} 前必须空一行
Type 必须是以下类型
    feat:新功能
    fix:修复bug
    style:格式变动，不影响代码运行
    refactor:重构
    perf:新能优化
    test:增加测试
    docs:文档
    chore:构建过程或辅助工具的变动
Subject 摘要，概述。一句话描述本次提交的目的，不能为空
Body: 详细描述本次提交。比如：修改了什么，增加了什么，删除了什么等。
Footer:
     BREAKING CHANGE:不兼容的改动
     Closes:关闭issue。如#123, #245, #992O 。 CLOSE: #BOS-1273
"""

msgFileName = sys.argv[1]

inputs = []

with open(msgFileName, "r", encoding = "utf-8") as f:
    for l in f.readlines():
        if l.startswith("#"):
            inputs.append("")
        else:
            inputs.append(l)

if len(inputs) < 1:
    print("需要填写提交信息")
    exit(1)

while len(inputs) > 0:
    if "" == inputs[-1].strip():
        inputs.pop()
    else:
        break

size = len(inputs)
if size != 1 and size != 3 and size != 5:
    print(f"提交格式不正确: line.size: {size}")
    exit(1)

if size == 5 and inputs[3].strip() != "":
    print("{Footer}前需要有空行")
    exit(1)

if size == 3 and inputs[1].strip() != "":
    print("{Body}前需要有空行")
    exit(1)

head = inputs[0]
if ":" not in head:
    print("需要用 : 分割{Type}和{Subject}")
    exit(1)

l = head.index(":")
if 0 == l:
    print("缺少{Type}")
    exit(1)
if len(head) == l+1:
    print("缺少{Subject}")
    exit(1)

type = head[:l].strip()
subject = head[:l].strip()
types = ["feat", "fix", "style", "refactor", "perf", "test", "docs", "chore"]

if type not in types:
    print(f"类型不正确 {{Type}}: {type}")
    exit(1)

if "" == subject:
    print("{Subject}不能为空")
    exit(1)

exit(0)
