#
import atexit
import sys

sys.setrecursionlimit(1000000)


def getIntList():
	return list(map(int, input().split()))


try:
	# raise ModuleNotFoundError

	def dprint(*args, **kwargs):
		# print(*args, **kwargs, file=sys.stderr)
		# in python 3.4 **kwargs is invalid???
		print(*args, file=sys.stderr)

	dprint("debug mode")
except Exception:

	def dprint(*args, **kwargs):
		pass


inId = 0
outId = 0
if 0 < inId:
	dprint("use input", inId)
	sys.stdin = open(str(inId) + "input" + ".txt")  # 标准输出重定向至文件
if outId > 0:
	dprint("use output", outId)
	sys.stdout = open(str(outId) + "stdout" + ".txt", "w")  # 标准输出重定向至文件
	atexit.register(lambda: sys.stdout.close())  # idle 中不会执行 atexit

(N,) = getIntList()
# print(N)
re = 0
for i in range(2, N):
	t = N // i - 1
	re += t * i

print(4 * re)
